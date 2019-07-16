from django.urls import path,include
from .views import add_post,showpost

urlpatterns = [

    path('add_post/', add_post),
    path('show_post/',showpost)
]
