from . import views
from django.urls import path

app_name = 'home' 

urlpatterns = [
    #/home/
    path('', views.index,name='index'),
    #/home/1
    path('<int:item_id>/', views.detail,name='detail'),
    
    
    #path('product/', views.product,name='product'),
    
    #community
    path('community/', views.community,name='community'),

    #quiz
    path('quiz/', views.quiz,name='quiz'),

    path('createpost/', views.createpost, name='createpost')
]
