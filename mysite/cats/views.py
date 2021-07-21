from django.forms.models import construct_instance
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaulttags import LoadNode
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Cat, Breed


class CatList(LoginRequiredMixin, ListView):
    model = Cat

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        breed_count = Breed.objects.all().count()

        context['breed_count'] = breed_count

        return context

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedList(LoginRequiredMixin, ListView):
    model = Breed

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')