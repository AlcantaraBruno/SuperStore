from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class dos produtos
class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #lembrar modificar o tipo do price
    price = models.CharField(max_length = 11)
    photo = models.ImageField(upload_to='photostore')
    #desafio
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #criar um id automaticamente
    def __str__ (self):
        return str(self.id)

    #renomear a tabela como vai ser no banco
    class Meta:
        db_table = 'Produto'