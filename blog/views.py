from django.shortcuts import render
from blog.models import Blog
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "text", "preview")
    success_url = reverse_lazy("blog:blog_list")


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "text", "preview")
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")