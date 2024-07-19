from django.db import models
import os 
import uuid

# Create your models here.

def unique_file_path(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    
    # Create a unique identifier (shortened)
    unique_id = str(uuid.uuid4().int)[:6]  
    # Take the first 6 characters of the UUID integer representation

    # Create a unique identifier (shortened)
    unique_id = str(uuid.uuid4().int)[:6]  
    # Take the first 6 characters of the UUID integer representation
    
    # Create the unique filename
    unique_filename = f"{unique_id}.{ext}"
    
    return os.path.join('images/', unique_filename)

class Image(models.Model):
    # photo = models.ImageField(upload_to="images")
    photo = models.ImageField(upload_to=unique_file_path)
    date = models.DateTimeField(auto_now_add=True)