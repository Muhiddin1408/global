from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import ListView, CreateView
from .models import SendMessage, Product
from .forms import ContactFrom, UserRegisterForm
from django.urls import reverse_lazy


# Create your views here.

# login user
class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


# create new user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})




#
# class Index(ListView):
#     model = Category
#     if Product.type == 'CLOTHES':
#         template_name = 'index.html'
#         context_object_name = 'categories'
#         paginate_by = 9
# #
# #
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

    template_name = 'index.html'
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
#     return render(request, 'pages/jihoz.html', res)

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
#         return render(request, 'pages/jihoz.html', {'form': form})
#
#
# class PostCreateView(CreateView):
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         form = PostCreateForm
#         content = {'form': form}
#         return render(request, 'pages/create_card.html', content)
#
#     def post(self, request, *args, **kwargs):
#         form = PostCreateForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             post.save()
#             return HttpResponseRedirect(reverse_lazy('create-post'))
#         return render(request, 'pages/create_card.html', {'form': form})


class ContactView(CreateView):
    def get_queru(self, id):
        post = Product.objects.get(id=id)
        res = {

        }
    queryset = SendMessage.objects.all()

    def get(self, request, *args, **kwargs):
        form = ContactFrom
        content = {'form': form}
        return render(request, 'pages/contact.html', content)

    def post(self, request, *args, **kwargs):
        form = ContactFrom(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('contact'))
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
