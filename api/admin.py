from django.contrib import admin
from django.contrib.admin import ModelAdmin
from api import models
from django.contrib.auth.models import Group, User

admin.site.site_title = "University Admin"
admin.site.site_header = "University"
admin.site.index_title = "University Admin"
admin.site.site_brand = "University"
admin.site.welcome_sign = "University"
admin.site.copyright = "University"

admin.site.unregister(Group)
admin.site.unregister(User)


class NewsAdmin(ModelAdmin):
    list_display = ['id', 'title', 'date',]
    list_display_links = ['title', 'date',]
    search_fields = ['title',]


admin.site.register(models.New, NewsAdmin)


class ManagementsAdmin(ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ['title',]
    search_fields = ['title',]


admin.site.register(models.Management, ManagementsAdmin)


class EmployeesAdmin(ModelAdmin):
    list_display = ['id', 'fio', 'position', 'status',]
    list_display_links = ['fio', 'position', 'status',]
    search_fields = ['fio',]
    list_filter = ['status',]


admin.site.register(models.Employee, EmployeesAdmin)


class MessagesAdmin(ModelAdmin):
    list_display = ['id', 'fio', 'phone', 'message', 'status',]
    list_display_links = ['fio', 'phone', 'message',]
    search_fields = ['fio',]
    list_filter = ['status',]
    list_editable = ['status']


admin.site.register(models.Message, MessagesAdmin)
