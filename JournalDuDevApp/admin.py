from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article
from ckeditor.widgets import CKEditorWidget
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    contenu = forms.CharField(widget=CKEditorWidget())  # Ajout de CKEditor au champ 'contenu'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)
