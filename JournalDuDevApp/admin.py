from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)
