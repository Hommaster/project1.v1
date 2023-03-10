from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *


menu = [
    {'title': "О  сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>лох</p>')

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    #extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context
    def get_queryset(self):
        return Women.objects.filter(is_published=True)

# def index(request):
#     posts = Women.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)

def about(request):
    context = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'women/about.html', context=context)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Добавление нового поста'
        return context

# def addpage(request):
#     if request.method=='POST':
#         form = AddPostForm(request.POST, request.FILES,)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     context = {
#         'form': form,
#         'menu': menu,
#         'title': 'Добавление новой статьи',
#     }
#     return render(request, 'women/addpage.html', context=context)

def contact(request):
    return render(request, 'women/contact.html', {'title': 'Обратная связь'})

def login(request):
    return HttpResponse("Авторизация")

class ShowPost(DetailView):
    model=Women
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    template_name = 'women/post.html'
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']=context['post']
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post_slug,
#         'menu': menu,
#     }
#     return render(request, 'women/post.html', context=context)


# def show_cats(request, cat_slug):
#     posts = Women.objects.filter(cat__slug=cat_slug)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_slug,
#     }
#     return render(request, 'women/index.html', context=context)

class WomenCats(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    #allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - '+ str(context['posts'][0].cat)
        context['menu']=menu
        context['cat_selected'] = self.kwargs['cat_slug']
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)