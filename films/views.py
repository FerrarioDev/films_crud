from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film

class FilmBaseView(View):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films:all')

class FilmListView(FilmBaseView, ListView):
    model = Film
    template_name = 'films/film_list.html'
    context_object_name = 'film_list'
    def get_queryset(self):
        return self.model.objects.all()

class FilmDetailView(FilmBaseView, DetailView):
    model = Film
    template_name = 'films/film_detail.html'
    context_object_name = 'film'

    
class FilmCreateView(FilmBaseView, CreateView):
    model = Film
    template_name = 'films/film_form.html'
    fields = '__all__'

class FilmDeleteView(FilmBaseView, DeleteView):
    model = Film
    template_name = 'films/film_confirm_delete.html.html'
    success_url = reverse_lazy('films:all')

class FilmUpdateView(FilmBaseView, UpdateView):
    model = Film
    template_name = 'films/film_update.html'
    fields = '__all__'
    success_url = reverse_lazy('films:all')