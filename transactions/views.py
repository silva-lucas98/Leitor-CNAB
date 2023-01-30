from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from transactions.handle_uploaded_file import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(request)

    else:
        form = UploadFileForm()
    return render(request, 'form.html', {'form': form})
