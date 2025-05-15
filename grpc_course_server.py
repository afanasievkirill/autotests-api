import grpc
from concurrent import futures

from core.grpc.course_service_pb2_grpc import (
    CourseServiceServicer,
    add_CourseServiceServicer_to_server,
)
from core.grpc.course_service_pb2 import GetCourseResponse


class CourseServiseServiser(CourseServiceServicer):
    def GetCourse(self, request, context):
        print(f"Получили запрос курса с id: {request.course_id}")
        data = {
            "course_id": request.course_id,
            "title": "Автотесты API",
            "description": "Будем изучать написание API автотестов",
        }
        return GetCourseResponse(data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Сервер запущен на порту: 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
