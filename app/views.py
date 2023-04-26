from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    To=TopicForm()
    d={'To':To}
    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('insert_topic is done')
   
    return render(request,'insert_topic.html',d)