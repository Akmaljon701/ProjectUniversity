from typing import Optional

from drf_spectacular.utils import extend_schema_field
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField
from api import models


class MessageCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = [
            'fio',
            'phone',
            'message',
        ]


class NewsSerializer(ModelSerializer):
    description = SerializerMethodField()

    class Meta:
        model = models.New
        fields = [
            'title',
            'description',
            'photo',
            'date',
        ]

    @extend_schema_field(str)
    def get_description(self, obj) -> Optional[str]:
        description = obj.description
        if len(description) > 30:
            return description[:30] + '...'
        return description


class NewSerializer(ModelSerializer):

    class Meta:
        model = models.New
        fields = [
            'title',
            'description',
            'photo',
            'date',
        ]


class ManagementsSerializer(ModelSerializer):
    description = SerializerMethodField()

    class Meta:
        model = models.New
        fields = [
            'title',
            'description',
            'photo',
        ]

    @extend_schema_field(str)
    def get_description(self, obj) -> Optional[str]:
        description = obj.description
        if len(description) > 30:
            return description[:30] + '...'
        return description


class ManagementSerializer(ModelSerializer):

    class Meta:
        model = models.Management
        fields = [
            'title',
            'description',
            'photo',
        ]


class EmployeesSerializer(ModelSerializer):

    class Meta:
        model = models.Employee
        fields = [
            'fio',
            'position',
            'status',
            'photo',
        ]
