from django.db import models

# Create your models here.
# TestCommit

class Cliente (models.Model):
    nome= models.CharField('nome', max_length=100)
    email=models.CharField('email', max_length=100)

class Parceirias (models.Model):
    nome= models.CharField('nome', max_length=100)
    email=models.CharField('email', max_length=100)
    proposta= models.CharField('proposta', max_length=100)

class duvidas (models.Model):
    nome= models.CharField('nome', max_length=100)
    email=models.CharField('email', max_length=100)
    duvidas= models.CharField('duvidas', max_length=100)