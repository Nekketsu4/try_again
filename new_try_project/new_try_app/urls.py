from django.urls import path
from .views import *

app_name = 'new_try_app'
urlpatterns = [
    path('', Simple_indexView.as_view(), name='simple_index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),

]