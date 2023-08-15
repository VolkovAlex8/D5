from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  # , SearchView
# импоритируем необходимые дженерики
# импортируем класс ListView, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
# импортируем класс DetailView получения деталей объекта
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .models import Post, Category, Author, \
    PostCategory  # Дополнительно импортируем категорию, чтобы пользователь мог её выбрать
from .filters import PostFilter  # импортируем недавно написанный фильтр
from .forms import PostForm  # импортируем нашу форму


# from datetime import datetime

class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML,
    # в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты,
    # его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = [
        '-dateCreation']  # сортировка по дате публикации, сначала более новые /  queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 1 # поставим постраничный вывод в один элемент


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'news_app/post_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните.
# Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'news_app/post_create.html'
    form_class = PostForm


# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'news_app/post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления поста
class PostDeleteView(DeleteView):
    template_name = 'news_app/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


# дженерик для поиска поста
class PostSearchView(ListView):
    model = Post
    template_name = 'news_app/post_search.html'
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты,
    # его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = [
        '-dateCreation']  # сортировка по дате публикации, сначала более новые /  queryset = Post.objects.order_by('-dateCreation')

    def get_context_data(self, **kwargs):
        # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        # context['categories'] = Category.objects.all()
        # context['form'] = PostForm()
        return context