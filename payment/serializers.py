from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from course.models import Course, Lesson
from payment.models import Payment
from users.models import User


class PaymentSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    paid_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    paid_lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'