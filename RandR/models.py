from django.db import models

# Create your models here.
class RatingReview(models.Model):
    s_reg=models.IntegerField()
    c_name=models.CharField(max_length=100)
    s_ratings=models.IntegerField()
    s_reviews=models.TextField()