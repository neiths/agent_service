from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from core_app.chat_service.simple_chat_bot import load_llm_model
from core_app.chat_service.tool_basic import tools
from core_app.models import Conversation, SystemPrompt, Lecture

def convert_dict_to_template_message(dict_message):
    if dict_message["message_type"] == "human_message":
        return HumanMessage(dict_message["content"])
    elif dict_message["message_type"] == "ai_message":
        return AIMessage(dict_message["content"])
    else:
        raise Exception("Message type not supported")

def run_lecture_agent(input, chat_history, character, provider):
    # prompt search information from wikipedia (tools)
    
    system_prompt_qs = SystemPrompt.objects.filter(character=character)
    if not system_prompt_qs.exists():
        raise Exception("Character not found")
    
    # get system prompt
    system_prompt_instance = system_prompt_qs.first()
    system_prompt = system_prompt_instance.prompt
    
    # system prompt content
    system_prompt_content=f"""{system_prompt} \n
                           You can call tool function 'query_data_from_db_table' to get information from database with input: 'query_data_from_db_table('subject', 'chapter')'"""

    # create system prompt
    system_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt_content
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    # load llm model
    llm = load_llm_model(provider="google")

    # create agent constructor
    agent = create_tool_calling_agent(llm, tools, system_prompt)

    # create agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # invoke agent
    output = agent_executor.invoke({"input": input, "chat_history": []})

    return output


def get_message_from_agent(conversation_id, user_message):
    # get conversation instance
    conversation_instance_qs = Conversation.objects.filter(id=conversation_id)
    if not conversation_instance_qs.exists():
        raise Exception("Conversation id not found")
    conversation_instance = conversation_instance_qs.first()

    # get character and provider
    character = conversation_instance.prompt_name
    provider = conversation_instance.gpt_model

    # get chat history
    chat_history_dicts = conversation_instance.chat_history
    chat_history = [
        convert_dict_to_template_message(chat_history_dict)
        for chat_history_dict in chat_history_dicts
    ]

    # run agent
    response = run_lecture_agent(
        user_message, chat_history, character=character, provider=provider
    )
    
    print("output_agent--------------------------")
    print(response)

    # update chat history
    conversation_instance.chat_history.append({"message_type": "human_message", "content": user_message})
    conversation_instance.chat_history.append({"message_type": "ai_message", "content": response['output']}) 
    
    # save conversation instance
    conversation_instance.save()
    
    return response