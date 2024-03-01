from django.shortcuts import render
from .models import Invoice

# Create your views here.
def check_invoice(request, code):
    invoice = Invoice.objects.get(invoice_check_code = code)
    context = {
        "invoice" : invoice
    }
    return render(request, "invoice/index.html", context=context)