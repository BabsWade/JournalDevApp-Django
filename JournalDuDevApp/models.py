from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    def __str__(self):
        return self.titre
