from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import brand
from .forms import ImageForm
from .logoDetect import predict

'''class HomePageView(TemplateView):
    template_name = 'home.html'''

# def HomePageView(request):
#     return render(request, 'home.html')

class SearchResultsView(ListView):
    model = brand
    template_name = 'search_results.html'
    
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = brand.objects.filter(name__icontains=query)
        return object_list

def HomePageView(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            # print('\n',img_obj,'\n')
            print('\n', predict(img_obj.image.url), '\n')
            query = predict(img_obj.image.url)
            if query:
                object_list = brand.objects.filter(name__icontains=query)
                return render(request, 'search_results.html', {'form': form, 'object_list': object_list})
            form = ImageForm()
            return render(request, 'home.html', {'form': form})
    
    form = ImageForm()
    return render(request, 'home.html', {'form': form})

