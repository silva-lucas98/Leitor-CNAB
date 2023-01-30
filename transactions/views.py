from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from transactions.handle_uploaded_file import handle_uploaded_file
from .models import Transaction
from django.db.models import Sum
import ipdb


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(request)
            return HttpResponseRedirect('list/')

    else:
        form = UploadFileForm()
    return render(request, 'form.html', {'form': form})


def list_data_stores(request):
    if request.method == "GET":
        stores = Transaction.objects.all()

        list_stores = []
        for store in stores:
            if store.store not in list_stores:
                list_stores.append(store.store)

        data_stores = []
        for name in list_stores:
            store = Transaction.objects.filter(store=name)[0]
            value = Transaction.objects.filter(store=name).aggregate(total_value=Sum("value"))

            # ipdb.set_trace()
            store.total = round(int(value["total_value"]) / 100, 2)
            if store.type == "2" or store.type == "3" or store.type == "9":
                store.total = f"-{store.total}"
            
            data_stores.append(store)

        return render(request, "list.html", {"data_stores": data_stores})
