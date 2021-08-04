from django.http import HttpResponse
from django.shortcuts import render
from upload_image.models import Image


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'upload_image/index.html', locals())
    if request.method == 'POST':
        username = request.session['username']
        afile = request.FILES['myfile']
        Image.objects.create(username=username, myfile=afile)
        # return render(request, 'upload_image/index.html', locals())
        return HttpResponse('上传成功')
