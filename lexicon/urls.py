from django.urls import path

from . import views


app_name = 'lexicon'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/', views.TermDetail.as_view(), name='term_detail'),
    path('random/', views.random_term, name='random_term'),
    path('<int:term_id>/add_sentence/', views.add_sentence, name='add_sentence'),
]
