from django.db import models

# Create your models here.


class WorkerMemory(models.Model):
    name = models.CharField(max_length=100)
    last_url = models.URLField()

    def __str__(self):
        return "\n %s : %s" % (self.name, self.last_url)