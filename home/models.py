from django.db import models

# Create your models here.
class courses(models.Model):
    c_name= models.CharField(max_length=100)
    c_tfees=models.IntegerField()
    c_eligibility=models.IntegerField()
    c_description=models.TextField()
    c_rstream=models.CharField(max_length=100)
    c_type=models.CharField(max_length=100)
    c_img=models.ImageField(upload_to='media/static/courses_pic')
    c_code=models.IntegerField()

class userinput(models.Model):
    percentage=models.IntegerField()
    stream=models.CharField(max_length=100)
    budget=models.IntegerField()