from rest_framework.pagination import LimitOffsetPagination, CursorPagination


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