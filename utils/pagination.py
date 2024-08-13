from rest_framework.pagination import LimitOffsetPagination, CursorPagination
from rest_framework import serializers


class CustomOffSetPagination(LimitOffsetPagination):
    default_limit = 25
    max_limit = 100


def paginate(instances, serializator, request, **kwargs):
    paginator = CustomOffSetPagination()
    paginated_order = paginator.paginate_queryset(instances, request)

    serializer = serializator(paginated_order, many=True, **kwargs)

    return paginator.get_paginated_response(serializer.data)


class CustomCursorPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100
    ordering = 'id'


def cursor_paginate(instances, serializator, request, **kwargs):
    paginator = CustomCursorPagination()
    paginated_order = paginator.paginate_queryset(instances, request)

    serializer = serializator(paginated_order, many=True, **kwargs)

    return paginator.get_paginated_response(serializer.data)


class PaginationResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.URLField(required=False, allow_null=True)
    previous = serializers.URLField(required=False, allow_null=True)
    results = serializers.ListSerializer(child=serializers.Serializer())

    def __init__(self, *args, **kwargs):
        self.child_serializer_class = kwargs.pop('child_serializer_class', serializers.Serializer)
        super().__init__(*args, **kwargs)
        self.fields['results'].child = self.child_serializer_class()
