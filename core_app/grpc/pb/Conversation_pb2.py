# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Conversation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import Agent_pb2 as Agent__pb2
import UUID_pb2 as UUID__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x43onversation.proto\x12\x02pb\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0b\x41gent.proto\x1a\nUUID.proto\"4\n\x0b\x43hathistory\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x14\n\x0cmessage_type\x18\x02 \x01(\t\"\x83\x02\n\x0c\x43onversation\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\x12%\n\x0c\x63hat_history\x18\x02 \x03(\x0b\x32\x0f.pb.Chathistory\x12!\n\x19is_use_internal_knowledge\x18\x03 \x01(\x08\x12\x18\n\x05\x61gent\x18\x04 \x01(\x0b\x32\t.pb.Agent\x12\x19\n\x07user_id\x18\x05 \x01(\x0b\x32\x08.pb.UUID\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"C\n\x19\x43reateConversationRequest\x12&\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x10.pb.Conversation\"2\n\x1a\x43reateConversationResponse\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\".\n\x16GetConversationRequest\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\"A\n\x17GetConversationResponse\x12&\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x10.pb.Conversation\"\x1a\n\x18ListConversationsRequest\"D\n\x19ListConversationsResponse\x12\'\n\rconversations\x18\x01 \x03(\x0b\x32\x10.pb.Conversation\"C\n\x19UpdateConversationRequest\x12&\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x10.pb.Conversation\"\x1c\n\x1aUpdateConverastionResponse\"1\n\x19\x44\x65leteConversationRequest\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\"\x1c\n\x1a\x44\x65leteConversationResponse2\xbf\x03\n\x16\x43onversationController\x12U\n\x12\x43reateConversation\x12\x1d.pb.CreateConversationRequest\x1a\x1e.pb.CreateConversationResponse\"\x00\x12L\n\x0fGetConversation\x12\x1a.pb.GetConversationRequest\x1a\x1b.pb.GetConversationResponse\"\x00\x12R\n\x11ListConversations\x12\x1c.pb.ListConversationsRequest\x1a\x1d.pb.ListConversationsResponse\"\x00\x12U\n\x12UpdateConversation\x12\x1d.pb.UpdateConversationRequest\x1a\x1e.pb.UpdateConverastionResponse\"\x00\x12U\n\x12\x44\x65leteConversation\x12\x1d.pb.DeleteConversationRequest\x1a\x1e.pb.DeleteConversationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Conversation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHATHISTORY']._serialized_start=84
  _globals['_CHATHISTORY']._serialized_end=136
  _globals['_CONVERSATION']._serialized_start=139
  _globals['_CONVERSATION']._serialized_end=398
  _globals['_CREATECONVERSATIONREQUEST']._serialized_start=400
  _globals['_CREATECONVERSATIONREQUEST']._serialized_end=467
  _globals['_CREATECONVERSATIONRESPONSE']._serialized_start=469
  _globals['_CREATECONVERSATIONRESPONSE']._serialized_end=519
  _globals['_GETCONVERSATIONREQUEST']._serialized_start=521
  _globals['_GETCONVERSATIONREQUEST']._serialized_end=567
  _globals['_GETCONVERSATIONRESPONSE']._serialized_start=569
  _globals['_GETCONVERSATIONRESPONSE']._serialized_end=634
  _globals['_LISTCONVERSATIONSREQUEST']._serialized_start=636
  _globals['_LISTCONVERSATIONSREQUEST']._serialized_end=662
  _globals['_LISTCONVERSATIONSRESPONSE']._serialized_start=664
  _globals['_LISTCONVERSATIONSRESPONSE']._serialized_end=732
  _globals['_UPDATECONVERSATIONREQUEST']._serialized_start=734
  _globals['_UPDATECONVERSATIONREQUEST']._serialized_end=801
  _globals['_UPDATECONVERASTIONRESPONSE']._serialized_start=803
  _globals['_UPDATECONVERASTIONRESPONSE']._serialized_end=831
  _globals['_DELETECONVERSATIONREQUEST']._serialized_start=833
  _globals['_DELETECONVERSATIONREQUEST']._serialized_end=882
  _globals['_DELETECONVERSATIONRESPONSE']._serialized_start=884
  _globals['_DELETECONVERSATIONRESPONSE']._serialized_end=912
  _globals['_CONVERSATIONCONTROLLER']._serialized_start=915
  _globals['_CONVERSATIONCONTROLLER']._serialized_end=1362
# @@protoc_insertion_point(module_scope)
