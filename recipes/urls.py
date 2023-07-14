from django.contrib import admin
from django.urls import path

from recipes.views import contato, my_view, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre', sobre),
    path('contato', contato),
    path('', my_view)
]
