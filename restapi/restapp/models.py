from django.db import models
class Task(models.Model):
    task_name=models.CharField(max_length=250)
    task_desc=models.TextField()
    completed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images',default="image/None/image.jpg")

# Create your models here.
