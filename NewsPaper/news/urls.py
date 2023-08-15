from django.urls import path
from .views import NewsList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    PostSearchView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем статьям у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),  # т.к. сам по себе это класс, то нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали статьи
    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание статьи
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),  # Ссылка на редактирование статьи
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),  # Ссылка на удаление статьи
    path('search/', PostSearchView.as_view(), name='post_search'),  # Ссылка на поиск статьи
]