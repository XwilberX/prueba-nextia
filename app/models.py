from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserModel(BaseModel):
    fullname = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BienesModel(BaseModel):
    article = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

