from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def chat(request):
    if request.method == "GET":
        return render(request, 'nlp/nlp.html')
    if request.method == 'POST':
        text = request.POST['input']
        return render(request, 'nlp/nlp.html', locals())
