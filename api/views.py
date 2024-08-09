from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from api import serializers, models
from rest_framework.response import Response


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
        responses=serializers.NewsSerializer()
    )
    def get(self, request):
        news = models.New.objects.all().order_by('-date')
        serializer = serializers.NewsSerializer(news, many=True)
        return Response(serializer.data)


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
        responses=serializers.ManagementsSerializer()
    )
    def get(self, request):
        managements = models.Management.objects.all()
        serializer = serializers.ManagementsSerializer(managements, many=True)
        return Response(serializer.data)


class ManagementAPIView(APIView):

    @extend_schema(
        summary="Management by id",
        request=None,
        responses=serializers.ManagementSerializer(),
        operation_id='retrieve_management'
    )
    def get(self, request, management_id: int):
        management = get_object_or_404(models.Management, id=management_id)
        serializer = serializers.ManagementSerializer(management)
        return Response(serializer.data)


class EmployeesAPIView(APIView):

    @extend_schema(
        summary="Employees",
        request=None,
        responses=serializers.EmployeesSerializer()
    )
    def get(self, request):
        employees = models.Employee.objects.all()
        serializer = serializers.EmployeesSerializer(employees, many=True)
        return Response(serializer.data)


