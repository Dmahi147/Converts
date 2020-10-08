from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def model_form_upload(request):

    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Redirect to the document list after POST
            return redirect('/pdf')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    return render(request, 'app/file_upload.html', {'form': form, 'file': True, 'documents': documents})
