from django.shortcuts import render
from rest_framework import generics, status, permissions
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import Conversation, SystemPrompt, ExternalKnowledge, InternalKnowledge, Agent, AgentTool, LlmModel
from .serializers import ConversationSerializer, SystemPromptSerializer, ExternalKnowledgeSerializer, AgentSerializer, AgentToolSerializer, LlmModelSerializer, InternalKnowledgeSerializer
from core_app.chat_service.AgentMessage import get_message_from_agent, get_streaming_agent_instance
from core_app.extract import extract
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import HttpResponse, StreamingHttpResponse
from asgiref.sync import sync_to_async
from langchain.agents import AgentExecutor
import asyncio
import logging
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    
# create CRUD API views here with LlmModel models
class LlmModelListCreate(generics.ListCreateAPIView):
    queryset = LlmModel.objects.all().order_by('-updated_at')
    serializer_class = LlmModelSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated] # Ensure user is authenticated
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically associate the model with the current user
        
    def get_queryset(self):
        # Filter LlmModel objects to only those belonging to the logged-in user
        return LlmModel.objects.filter(user=self.request.user).order_by('-updated_at')
    
llm_list_create = LlmModelListCreate.as_view()
    
class LlmModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LlmModel.objects.all().order_by('-updated_at')
    serializer_class = LlmModelSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        serializer.save()
        
    def get_queryset(self):
        # Filter LlmModel objects to only those belonging to the logged-in user
        return LlmModel.objects.filter(user=self.request.user).order_by('-updated_at')
    

llm_retrieve_update_destroy = LlmModelRetrieveUpdateDestroy.as_view()

# Create CRUD API views here with Conversation models
class ConversationListCreate(generics.ListCreateAPIView):
    queryset = Conversation.objects.all().order_by('-updated_at')
    serializer_class = ConversationSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

conversation_list_create = ConversationListCreate.as_view()

class ConversationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all().order_by('-updated_at')
    serializer_class = ConversationSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

conversion_retrieve_update_destroy = ConversationRetrieveUpdateDestroy.as_view()


# create CRUD API views here with SystemPrompt models
class SystemPromptListCreate(generics.ListCreateAPIView):
    queryset = SystemPrompt.objects.all().order_by('-updated_at')
    serializer_class = SystemPromptSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

system_prompt_list_create = SystemPromptListCreate.as_view()

class SystemPromptRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystemPrompt.objects.all().order_by('-updated_at')
    serializer_class = SystemPromptSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

system_prompt_retrieve_update_destroy = SystemPromptRetrieveUpdateDestroy.as_view()


# create CRUD API views here with ExternalKnowledge models
class ExternalListCreate(generics.ListCreateAPIView):
    queryset = ExternalKnowledge.objects.all().order_by('-updated_at')
    serializer_class = ExternalKnowledgeSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

external_knowledge_list_create = ExternalListCreate.as_view()

class ExternalKnowledgeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExternalKnowledge.objects.all().order_by('-updated_at')
    serializer_class = ExternalKnowledgeSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

external_knowledge_retrieve_update_destroy = ExternalKnowledgeRetrieveUpdateDestroy.as_view()

# create CRUD API views here with Agent models
class AgentListCreate(generics.ListCreateAPIView):
    queryset = Agent.objects.all().order_by('-updated_at')
    serializer_class = AgentSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        agent_name = data.get("agent_name")
        llm = data.get("llm")
        tools = data.get("tools")
        prompt_id = data.get("prompt_id") or data.get("prompt")

        if prompt_id:
            prompt = SystemPrompt.objects.get(id=prompt_id)
        else:
            system_prompt_message = data.get("prompt_message")
            prompt = SystemPrompt(prompt_name=agent_name, prompt_content=system_prompt_message)
            prompt.save()
        agent = Agent.objects.create(agent_name=agent_name, llm=llm, prompt=prompt, tools=tools)
        agent.save()
        return Response(self.serializer_class(agent).data, status=status.HTTP_201_CREATED)


Agent_list_create = AgentListCreate.as_view()

class AgentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all().order_by('-updated_at')
    serializer_class = AgentSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

Agent_retrieve_update_destroy = AgentRetrieveUpdateDestroy.as_view()

# create CRUD API views here with AgentTool models
class AgentToolListCreate(generics.ListCreateAPIView):
    queryset = AgentTool.objects.all().order_by('-updated_at')
    serializer_class = AgentToolSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
AgentTool_list_create = AgentToolListCreate.as_view()

class AgentToolRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentTool.objects.all().order_by('-updated_at')
    serializer_class = AgentToolSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

AgentTool_retrieve_update_destroy = AgentToolRetrieveUpdateDestroy.as_view()
    
logger = logging.getLogger(__name__)
    
class AgentMessage(generics.CreateAPIView):
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["conversation_id", "message"],
            properties={
                "conversation_id": openapi.Schema(type=openapi.TYPE_STRING, format="uuid"),
                "message": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: openapi.Response("Successful response", schema=openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: "Bad Request",
        },
    )
    def post(self, request, *args, **kwargs):
        data = request.data
        message = data.get("message")
        conversation_id = data.get("conversation_id")
        try:
            # Get response from AI
            ai_response = get_message_from_agent(conversation_id, message)      
            return Response(ai_response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error processing request: {e}", exc_info=True)
            return Response({"ai_message": "Defined error", "human_message": message}, status=status.HTTP_400_BAD_REQUEST)
        
agent_answer_message = AgentMessage.as_view()

class AgentAnswerMessageStream(generics.GenericAPIView):
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["conversation_id", "message"],
            properties={
                "conversation_id": openapi.Schema(type=openapi.TYPE_STRING, format="uuid"),
                "message": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: openapi.Response("Successful response", schema=openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: "Bad Request",
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            print("response success")
            conversation_id = request.data.get("conversation_id")
            message = request.data.get("message")

            if not conversation_id or not message:
                return Response(
                    {"message": "conversation_id and message are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            agent_executor, chat_history, conversation_instance = get_streaming_agent_instance(conversation_id)

            async def on_chat_model_stream():
                
                final_event = None
                
                async for event in agent_executor.astream_events({'input': message, 'chat_history': chat_history},
                    version="v1",
                ):

                    if event['event'] == 'on_chat_model_stream':

                        # if event['data']['chunk'].content == "":
                        #     continue
                        print(f"data: {event['data']['chunk'].content} \n\n")
                        yield f"data: {event['data']['chunk'].content} \n\n"
                    if event["event"] == 'on_chain_end':
                        final_event = event["data"]["output"]

                await sync_to_async(conversation_instance.chat_history.append)({"message_type": "human_message", "content": message})
                await sync_to_async(conversation_instance.chat_history.append)({"message_type": "ai_message", "content": final_event['output']})
                await sync_to_async(conversation_instance.save)()

            response = StreamingHttpResponse(on_chat_model_stream(), content_type="text/event-stream", status=status.HTTP_200_OK)
            response["Cache-Control"] = "no-cache"
            
            return response

        except Exception as e:
            return Response(
                {"message": "failed", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

agent_answer_message_stream = AgentAnswerMessageStream.as_view()

class InternalKnowledgeList(generics.ListAPIView):
    queryset = InternalKnowledge.objects.all()
    serializer_class = InternalKnowledgeSerializer
    authentication_classes = [BearerTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        agent_id = self.kwargs.get('agent_id')
        
        # Lọc theo user và agent (nếu có)
        return InternalKnowledge.objects.filter(user=user, agent_id=agent_id)