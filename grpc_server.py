from concurrent import futures

import grpc

import user_service_pb2
import user_service_pb2_grpc


class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """Реализация методов gRPC-сервиса UserService"""

    def GetUser(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')

        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")


def serve():
    """Функция создает и запускает gRPC-сервер"""

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)

    server.add_insecure_port('[::]:50051')

    server.start()
    print("gRPC сервер запущен на порту 50051...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
