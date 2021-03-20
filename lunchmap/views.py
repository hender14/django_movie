from django.urls import reverse_lazy
from django.views import generic
from .models import Category

class IndexView(generic.ListView):
    model = Category

class DetailView(generic.DetailView):
    model = Category

class CreateView(generic.edit.CreateView):
    model = Category
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Category
    fields = '__all__'

class DeleteView(generic.edit.DeleteView):
    model = Category
    success_url = reverse_lazy('lunchmap:index')