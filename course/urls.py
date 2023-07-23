from django.urls import path
from rest_framework.routers import DefaultRouter
from course.views import *
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/detail/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDeleteAPIView.as_view(), name='lesson_delete')
] + router.urls