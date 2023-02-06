# app1/models.py
from django.db import models

class App1Model(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# app2/models.py
from django.db import models

class App2Model(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
