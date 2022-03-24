from django.shortcuts import render
from .models import CATEGORY,SUBJECT,UNIT,SUB_TOPICS
from .serializers import CATEGORY_SERIALIZER,SUBJECT_SERIALIZER,UNIT_SERIALIZER,SUB_TOPICS_SERIALIZER
from rest_framework.viewsets import ModelViewSet


# CURD FOR CATEGORY MODULES:
class CATEGORY_CURD(ModelViewSet):
    queryset=CATEGORY.objects.all()
    serializer_class=CATEGORY_SERIALIZER


# CURD FOR SUBJECT MODULES:
class SUBJECT_CURD(ModelViewSet):
    queryset=SUBJECT.objects.all()
    serializer_class=SUBJECT_SERIALIZER


# CURD FOR UNIT MODULES:
class UNIT_CURD(ModelViewSet):
    queryset=UNIT.objects.all()
    serializer_class=UNIT_SERIALIZER


# CURD FOR CATEGORY MODULES:
class SUB_TOPICS_CURD(ModelViewSet):
    queryset=SUB_TOPICS.objects.all()
    serializer_class=SUB_TOPICS_SERIALIZER


