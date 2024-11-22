import django
from django.db import models

# Create your models here.

class Cars(models.Model):
    model = models.CharField(max_length=50,null=False)
    brand = models.CharField(max_length=50,null=False)
    year = models.IntegerField(null=False)
    filename = models.CharField(max_length=50,null=False)
    user = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        
        return ' Modelo: ' + self.model + ' Ano: ' + str(self.year) 
    