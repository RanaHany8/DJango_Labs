from django.db import models
from django.core.exceptions import ValidationError


def validate_name_length(value):
    if len(value) < 3:
        raise ValidationError("Name must be at least 3 characters long.")


class Trainee(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=100, 
        validators=[validate_name_length]
    )

    def __str__(self):
        return f"{self.id} - {self.name}"