# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/requests/v1/requests.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'api/requests/v1/requests.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/requests/v1/requests.proto\x12\x03\x61pi\"7\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\t\"-\n\x0bRequestList\x12\x1e\n\x08requests\x18\x01 \x03(\x0b\x32\x0c.api.Request\"+\n\rRequestStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xcd\x01\n\x0eRequestService\x12+\n\x0bGetRequests\x12\n.api.Empty\x1a\x10.api.RequestList\x12+\n\rCreateRequest\x12\x0c.api.Request\x1a\x0c.api.Request\x12+\n\rUpdateRequest\x12\x0c.api.Request\x1a\x0c.api.Request\x12\x34\n\x10GetRequestStatus\x12\x0c.api.Request\x1a\x12.api.RequestStatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.requests.v1.requests_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST']._serialized_start=39
  _globals['_REQUEST']._serialized_end=94
  _globals['_REQUESTLIST']._serialized_start=96
  _globals['_REQUESTLIST']._serialized_end=141
  _globals['_REQUESTSTATUS']._serialized_start=143
  _globals['_REQUESTSTATUS']._serialized_end=186
  _globals['_EMPTY']._serialized_start=188
  _globals['_EMPTY']._serialized_end=195
  _globals['_REQUESTSERVICE']._serialized_start=198
  _globals['_REQUESTSERVICE']._serialized_end=403
# @@protoc_insertion_point(module_scope)
