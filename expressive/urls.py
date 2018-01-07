from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('lexicon/', include('lexicon.urls')),
    path('admin/', admin.site.urls),
]
