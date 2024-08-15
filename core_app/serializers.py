from rest_framework import serializers
from .models import Conversation, SystemPrompt, ExternalKnowledge, Agent, AgentTool, LlmModel, InternalKnowledge

class LlmModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LlmModel
        fields = ['id', 'llm_name', 'provider', 'model_version', 'user', 'api_key']  # Exclude api_key for security
        read_only_fields = ['id', 'user']  # Ensure some fields are read-only


class ConversationSerializer(serializers.ModelSerializer):
    chat_history = serializers.ListField(child=serializers.DictField(), required=False, allow_empty=True)
    class Meta:
        model = Conversation
        fields = ['id', 'agent', 'chat_history']

class SystemPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemPrompt
        fields = '__all__'

class ExternalKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalKnowledge
        fields = ['subject', 'chapter', 'content']

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['agent_name', 'llm', 'prompt', 'tools']
        
class AgentToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentTool
        fields = '__all__'
        
class InternalKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalKnowledge
        fields = '__all__'