import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import Club
from bloc.models import Order, User
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['pending'] = 0
        context['delivering'] = 0
        context['total'] = 0
        context['online'] = 0
        context['user'] = 0
        context['new_user'] = 0
        for i in Order.objects.all():
            if i.status == 'pending':
                context['pending'] += 1
                context['online'] += 1
            elif i.status == 'delivering':
                context['delivering'] += 1
                context['online'] += 1
            context['total'] += 1
        time = datetime.datetime.now()-datetime.timedelta(10)
        context['new_user'] = User.objects.filter(date_joined__gte=time).count()
        context['user'] = User.objects.all().count()

        return context


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


def deliveringView(request, id):
    obj = Order.objects.filter(id=id).first()
    obj.status = 'delivering'
    obj.save()
    return HttpResponseRedirect(reverse_lazy('widgets'))


def completedView(request, id):
    obj = Order.objects.filter(id=id).first()
    obj.status = 'completed'
    obj.save()
    return HttpResponseRedirect(reverse_lazy('widgets'))

def notcompletedView(request, id):
    obj = Order.objects.filter(id=id).first()
    obj.status = 'notcompleted'
    obj.save()
    return HttpResponseRedirect(reverse_lazy('widgets'))

def tables(request):
    return render(request, 'dashboard/template/tables.html')