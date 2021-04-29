from django.db import models

# Create your models here.

class Calculator(models.Model):
    
    @staticmethod
    def getPercentage(goal, objective):
        percentage= 0
        if goal >= objective:
            percentage = 1
        else:
            percentage = goal /objective
        return percentage