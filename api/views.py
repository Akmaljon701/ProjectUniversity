from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from api import serializers, models
from rest_framework.response import Response
from utils.pagination import paginate, PaginationResponseSerializer


class MessageAPIView(APIView):

    @extend_schema(
        summary="Create Message",
        request=serializers.MessageCreateSerializer(),
        responses={201: ''}
    )
    def post(self, request):
        serializer = serializers.MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)


class NewsAPIView(APIView):

    @extend_schema(
        summary="News",
        request=None,
        responses=PaginationResponseSerializer(child_serializer_class=serializers.NewsSerializer)
    )
    def get(self, request):
        news = models.New.objects.all().order_by('-date')
        return paginate(news, serializers.NewsSerializer, request)


class NewAPIView(APIView):

    @extend_schema(
        summary="New by id",
        request=None,
        responses=serializers.NewSerializer(),
        operation_id='retrieve_new'
    )
    def get(self, request, new_id: int):
        new = get_object_or_404(models.New, id=new_id)
        serializer = serializers.NewSerializer(new)
        return Response(serializer.data)


class ManagementsAPIView(APIView):

    @extend_schema(
        summary="Managements",
        request=None,
        responses=PaginationResponseSerializer(child_serializer_class=serializers.ManagementsSerializer)
    )
    def get(self, request):
        managements = models.Management.objects.all()
        return paginate(managements, serializers.ManagementsSerializer, request)


class EmployeesAPIView(APIView):

    @extend_schema(
        summary="Employees",
        request=None,
        responses=PaginationResponseSerializer(child_serializer_class=serializers.EmployeesSerializer),
        parameters=[
            OpenApiParameter(name='status', required=True, type=OpenApiTypes.STR,
                             enum=[
                                 'XODIM',
                                 'TALABA',
                                 'PROFESSOR'
                             ]),
        ]
    )
    def get(self, request):
        status = request.query_params.get('status')
        employees = models.Employee.objects.filter(status=status).all()
        return paginate(employees, serializers.EmployeesSerializer, request)


class EmployeeAPIView(APIView):

    @extend_schema(
        summary="Employee by id",
        request=None,
        responses=serializers.EmployeeSerializer(),
        operation_id='retrieve_employee'
    )
    def get(self, request, employee_id: int):
        employee = get_object_or_404(models.Employee, id=employee_id)
        serializer = serializers.EmployeeSerializer(employee)
        return Response(serializer.data)

