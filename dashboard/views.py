import datetime
from select import select

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, FormView

from .forms import UserUpdateForm, ProductUpdateForm, AddProductForm
from bloc.models import Order, User, Statistics, Product
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            print(self.request.user.status)
            return HttpResponseRedirect(reverse_lazy('index'))
        else:

            context = super().get_context_data(**kwargs)
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

            context['userdate'] = User.objects.raw('''select 1 id, date(u.date_joined), count(u)
    from account_user as u
    group by date(u.date_joined)''')

            return render(request, 'dashboard/index.html', context)


class WidgetsView(TemplateView):
    template_name = 'dashboard/template/widgets.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif  self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))
        context = super().get_context_data(**kwargs)
        context['pending'] = Order.objects.filter(status='pending')
        context['delivering'] = Order.objects.filter(status='delivering')
        return render(request, 'dashboard/template/widgets.html', context)


def orderUserView(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.status == 'false':
        return HttpResponseRedirect(reverse_lazy('index'))
    order = Order.objects.get(id=id)
    res = {
        "post": order
    }
    return render(request, 'dashboard/template/orderuser.html', res)


class ClubChartView(TemplateView):
    template_name = 'dashboard/template/charts.html'


    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            context = super().get_context_data(**kwargs)
            context['qs'] = Statistics.objects.all()
            return render(request, 'dashboard/template/charts.html', context)


def deliveringView(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.status == 'false':
        return HttpResponseRedirect(reverse_lazy('index'))
    obj = Order.objects.filter(id=id).first()
    obj.status = 'delivering'
    obj.save()
    return HttpResponseRedirect(reverse_lazy('widgets'))


def completedView(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.status == 'false':
        return HttpResponseRedirect(reverse_lazy('index'))
    obj = Order.objects.filter(id=id).first()
    obj.status = 'completed'
    obj.save()
    return HttpResponseRedirect(reverse_lazy('widgets'))


def notcompletedView(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.status == 'True':
        return HttpResponseRedirect(reverse_lazy('index'))
    obj = Order.objects.filter(id=id).first()
    obj.status = 'notcompleted'
    obj.save()
    return HttpResponseRedirect(reverse_lazy('widgets'))


class TablesView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))

        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        return render(request, 'dashboard/template/tables.html', context)


class UserEditForm(UpdateView):
    # queryset = User.objects.get()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))
        form = UserUpdateForm
        user = User.objects.get(id=self.kwargs['id'])
        content = {'form': form,
                   'user': user}
        return render(request, 'dashboard/template/useredit.html', content)

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST)
        user = User.objects.get(id=self.kwargs['id'])
        user.username = form.data['username']
        user.phone = form.data['phone']
        user.status = form.data['status']
        user.save()
        return HttpResponseRedirect(reverse_lazy('tables'))


class ProductView(TemplateView):

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        return render(request, 'dashboard/template/product.html', context)


class ProductEditView(UpdateView):

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))
        form = ProductEditView

        user = Product.objects.get(id=self.kwargs['id'])
        content = {'form': form,
                   'user': user}
        return render(request, 'dashboard/template/productedit.html', content)

    def post(self, request, *args, **kwargs):
        form = ProductUpdateForm(request.POST)
        user = Product.objects.get(id=self.kwargs['id'])
        user.name = form.data['name']
        user.price = form.data['price']
        user.description = form.data['description']
        user.save()
        return HttpResponseRedirect(reverse_lazy('products'))


class AddProductView(CreateView):
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        elif self.request.user.status == 'false':
            return HttpResponseRedirect(reverse_lazy('index'))
        form = AddProductForm
        context = {'form': form}
        return render(request, 'dashboard/template/addProduct.html', context)

    def post(self, request, *args, **kwargs):
        form = AddProductForm(request.POST)
        print('ssd')
        if form.is_valid():
            print('ssd')
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('products'))
        return render(request, 'dashboard/template/addProduct.html', {'form': form})




