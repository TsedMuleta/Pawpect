from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('store/', views.store, name='store'),
    path('order/<int:food_id>/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('signup/', views.signup, name='signup'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
