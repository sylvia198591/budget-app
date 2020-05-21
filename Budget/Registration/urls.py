"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Registration import views

from Registration.views import *

urlpatterns = [
    path('Entrycr', views.Entrycr.as_view(),name="Entry_cr"),
    path('Entryv', views.Entryv.as_view(),name="Entry_v"),
    path('Essentialcr', views.Essentialcr.as_view(), name="Essential_cr"),
    path('Essentialv', views.Essentialv.as_view(), name="Essential_v"),
    path('Accountcr', views.Accountcr.as_view(), name="Account_cr"),
    path('Accountv', views.Accountv.as_view(), name="Account_v"),
    path('Usercr', views.Usercr.as_view(), name="User_cr"),
    path('Userl', views.Userl.as_view(), name="User_l"),
    path('Entryccdd', views.Entryccdd.as_view(), name="Entryccdd"),

]
# urlpatterns = [
#     path('catcr', getCatcr,name="cat_cr"),
#     path('cres', getCres, name="c_res"),
#     path('cedit/<int:pk>', getCedit, name="c_edit"),
#     path('cview/<int:pk>', getCview, name="c_view"),
#     path('cdel/<int:pk>', getCdel, name="c_del"),
#     path('prodcr', getProdcr,name="prod_cr"),
#     path('pres', getPres, name="p_res"),
#     path('pedit/<int:pk>', getPedit,name="p_edit"),
#     path('pview/<int:pk>', getPview, name="p_view"),
#     path('pdel/<int:pk>', getPdel, name="p_del"),
# ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


