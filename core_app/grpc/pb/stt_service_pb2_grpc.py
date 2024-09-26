# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import core_app.grpc.pb.stt_service_pb2 as stt__service__pb2


class STTServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadAudio = channel.unary_unary(
                '/pb.STTService/UploadAudio',
                request_serializer=stt__service__pb2.AudioFileRequest.SerializeToString,
                response_deserializer=stt__service__pb2.TranscriptionResponse.FromString,
                )
        self.StreamAudio = channel.stream_stream(
                '/pb.STTService/StreamAudio',
                request_serializer=stt__service__pb2.AudioChunkRequest.SerializeToString,
                response_deserializer=stt__service__pb2.TranscriptionStreamingResponse.FromString,
                )


class STTServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadAudio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamAudio(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_STTServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadAudio': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadAudio,
                    request_deserializer=stt__service__pb2.AudioFileRequest.FromString,
                    response_serializer=stt__service__pb2.TranscriptionResponse.SerializeToString,
            ),
            'StreamAudio': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamAudio,
                    request_deserializer=stt__service__pb2.AudioChunkRequest.FromString,
                    response_serializer=stt__service__pb2.TranscriptionStreamingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.STTService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class STTService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadAudio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.STTService/UploadAudio',
            stt__service__pb2.AudioFileRequest.SerializeToString,
            stt__service__pb2.TranscriptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamAudio(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/pb.STTService/StreamAudio',
            stt__service__pb2.AudioChunkRequest.SerializeToString,
            stt__service__pb2.TranscriptionStreamingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
