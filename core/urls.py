from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('messages/', views.MessageAPIView.as_view()),

    path('news/', views.NewsAPIView.as_view()),
    path('news/<int:new_id>/', views.NewAPIView.as_view()),

    path('managements/', views.ManagementsAPIView.as_view()),

    path('employees/', views.EmployeesAPIView.as_view()),
    path('employees/<int:employee_id>/', views.EmployeeAPIView.as_view()),
]
