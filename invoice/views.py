from django.shortcuts import render
from .models import Invoice, FileTool

# Create your views here.
def check_invoice(request, code):
    invoice = Invoice.objects.get(invoice_check_code = code)
    url = ''
    if invoice.link != '':
        url = invoice.link
    else:
        url = invoice.file.url
    context = {
        "invoice" : invoice,
        "url" : url
    }
    return render(request, "invoice/index.html", context=context)


def tool_list_view(request):
    tool_list = FileTool.objects.all()
    context = {
        "tool_list" : tool_list
    }
    return render(request, "invoice/index2.html", context=context)