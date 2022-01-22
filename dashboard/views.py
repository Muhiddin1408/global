import datetime

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, FormView
from .models import Club
from .forms import UserUpdateForm
from bloc.models import Order, User, Statistics
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
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
        context['qs'] = Statistics.objects.all()
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


class TablesView(TemplateView):
    template_name = 'dashboard/template/tables.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        return context


class UserEditForm(FormView):
    model = User
    template_name = 'dashboard/template/useredit.html'
    form_class = UserUpdateForm
    # queryset = User.objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.kwargs['id'])
        return context
    # def get_context_data(self, **kwargs):

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('tables'))

        return render(request, 'dashboard/template/tables.html', {'form': form})



    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()
    #     return HttpResponse(self.template_name, self.get_context_data())
    #     form.instance.user = self.request.user
    #     form.save()
    #     return super(UserEditForm, self).form_valid(form)


def EditView(request, id):
        if not request.user.is_authenticated:
            return redirect("/login")
        if request.method == "GET":
            context = super().get_context_data()
            print('dsa')
            context['user'] = User.objects.get(id=request.POST.get("id")).first()
            return context

        if request.method == "POST":
            price = User.objects.filter(id=request.POST.get("id")).first()
            my_file = request.POST.get("username")
            post = request.POST.get("status")
            print(post)
            form = UserUpdateForm
            print(my_file)
            if form.is_valid():
                price.username = request.POST.get("username")
                price.phone = request.POST.get("phone")
                price.status = request.POST.get("status")
                price.save()
            # if not price:
            #     return JsonResponse({"price": "Not found"})

                return HttpResponseRedirect(reverse_lazy("tables"))
        price = User.objects.filter(id=request.GET.get("id")).first()
        return render(request, template_name="dashboard/template/useredit.html", context={"price": price})
    #
    # def post(self, request, *args, **kwargs):
    #     form = UserUpdateForm(request.POST)
    #     if form.is_valid():
    #         post = form.save()
    #         post.save()
    #         return HttpResponseRedirect(reverse_lazy('tebles'))











# class UserEdit(UpdateView):
    # def get(self):
    # if request.method == 'POST':
    #     form = UserUpdateView(request.POST, instance=request.user)
    #
    #     if form.is_valid:
    #         form.save()
    #         return HttpResponseRedirect(reverse_lazy('tables'))
    # else:
    #     form = UserUpdateView(instance=request.user)
    #
    #     args = {
    #         'form': form,
    #
    #     }
    #     return render(request, '.html', args)

