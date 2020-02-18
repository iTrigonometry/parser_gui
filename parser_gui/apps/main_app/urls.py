from django.urls import path
from . import views

# чтобы django не путался в приложениях
app_name = 'main_app'

# kavo kuda zachem
urlpatterns = [
    path('', views.index, name='index'),
]
