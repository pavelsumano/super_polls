from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


from django.shortcuts import render
import json
from django.conf import settings
import os

import requests


PROJECT_DIR=os.path.dirname(__file__)
settings.STATIC_ROOT= os.path.join(PROJECT_DIR,'static/')

def calculadora(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', ''))
        num2 = float(request.POST.get('num2', ''))
        operacion = request.POST.get('operacion', '')

        if operacion == 'suma':
            resultado = num1 + num2
            option=' + '
        elif operacion == 'resta':
            resultado = num1 - num2
            option=' - '
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
            option = ' * '
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
                option =' / '
            else:
                resultado = 'Error: División por cero'
        else:
            resultado = 'Operación no válida'

        return render(request, 'polls/calculadora.html', {'resultado': resultado, 'n1': num1, 'n2':num2, 'operador': option})

    return render(request, 'polls/calculadora.html')


def mostrar_datos(request):
    # URL de la API
    api_url = 'https://api.chucknorris.io/jokes/random'

    # Realizar solicitud a la API
    response = requests.get(api_url)
    data = []
    if response.status_code == 200:
        data = response.json()
        print(data)

    return render(request, 'polls/mostrar_datos.html', {'data': data})

def rickymorty(request):
    # URL de la API
    api_url = 'https://rickandmortyapi.com/api/character/5'

    # Realizar solicitud a la API
    response = requests.get(api_url)
    data = []
    if response.status_code == 200:
        data = response.json()
        print(data)

    return render(request, 'polls/testapirick.html', {'data': data})

def rick_morty(request):
    data = []
    resultado = False
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', ''))
        # URL de la API
        api_url = 'https://rickandmortyapi.com/api/character/' + str(num1)
        print(api_url)

        # Realizar solicitud a la API
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            resultado = True

    return render(request, 'polls/rickandmorty.html', { 'data': data, 'resultado': resultado })

# def mostrar_datos(request):
#    json_file_path = os.path.join(settings.STATIC_ROOT, 'datos.json')
#    with open(json_file_path, 'r') as file:
#        data = json.load(file)
#
#    return render(request, 'polls/mostrar_datos.html', {'data': data})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions
        (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
