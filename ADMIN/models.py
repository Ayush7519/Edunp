from django.db import models


# MODELS FRO CATEGORY FIELDS:
class CATEGORY(models.Model):
    Name=models.CharField(max_length=100)


# MODELS FOR SUBJECT FIELSD:
class SUBJECT(models.Model):
    Name=models.CharField(max_length=100)
    Subject_Code=models.IntegerField()
    Category=models.ForeignKey(CATEGORY,on_delete=models.CASCADE)


# MODELS FRO UNIT FIELDS:
class UNIT(models.Model):
    Category=models.ForeignKey(CATEGORY,on_delete=models.CASCADE)
    Subject=models.ForeignKey(SUBJECT,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)


# MODELS FRO SUB-TOPICS FIELDS:
class SUB_TOPICS(models.Model):
    Category=models.ForeignKey(CATEGORY,on_delete=models.CASCADE)
    Subject=models.ForeignKey(SUBJECT,on_delete=models.CASCADE)
    Unit=models.ForeignKey(UNIT,on_delete=models.CASCADE)
    Topic_Name=models.CharField(max_length=100)
