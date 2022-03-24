from dataclasses import fields
from multiprocessing.spawn import import_main_path
from pyexpat import model
from .models import CATEGORY,SUBJECT,UNIT,SUB_TOPICS
from rest_framework.serializers import ModelSerializer


# SERIALIZERS CLASS FRO CATEGORY MODULES:
class CATEGORY_SERIALIZER(ModelSerializer):
    class Meta:
        model=CATEGORY
        fields='__all__'


# SERIALIZERS CLASS FRO SUBJECT MODULES:
class SUBJECT_SERIALIZER(ModelSerializer):
    class Meta:
        model=SUBJECT
        fields='__all__'

    
# SERIALIZERS CLASS FRO UNT MODULES:
class UNIT_SERIALIZER(ModelSerializer):
    class Meta:
        model=UNIT
        fields='__all__'


# SERIALIZERS CLASS FRO SUB-TOPICS MODULES:
class SUB_TOPICS_SERIALIZER(ModelSerializer):
    class Meta:
        model=SUB_TOPICS
        fields='__all__'