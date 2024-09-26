# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ocr_service_pb2 as ocr__service__pb2


class OCRSserviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTextFromFile = channel.unary_unary(
                '/pb.OCRSservice/CreateTextFromFile',
                request_serializer=ocr__service__pb2.FileRequest.SerializeToString,
                response_deserializer=ocr__service__pb2.FileResponse.FromString,
                )


class OCRSserviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTextFromFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OCRSserviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTextFromFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTextFromFile,
                    request_deserializer=ocr__service__pb2.FileRequest.FromString,
                    response_serializer=ocr__service__pb2.FileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.OCRSservice', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OCRSservice(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTextFromFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.OCRSservice/CreateTextFromFile',
            ocr__service__pb2.FileRequest.SerializeToString,
            ocr__service__pb2.FileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
