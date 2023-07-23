from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Lesson
from course.serializers import CourseSerializer, LessonSerializer
from course.permissions import IsModerator, IsOwner

class CourseViewSet(viewsets.ModelViewSet):
    """Представление курса, которое включает в себя механизм CRUD"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_staff:
            return Course.objects.all()
        else:
            return Course.objects.filter(user=user)

    # def post(self, request, *args, **kwargs):
    #     data = request.POST.copy()
    #     print(data)
    #     data['user'] = request.user.id
    #     return self.create(data, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonListView(generics.ListAPIView):
    """Представление списка уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_staff:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(user=user)


class LessonDetailAPIView(generics.RetrieveAPIView):
    """Представление для одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     data = request.POST.copy()
    #     print(data)
    #     data['user'] = request.user.id
    #     return self.create(data, *args, **kwargs)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]