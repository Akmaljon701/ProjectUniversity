from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from api import serializers, models
from rest_framework.response import Response
from utils.pagination import paginate, PaginationResponseSerializer, paginate_dynamic, \
    PaginationDynamicResponseSerializer


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
        responses=PaginationDynamicResponseSerializer(child_serializer_class=serializers.NewsSerializer),
        parameters=[
            OpenApiParameter(name='page', required=True, type=OpenApiTypes.INT),
            OpenApiParameter(name='limit', required=True, type=OpenApiTypes.INT),
        ]
    )
    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        news = models.New.objects.all().order_by('-date')
        return paginate_dynamic(news, serializers.NewsSerializer, request, page, limit)


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
        responses=PaginationDynamicResponseSerializer(child_serializer_class=serializers.ManagementsSerializer),
        parameters=[
            OpenApiParameter(name='page', required=True, type=OpenApiTypes.INT),
            OpenApiParameter(name='limit', required=True, type=OpenApiTypes.INT),
        ]
    )
    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        managements = models.Management.objects.all()
        return paginate_dynamic(managements, serializers.ManagementsSerializer, request, page, limit)


class EmployeesAPIView(APIView):

    @extend_schema(
        summary="Employees",
        request=None,
        responses=PaginationDynamicResponseSerializer(child_serializer_class=serializers.EmployeesSerializer),
        parameters=[
            OpenApiParameter(name='status', required=True, type=OpenApiTypes.STR,
                             enum=[
                                 'XODIM',
                                 'TALABA',
                                 'PROFESSOR'
                             ]),
            OpenApiParameter(name='page', required=True, type=OpenApiTypes.INT),
            OpenApiParameter(name='limit', required=True, type=OpenApiTypes.INT),
        ]
    )
    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        status = request.query_params.get('status')
        employees = models.Employee.objects.filter(status=status).all()
        return paginate_dynamic(employees, serializers.EmployeesSerializer, request, page, limit)


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
