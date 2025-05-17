import grpc

from core.grpc.course_service_pb2_grpc import CourseServiceStub
from core.grpc.course_service_pb2 import GetCourseRequest

channel = grpc.insecure_channel("localhost:50051")
stub = CourseServiceStub(channel)

response = stub.GetCourse(GetCourseRequest(course_id="test"))
print(response)
