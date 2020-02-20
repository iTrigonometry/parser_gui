from django.urls import path
from . import views

# чтобы django не путался в приложениях
app_name = 'main_app'

# если пользователь переходит в путь в первом парметре
# выполнятеся код из второго параметра
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),  # для тестов
]
