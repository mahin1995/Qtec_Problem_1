from pydoc import describe
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class keyword(models.Model):
    title=models.CharField(max_length=255, null=True,db_index=True,)
    describe=models.TextField()
    user_name=models.CharField(max_length=20,blank=True,null=True)
    app_date_tiem=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.title)
    
