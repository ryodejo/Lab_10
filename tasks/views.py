from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать в Django!")