from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.views.generic import ListView, CreateView
from .models import Product, User, Order, OrderDetail, Cart
from .forms import UserRegisterForm, ContactFrom, OrderCreateForm
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

# login user
# class CustomLoginView(LoginView):
#     template_name = 'pages/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
#     user = authenticate(username='john', password='secret')
#
#     def get_success_url(self):
#         return reverse_lazy('index')
#

class OrderCreateView(CreateView):
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        form = OrderCreateForm
        content = {'form': form}
        return render(request, 'pages/address.html', content)

    def post(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        form = OrderCreateForm(request.POST)
        print(request.user.id)
        print(request.user.id)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                address=form.data['address'],
            )
            for item in carts:
                OrderDetail.objects.create(
                    product=item.product,
                    quantity=item.quantity,
                    order=order
                )
            Cart.objects.filter(user=request.user).delete()
            return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'pages/address.html', {'form': form})


class Register(CreateView):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm
        content = {'form': form}
        return render(request, 'pages/register.html', content)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        print(request.POST['phone'])
        if form.is_valid(request.POST, raise_exception=True):
            print('qwe')
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('register'))
        else:
            messages.add_message(request, messages.INFO, 'User already exists. Please provide another username')
            return HttpResponseRedirect(reverse_lazy('register'))


class CartView(ListView):
    model = Cart
    template_name = 'pages/cart.html'
    context_object_name = 'carts'



#
#
# class JihozlarView(ListView):
#     model = Product
#     if Product.type == 'ACCESSORIES':
#         template_name = 'pages/jihozlar.html'
#         context_object_name = 'jihozlars'
#         paginate_by = 9
# #
# #
# class PostView(ListView):
#     model = Product
#     if Product.type == 'PHONES':
#         template_name = 'pages/hendrerit.html'
#         context_object_name = 'posts'
#         paginate_by = 9
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

class ProductView(ListView):
    model = Product

    template_name = 'pages/hendrerit.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        # print(self.request)
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

#
def get_post(request, id):
    post = Product.objects.get(id=id)
    res = {
        "post": post
    }
    return render(request, 'pages/post.html', res)


def get_category(request, id):
    products = Product.objects.get(category__id=id)
    res = {
        "products": products
    }
    return render(request, 'pages/category.html', res)


# def get_jihoz(request, id):
#
#     jihoz = Jihozlar.objects.get(id=id)
#     res = {
#         "jihoz": jihoz
#     }
#     return render(request, 'pages/cart.html', res)

#
# def post_jihoz_buyurtma(request, id):
#     print(request.method)
#     if request.method == 'POST':
#         jihoz = Jihozlar.objects.get(id=id)
#         form = BuyForm(request.POST)
#         if not form.is_valid():
#             print(form.cleaned_data['number'], form.cleaned_data['name'])
#             print(form.cleaned_data['phone_number'])
#             post = form.save()
#             post.save()
#             # Buy.objects.create(
#             #     title=jihoz.title,
#             #     price=jihoz.price,
#             #
#             # )
#             return HttpResponseRedirect(reverse_lazy('jihoz-buyurtma'))
#         return render(request, 'pages/cart.html', {'form': form})
#
#
# class PostCreateView(ListView):
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         form = PostCreateForm
#         content = {'form': form}
#         return render(request, 'pages/.html', content)
#
#     def post(self, request, *args, **kwargs):
#         form = PostCreateForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             post.save()
#             return HttpResponseRedirect(reverse_lazy('create-post'))
#         return render(request, '.html', {'form': form})
#
#
class ContactView(CreateView):

    def get(self, request, *args, **kwargs):
        form = ContactFrom
        content = {'form': form}
        return render(request, 'pages/contact.html', content)

    def post(self, request, *args, **kwargs):
        print('njjb')
        form = ContactFrom(request.POST)
        print(request.user)
        product = Product.objects.get(id=kwargs['id'])
        if form.is_valid():
            post = form.save(commit=False)
            post.subtotel = product.price*float(form.data['quantity'])
            post.product_id = product.id
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'pages/contact.html', {'form': form})


class CategoryDetailView(ListView):
    model = Product
    template_name = 'pages/hendrerit.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(type=self.kwargs['type'])
        print('products', Product.objects.filter(type=self.kwargs['type']))
        return context