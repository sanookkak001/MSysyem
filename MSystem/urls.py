from django.contrib import admin
from django.urls import path,include
from Main import views as Mainviews
from Stock import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Mainviews.index, name='index'),
    path('Stock_info/', include('Stock.urls'), name='Stock_information'),
]
