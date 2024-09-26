# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LlmModel.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import core_app.grpc.pb.UUID_pb2 as UUID__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eLlmModel.proto\x12\x02pb\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\nUUID.proto\"\xe7\x01\n\x08LlmModel\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08llm_name\x18\x04 \x01(\t\x12\x10\n\x08provider\x18\x05 \x01(\t\x12\x15\n\rmodel_version\x18\x06 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x07 \x01(\t\x12\x19\n\x07user_id\x18\x08 \x01(\x0b\x32\x08.pb.UUID\"7\n\x15\x43reateLlmModelRequest\x12\x1e\n\x08llmmodel\x18\x01 \x01(\x0b\x32\x0c.pb.LlmModel\".\n\x16\x43reateLlmModelResponse\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\"*\n\x12GetLlmModelRequest\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\"5\n\x13GetLlmModelResponse\x12\x1e\n\x08llmmodel\x18\x01 \x01(\x0b\x32\x0c.pb.LlmModel\"\x16\n\x14ListLlmModelsRequest\"8\n\x15ListLlmModelsResponse\x12\x1f\n\tllmmodels\x18\x01 \x03(\x0b\x32\x0c.pb.LlmModel\"7\n\x15UpdateLlmModelRequest\x12\x1e\n\x08llmmodel\x18\x01 \x01(\x0b\x32\x0c.pb.LlmModel\"\x18\n\x16UpdateLlmModelResponse\"-\n\x15\x44\x65leteLlmModelRequest\x12\x14\n\x02id\x18\x01 \x01(\x0b\x32\x08.pb.UUID\"\x18\n\x16\x44\x65leteLlmModelResponse2\xff\x02\n\x12LlmModelController\x12I\n\x0e\x43reateLlmModel\x12\x19.pb.CreateLlmModelRequest\x1a\x1a.pb.CreateLlmModelResponse\"\x00\x12@\n\x0bGetLlmModel\x12\x16.pb.GetLlmModelRequest\x1a\x17.pb.GetLlmModelResponse\"\x00\x12\x46\n\rListLlmModels\x12\x18.pb.ListLlmModelsRequest\x1a\x19.pb.ListLlmModelsResponse\"\x00\x12I\n\x0eUpdateLlmModel\x12\x19.pb.UpdateLlmModelRequest\x1a\x1a.pb.UpdateLlmModelResponse\"\x00\x12I\n\x0e\x44\x65leteLlmModel\x12\x19.pb.DeleteLlmModelRequest\x1a\x1a.pb.DeleteLlmModelResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LlmModel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LLMMODEL']._serialized_start=68
  _globals['_LLMMODEL']._serialized_end=299
  _globals['_CREATELLMMODELREQUEST']._serialized_start=301
  _globals['_CREATELLMMODELREQUEST']._serialized_end=356
  _globals['_CREATELLMMODELRESPONSE']._serialized_start=358
  _globals['_CREATELLMMODELRESPONSE']._serialized_end=404
  _globals['_GETLLMMODELREQUEST']._serialized_start=406
  _globals['_GETLLMMODELREQUEST']._serialized_end=448
  _globals['_GETLLMMODELRESPONSE']._serialized_start=450
  _globals['_GETLLMMODELRESPONSE']._serialized_end=503
  _globals['_LISTLLMMODELSREQUEST']._serialized_start=505
  _globals['_LISTLLMMODELSREQUEST']._serialized_end=527
  _globals['_LISTLLMMODELSRESPONSE']._serialized_start=529
  _globals['_LISTLLMMODELSRESPONSE']._serialized_end=585
  _globals['_UPDATELLMMODELREQUEST']._serialized_start=587
  _globals['_UPDATELLMMODELREQUEST']._serialized_end=642
  _globals['_UPDATELLMMODELRESPONSE']._serialized_start=644
  _globals['_UPDATELLMMODELRESPONSE']._serialized_end=668
  _globals['_DELETELLMMODELREQUEST']._serialized_start=670
  _globals['_DELETELLMMODELREQUEST']._serialized_end=715
  _globals['_DELETELLMMODELRESPONSE']._serialized_start=717
  _globals['_DELETELLMMODELRESPONSE']._serialized_end=741
  _globals['_LLMMODELCONTROLLER']._serialized_start=744
  _globals['_LLMMODELCONTROLLER']._serialized_end=1127
# @@protoc_insertion_point(module_scope)
