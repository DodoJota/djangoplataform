"""
URL configuration for djangoapps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tutorpage import views
from tutorpage.views import user_login, salvar_notas, get_notas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', user_login, name='login'),
    path('aulas/', views.aulas, name='aulas'),
    path('materiais/', views.materiais, name='materiais'),
    path('praticar/', views.praticar, name='praticar'),
    path('salvar-notas/', salvar_notas, name='salvar-notas'),
    path("get-notas/", get_notas, name="get_notas"),
    path('flashcards/', views.flashcards_view, name='flashcards'),
    path('speech/', views.speech, name='speech'),
    path('gramatica/', views.gramatica, name='gramatica'),
]
