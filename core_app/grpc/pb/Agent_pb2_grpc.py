# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import core_app.grpc.pb.Agent_pb2 as Agent__pb2


class AgentControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAgent = channel.unary_unary(
                '/pb.AgentController/CreateAgent',
                request_serializer=Agent__pb2.CreateAgentRequest.SerializeToString,
                response_deserializer=Agent__pb2.CreateAgentResponse.FromString,
                )
        self.GetAgent = channel.unary_unary(
                '/pb.AgentController/GetAgent',
                request_serializer=Agent__pb2.GetAgentRequest.SerializeToString,
                response_deserializer=Agent__pb2.GetAgentResponse.FromString,
                )
        self.ListAgents = channel.unary_unary(
                '/pb.AgentController/ListAgents',
                request_serializer=Agent__pb2.ListAgentsRequest.SerializeToString,
                response_deserializer=Agent__pb2.ListAgentsResponse.FromString,
                )
        self.UpdateAgent = channel.unary_unary(
                '/pb.AgentController/UpdateAgent',
                request_serializer=Agent__pb2.UpdateAgentRequest.SerializeToString,
                response_deserializer=Agent__pb2.UpdateAgentResponse.FromString,
                )
        self.DeleteAgent = channel.unary_unary(
                '/pb.AgentController/DeleteAgent',
                request_serializer=Agent__pb2.DeleteAgentRequest.SerializeToString,
                response_deserializer=Agent__pb2.DeleteAgentResponse.FromString,
                )


class AgentControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAgents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAgent,
                    request_deserializer=Agent__pb2.CreateAgentRequest.FromString,
                    response_serializer=Agent__pb2.CreateAgentResponse.SerializeToString,
            ),
            'GetAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgent,
                    request_deserializer=Agent__pb2.GetAgentRequest.FromString,
                    response_serializer=Agent__pb2.GetAgentResponse.SerializeToString,
            ),
            'ListAgents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAgents,
                    request_deserializer=Agent__pb2.ListAgentsRequest.FromString,
                    response_serializer=Agent__pb2.ListAgentsResponse.SerializeToString,
            ),
            'UpdateAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAgent,
                    request_deserializer=Agent__pb2.UpdateAgentRequest.FromString,
                    response_serializer=Agent__pb2.UpdateAgentResponse.SerializeToString,
            ),
            'DeleteAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAgent,
                    request_deserializer=Agent__pb2.DeleteAgentRequest.FromString,
                    response_serializer=Agent__pb2.DeleteAgentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.AgentController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgentController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AgentController/CreateAgent',
            Agent__pb2.CreateAgentRequest.SerializeToString,
            Agent__pb2.CreateAgentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AgentController/GetAgent',
            Agent__pb2.GetAgentRequest.SerializeToString,
            Agent__pb2.GetAgentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAgents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AgentController/ListAgents',
            Agent__pb2.ListAgentsRequest.SerializeToString,
            Agent__pb2.ListAgentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AgentController/UpdateAgent',
            Agent__pb2.UpdateAgentRequest.SerializeToString,
            Agent__pb2.UpdateAgentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AgentController/DeleteAgent',
            Agent__pb2.DeleteAgentRequest.SerializeToString,
            Agent__pb2.DeleteAgentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
