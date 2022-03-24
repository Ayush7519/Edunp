from django.contrib import admin
from .models import CATEGORY,SUBJECT,UNIT,SUB_TOPICS


# MODELS REGISTRATION FOR CATEGORY IN THE ADMIN PANNEL:
class CATEGORYADMIN(admin.ModelAdmin):
    list_display=['id','Name']
admin.site.register(CATEGORY,CATEGORYADMIN)


# MODELS REGISTRATION FRO SUBJECT IN THE ADMIN PANNEL:
class SUBJECTADMIN(admin.ModelAdmin):
    list_display=['id','Name','Subject_Code','Category']
admin.site.register(SUBJECT,SUBJECTADMIN)


# MODELS REGISTRATION FRO UNIT IN THE ADMIN PANNEL:
class UNITADMIN(admin.ModelAdmin):
    list_display=['id','Category','Subject','Name']
admin.site.register(UNIT,UNITADMIN)


# MODELS REGISTRATION FRO SUB-TOPICS IN THE ADMIN PANNEL:
class SUB_TOPICSADMIN(admin.ModelAdmin):
    list_display=['id','Category','Subject','Unit','Topic_Name']
admin.site.register(SUB_TOPICS,SUB_TOPICSADMIN)