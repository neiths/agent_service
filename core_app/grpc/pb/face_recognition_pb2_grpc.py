# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import face_recognition_pb2 as face__recognition__pb2


class FaceRecognitionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadImage = channel.unary_unary(
                '/pb.FaceRecognitionService/UploadImage',
                request_serializer=face__recognition__pb2.UploadImageRequest.SerializeToString,
                response_deserializer=face__recognition__pb2.UploadImageResponse.FromString,
                )
        self.UploadImageRecognition = channel.unary_unary(
                '/pb.FaceRecognitionService/UploadImageRecognition',
                request_serializer=face__recognition__pb2.ImageRecognition.SerializeToString,
                response_deserializer=face__recognition__pb2.DetailResponse.FromString,
                )


class FaceRecognitionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadImageRecognition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaceRecognitionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadImage': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadImage,
                    request_deserializer=face__recognition__pb2.UploadImageRequest.FromString,
                    response_serializer=face__recognition__pb2.UploadImageResponse.SerializeToString,
            ),
            'UploadImageRecognition': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadImageRecognition,
                    request_deserializer=face__recognition__pb2.ImageRecognition.FromString,
                    response_serializer=face__recognition__pb2.DetailResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.FaceRecognitionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FaceRecognitionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FaceRecognitionService/UploadImage',
            face__recognition__pb2.UploadImageRequest.SerializeToString,
            face__recognition__pb2.UploadImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadImageRecognition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FaceRecognitionService/UploadImageRecognition',
            face__recognition__pb2.ImageRecognition.SerializeToString,
            face__recognition__pb2.DetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
