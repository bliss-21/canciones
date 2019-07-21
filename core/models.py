from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    nombre = models.CharField(max_length=30)
    letra = models.TextField()
    
    #vecinas
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#biblia-----------------------

class Testament(models.Model):
    
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testament'

    def __str__(self):
        return self.name

class Book(models.Model):
    
    testament = models.ForeignKey('Testament', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'
    
    def __str__(self):
        return self.name

class Verse(models.Model):
    
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    verse = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verse'

    def __str__(self):
        return str(self.book)+' : '+str(self.chapter)+' - '+str(self.verse)

