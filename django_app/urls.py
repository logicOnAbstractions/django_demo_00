"""django_demo_00 URL Configuration

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
from . import views
from django.urls import path

# app_name = "django_app"
urlpatterns = [

    # generic pattern: path([url], my_view, ??template_name?)

    path('', views.index, name='index'),            # default landing page at /ROOT/django_app/
    path('<int:question_id>', views.detail, name='detail'),                         # /django_app/42
    path('<int:question_id>/results/', views.results, name='results'),              # /django_app/42/results
    path('<int:question_id>/vote/', views.vote, name='vote'),                       # /django_app/42/vote

]
