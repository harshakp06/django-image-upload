from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from .utils import generate_presigned_url

# Create your views here.

def home(request):
    form = ImageForm()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        
        if form.is_valid():
            image_instance = form.save()
            return redirect('home')
    else:
        form = ImageForm()

    images = Image.objects.all()

    presigned_urls = []

    for image in images:
        presigned_url = generate_presigned_url(image.photo.name)  # Use the image name to get the URL
        presigned_urls.append(presigned_url)
    
    context = {
        'form':form,
        'urls':presigned_urls,
    }
    return render(request, 'index.html',context)