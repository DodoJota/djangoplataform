from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NotaAula

# Create your views here.

def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Autenticação do usuário (Django usa 'username', não 'email' por padrão)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  # Redireciona para a home após login
        else:
            messages.error(request, "E-mail ou senha inválidos")

    return render(request, "login.html")

@csrf_exempt
def salvar_notas(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            aula = data.get("aula")
            notas = data.get("notas", "")

            if not aula:
                return JsonResponse({"erro": "Aula não especificada"}, status=400)

            nota_obj, created = NotaAula.objects.update_or_create(
                aula=aula,
                defaults={'notas': notas}
            )

            return JsonResponse({"mensagem": "Notas salvas com sucesso!", "criado": created})
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=500)

    return JsonResponse({"erro": "Método não permitido"}, status=405)


def get_notas(request):
    aula = request.GET.get("aula")
    if not aula:
        return JsonResponse({"erro": "Aula não especificada"}, status=400)

    nota_obj = NotaAula.objects.filter(aula=aula).first()
    return JsonResponse({"notas": nota_obj.notas if nota_obj else ""})

def aulas(request):
    return render(request, 'aulas.html') 

def materiais(request):
    return render(request, 'materiais.html')

def praticar(request):
    return render(request, 'praticar.html') 

"""

def register(request):


def lives(request):

"""