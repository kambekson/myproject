from django.http import HttpResponse

def homepage(request):
    return HttpResponse("gg world")

def about(request):
    return HttpResponse("about this page")


