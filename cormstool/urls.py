"""cormstool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include,path
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("step/1/", views.step1, name="step1"),
    path("step/2/", views.step2, name="step2"),
    path("step/3/", views.step3, name="step3"),
    path("results/", views.results, name="results"),
    path("projects/", views.projects, name="projects"),
    path("projects/add/", views.add_project, name="add_project"),
    path("upload/", views.upload, name="upload"),
    path('download/<str:filename>', views.download_file, name="download_file")
]
