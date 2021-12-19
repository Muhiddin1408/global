
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Category, Jihozlar, Post, SendMessage, Buy
from .forms import PostCreateForm, ContactFrom, BuyForm
from django.urls import reverse_lazy


# Create your views here.


class Index(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'


class JihozlarView(ListView):
    model = Jihozlar
    template_name = 'pages/jihozlar.html'
    context_object_name = 'jihozlars'
    paginate_by = 9


class PostView(ListView):
    model = Post
    template_name = 'pages/hendrerit.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def get_post(request, id):
    post = Post.objects.get(id=id)
    res = {
        "post": post
    }
    return render(request, 'pages/post.html', res)


def get_category(request, id):
    category = Category.objects.get(id=id)
    res = {
        "category": category
    }
    return render(request, 'pages/category.html', res)


def get_jihoz(request, id):

    jihoz = Jihozlar.objects.get(id=id)
    res = {
        "jihoz": jihoz
    }
    return render(request, 'pages/jihoz.html', res)


def post_jihoz_buyurtma(request, id):
    print(request.method)
    if request.method == 'POST':
        jihoz = Jihozlar.objects.get(id=id)
        form = BuyForm(request.POST)
        if not form.is_valid():
            print(form.cleaned_data['number'], form.cleaned_data['name'])
            print(form.cleaned_data['phone_number'])
            post = form.save()
            post.save()
            # Buy.objects.create(
            #     title=jihoz.title,
            #     price=jihoz.price,
            #
            # )
            return HttpResponseRedirect(reverse_lazy('jihoz-buyurtma'))
        return render(request, 'pages/jihoz.html', {'form': form})


class PostCreateView(CreateView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        form = PostCreateForm
        print(Post.photo)
        content = {'form': form}
        return render(request, 'pages/create_card.html', content)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('create-post'))
        return render(request, 'pages/create_card.html', {'form': form})


class ContactView(CreateView):
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

