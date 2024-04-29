from . import views
from django.urls import path

app_name = 'home' 

urlpatterns = [
    #/home/
    path('', views.index,name='index'),
    #/home/1
    path('<int:item_id>/', views.detail,name='detail'),
    
    
    #path('product/', views.product,name='product'),
    path('community/', views.community,name='community'),
    path('home/', views.home,name='home'),
    path('product/', views.home,name='product'),
    path('quiz/', views.quiz, name='quiz'),
   path('quiz/results/', views.quiz_results, name='quiz_results'),
    path('createpost/', views.createpost, name='createpost'), 

]
