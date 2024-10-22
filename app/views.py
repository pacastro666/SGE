from django.shortcuts import render
from . import metrics


def home(request):
    product_metrics = metrics.get_product_metrics()
    seles_metrics = metrics.get_sales_metrics()
    context = {
        'product_metrics': product_metrics,
        'sales_metrics':seles_metrics,
    }
    return render(request, 'home.html', context)