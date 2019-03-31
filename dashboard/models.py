from django.db import models
import datetime

class events(models.Model):
    name = models.CharField(max_length = 100)
    doc = models.CharField(max_length = 100)
    # date = models.CharField(max_length = 100)
    date = models.DateField()
    med1 = models.CharField(max_length = 100 , default = "" , blank = True)
    med2 = models.CharField(max_length = 100 , default = "" , blank = True)
    med3 = models.CharField(max_length = 100 , default = "" , blank = True)
    med4 = models.CharField(max_length = 100 , default = "" , blank = True)
    med5 = models.CharField(max_length = 100 , default = "" , blank = True)
    med6 = models.CharField(max_length = 100 , default = "" , blank = True)
    med7 = models.CharField(max_length = 100 , default = "" , blank = True)
    med8 = models.CharField(max_length = 100 , default = "" , blank = True)
    med9 = models.CharField(max_length = 100 , default = "" , blank = True)
    med10 = models.CharField(max_length = 100 , default = "" ,blank = True )


    def __str__(self):
        return str(self.name)
