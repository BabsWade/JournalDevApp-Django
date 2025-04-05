from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    fields = ['titre', 'contenu', 'image']

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['titre', 'contenu', 'image']

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['titre', 'contenu', 'image']
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')


