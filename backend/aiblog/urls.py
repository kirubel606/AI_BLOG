"""
URL configuration for aiblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),
    path('api/blogs/', include('blogs.urls')),
    path('collaborations/', include('collaborations.urls')),
    path('settings/', include('settings.urls')),
    path('contacts/', include('contact_us.urls')),
    path('faq/', include('faq.urls')),
    path('resources/', include('resources.urls')),
    path('rnd/', include('rnd.urls')),
    path('about/', include('about_us.urls')),
    path('categories/', include('categories.urls')),
    path('events/', include('events.urls')),
    path('news/', include('news.urls')),
    path('quotes/', include('quotes.urls')),
]
