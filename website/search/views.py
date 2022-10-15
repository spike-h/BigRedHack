from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import brand

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = brand
    template_name = 'search_results.html'
    
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = brand.objects.filter(name__icontains=query)
        return object_list