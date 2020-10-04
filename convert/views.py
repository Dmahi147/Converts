from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:home')
    else:
        form = DocumentForm()
    return render(request, 'app/file_upload.html', {
        'form': form,
        'file': True
    })
