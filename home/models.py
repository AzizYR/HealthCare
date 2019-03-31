from django.db import models

class db(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.name)


class dbadmin(models.Model):
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.name)
