from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import brand
from .parentExtract import extractParent

def HomePageView(request):
    return render(request, 'home.html')

class SearchResultsView(ListView):
    model = brand
    template_name = 'search_results.html'
    
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = brand.objects.filter(name__icontains=query)
        return object_list
    
    def suggest_parent(self):
        query = self.request.GET.get("q")
        suggestedP = extractParent(query)
        return suggestedP

