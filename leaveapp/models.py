from django.db import models
class apply(models.Model):
    Name = models.CharField(max_length=55, blank=False)
    Department = models.CharField(max_length=25, blank=False)
    Rollno = models.CharField(max_length=8, blank=False, unique=True)
    Reason = models.CharField(max_length=150, blank=False)
    FromDate = models.DateTimeField(blank=False)
    ToDate = models.DateTimeField(blank=False)
    email = models.EmailField(max_length=50, blank=False,)
