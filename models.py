from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

def _str_(self): 
    return self.title

def summary(self):
    return self.body[1:100]
    #100번째 인덱스까지 잘라주는 것이다(python slicing)
