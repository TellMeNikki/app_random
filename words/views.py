from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    return HttpResponse("probando random_words")


# login/logout sessions
def login(request, name):
    request.session["name"] = name
    return redirect("/random_words")


def rand_words(request):
    counter = request.session.get("counter")
    # inicializa el contador en cero
    if "counter" not in request.session:
        request.session["counter"] = 0
    # max de intentos
    if request.session["counter"] < 10:
        request.session["counter"] += 1
        word = get_random_string(length=14)
    else:
        word = "Límite de intentos superados"
    context = {"word": word, "counter": counter}
    return render(request, "random_pass.html", context)


def reset(request):
    request.session.flush()
    return redirect("/random_words")


def generate(request):
    context = {
        "word": get_random_string(length=14),
    }
    return render(request, "random_pass.html", context)
