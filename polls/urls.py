from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('mostrar-datos/', views.mostrar_datos, name='mostrar_datos'),
    path('rickymorty/', views.rickymorty, name='testapirick'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('rick_morty/', views.rick_morty, name='rickandmorty'),
]
