from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from ca_vntl_helper import error_tracking_decorator
import os
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from .agent_tool import tool_mapping, retrieve_documents_with_rrf
from langchain_core.output_parsers import StrOutputParser


class AgentCreator:
    def __init__(self, agent_name: str, llm_type: str, prompt_content: str, tools: list[str]):
        self.agent_name = agent_name
        self.llm_type = llm_type
        self.prompt_content = prompt_content
        self.tools_str = tools
        self.hidden_prompt = """ """
        #         "Generate an output on the given question. Then, summarize this output in one sentence and create a relevant hashtag. Ensure the summary and hashtag accurately reflect the content of the output.
        #         question: user's question
        #         Actual Output: (Write the main content here)
        #         Summary: (Summarize the main content in one sentence)
        #         Hashtag: (Create some hashtags that captures the essence of the content)"
        #         if you can not summarize the content, you can write the content in the summary section.
        #         Example
        #             When user's input: The impact of remote work on productivity
        #             your output should be:
        #             format:
        #             - Actual Output: The shift to remote work has significantly altered the dynamics of workplace productivity. While some employees report higher levels of efficiency and better work-life balance, others struggle with distractions and isolation. Companies are investing in new tools and technologies to support remote teams, fostering collaboration and communication. Overall, the impact on productivity varies widely among different industries and individual circumstances.
        #             - Summary: Remote work's impact on productivity varies, with some finding increased efficiency and others facing challenges.
        #             - Hashtag: #RemoteWorkEffect #ProductivityImpact #WorkplaceDynamics ,....."
        # """

    def load_tools(self):
        tools = []
        for tool_str in self.tools_str:
            tools.append(tool_mapping[tool_str])
        
        return tools

    def load_llm(self):
        if self.llm_type == "openai":
            OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
            llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
        else:
            raise Exception("LLM type not supported")
        return llm

    def create_system_prompt_template(self):

        system_prompt_content = self.prompt_content + "\n following the format below to generate the output. Remember: always follow format No matter what happens.\n" + self.hidden_prompt

        system_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt_content),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ])
        return system_prompt
    
    def create_multi_queries(self, user_input):
        template = """You are an AI language model assistant. Your task is to generate five 
        different versions of the given user question to retrieve relevant documents from a vector 
        database. By generating multiple perspectives on the user question, your goal is to help
        the user overcome some of the limitations of the distance-based similarity search. 
        Provide these alternative questions separated by newlines. Original question: {question}"""
        prompt_perspectives = ChatPromptTemplate.from_template(template)
        llm = self.load_llm()
        generate_queries = (
            prompt_perspectives 
            | llm
            | StrOutputParser() 
            | (lambda x: x.split("\n"))
        )
        
        return generate_queries.invoke({"question": user_input})

    def create_agent_runnable(self):
        system_prompt = self.create_system_prompt_template()
        llm = self.load_llm()
        tools = self.load_tools()
        agent_runnable = create_tool_calling_agent(llm, tools, system_prompt)
        return agent_runnable, tools

    def create_agent_executor(self):
        agent, tools = self.create_agent_runnable()
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        return agent_executor

    def get_message_from_agent(self, user_message, chat_history):
        agent_exec = self.create_agent_executor()
        output = agent_exec.invoke({"input": user_message, "chat_history": chat_history})
        return output['output']


@error_tracking_decorator
def run_chatbot(input_text, chat_history, agent_role, llm_type="openai", prompt_content="", user_tools=[]):
        
    agent_instance = AgentCreator(agent_name=agent_role, llm_type=llm_type, prompt_content=prompt_content,
                                  tools=user_tools)
    
    top_knowledge = retrieve_documents_with_rrf(agent_instance, input_text)
    
    context = "".join([content for content, _ in top_knowledge])
    
    enhanced_input = f"according to the knowledge base, {context}. {input_text}"
    
    
    output_message = agent_instance.get_message_from_agent(enhanced_input, chat_history)

    return output_message

# agent = AgentCreator(agent_name="chatbot", llm_type="openai", prompt_content="Hello! How can I assist you today?", tools=[])
# print(agent.create_multi_queries("What is the capital of France?"))