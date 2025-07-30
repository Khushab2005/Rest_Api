from django.urls import path
from myapp.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    
    # --------------------jWT token authentication------------------
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ---------------------end---------------
    # -----------------basic token authentication------------------
    path('secure_data/',secure_data, name='secure_data'),
    
    # ---------------------generic base api------------------
    path('generic_list/',genericlistcreate.as_view(),name='genericlistcreate'),
    path('generic_list/<int:id>',genericretriveupdatedestroy.as_view(),name='genericretriveupdatedestroy'),  
    # ---------------------end--------------------------------
    # ---------------------function base api------------------
    path('f_get/',f_get, name='f_get'),
    path('f_post/',f_post, name='f_post'),
    path('f_put/<int:id>',f_put, name='f_put'),
    path('f_patch/<int:id>',f_patch, name='f_patch'),
    path('f_delete/<int:id>',f_delete, name='f_delete'),
    # ---------------------end--------------------------------
    # ---------------------Class based api--------------------
    path('class_employee/',Class_Employe.as_view(),name='class_employee'),
    path('class_employee/<int:id>',Classs_Employe.as_view(),name='class_employee'),  
    # ---------------------end--------------------------------
    
]
