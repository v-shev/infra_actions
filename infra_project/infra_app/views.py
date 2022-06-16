from django.http import HttpResponse


def index(request):
    return HttpResponse("I am do it!")


def second_page(request):
    return HttpResponse("А это вторая страница!")
