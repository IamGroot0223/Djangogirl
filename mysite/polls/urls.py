import urllib


from django.urls import path
from . import views

app_name='polls'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  #<int:question_id> 使用尖括号“捕获”这部分 URL，匹配question_id

    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]

