from django.urls import path
from .import views 

urlpatterns = [
  
    path('api/',views.firstapi, name='firstapi'),
    path('',views.Home, name='home'),
    path('registerApi/',views.RegistationApi,name='RegistationApi'),
    path('planlist/',views.planlist.as_view()),
    path('plancreate/',views.plancreate.as_view()),
    path('plandelete/<int:pk>',views.plandelete.as_view())
    

    	
]
