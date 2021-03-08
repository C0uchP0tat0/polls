from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Poll, Question, Answer

class HomePage(ListView):
    template_name = 'home.html'
    context_object_name = 'polls_list'

    def get_queryset(self):
        return Poll.objects.all()

class DetalePage(DetailView):
    model = Question
    template_name = 'detail.html'