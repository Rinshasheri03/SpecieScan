from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Research_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone= models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()

class User_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()

class Findings_table(models.Model):
    RESEARCHER = models.ForeignKey(Research_table, on_delete=models.CASCADE)
    image= models.FileField()
    findings=models.TextField(max_length=50000)
    name=models.CharField(max_length=100)

class Chat(models.Model):
    FROMID= models.ForeignKey(login_table,on_delete=models.CASCADE,related_name="Fromid")
    TOID= models.ForeignKey(login_table,on_delete=models.CASCADE,related_name="Toid")
    message=models.CharField(max_length=100)
    date=models.DateField()


class Complaint_table(models.Model):
    USER = models.ForeignKey(User_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.CharField(max_length=100)

class Feedback_table(models.Model):
    USER = models.ForeignKey(User_table, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    date = models.DateField()
    rating= models.FloatField()

class Bdetails_table(models.Model):

    Image = models.FileField()
    Common_Name = models.CharField(max_length=100)
    Scientific_Name = models.CharField(max_length=100)
    Kingdom = models.CharField(max_length=100)
    Phylum = models.CharField(max_length=100)
    Class = models.CharField(max_length=100)
    Order = models.CharField(max_length=100)
    Family = models.CharField(max_length=100)
    Genus = models.CharField(max_length=100)
    Species = models.CharField(max_length=100)
    LifeCycle = models.CharField(max_length=10000)
