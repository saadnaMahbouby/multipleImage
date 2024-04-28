from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import UploadImage

def upload_photo(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Traitement pour plusieurs fichiers
            files = request.FILES.getlist('image')
            for file in files:
                upload_image = UploadImage(image=file, title=form.cleaned_data['title'], description=form.cleaned_data['description'])
                upload_image.save()
            return redirect('photo_list')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})

def photo_list(request):
    photos = UploadImage.objects.all()
    return render(request, 'show_files.html', {'photos': photos})
def delete_all_photos(request):
    UploadImage.objects.all().delete()
    return redirect('photo_list')