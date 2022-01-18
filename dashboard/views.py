from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club
from bloc.models import Order
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


class WidgetsView(TemplateView):
    template_name = 'dashboard/template/widgets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending'] = Order.objects.filter(status='pending')
        context['delivering'] = Order.objects.filter(status='delivering')
        return context


def orderUserView(request, id):
    order = Order.objects.get(id=id)
    res = {
        "post": order
    }
    return render(request, 'dashboard/template/orderuser.html', res)



class ClubChartView(TemplateView):
    template_name = 'dashboard/template/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        return context
