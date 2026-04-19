from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150) 
    description = models.TextField(null=True, blank=True) 
    duration = models.IntegerField(default=0) 

    def __str__(self):
        return self.title 