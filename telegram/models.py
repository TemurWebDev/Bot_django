from django.db import models
#from core.models import TimeStampedModel

class Tguser(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100,null=True)
    language = models.CharField(max_length=10,null=True)
    phon_number = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.first_name)


class Ariza(models.Model):
    body = models.TextField()

    def __str__(self):
        return str(self.body)


