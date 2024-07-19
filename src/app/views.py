from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image

# Create your views here.

def home(request):
    form = ImageForm()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()

    img = Image.objects.all
    context = {
        'form':form,
        'img':img,
    }
    return render(request, 'index.html',context)