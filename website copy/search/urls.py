from django.urls import path
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    #path("", HomePageView.as_view(), name="home"),
    path('', HomePageView, name='home'),
    # path('upload/', image_upload_view, name='upload'),
]