from django.shortcuts import render
from pytube import *

# Create your views here.
def youtube(request):
    if request.method =='POST':
        link   = request.POST['link']
        video = YouTube(link)

        stream = video.streams.get_highest_resolution()

        stream.download()

        return render(request,'templates/index.html')


    return render(request, 'templates/index.html')
