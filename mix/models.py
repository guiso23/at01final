from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)  
    detalhes = models.TextField()            
    image = models.ImageField(upload_to='produtos/') 
    def _str_(self):
        return self.nome