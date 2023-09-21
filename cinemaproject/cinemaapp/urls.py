from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.test,name='test'),
    path('movie/<int:film_id>/',views.detail,name='detail'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    ]