from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='jobs')
    title=models.CharField(max_length=255)
    description=models.TextField()
    company_name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    salary=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title