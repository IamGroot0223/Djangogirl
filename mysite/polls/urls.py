import urllib


from django.urls import path
from . import views

app_name='polls'
urlpatterns=[
    path('', views.index, name='index'),

    path('<int:question_id>/',views.detail,name='detail'),  #<int:question_id> 使用尖括号“捕获”这部分 URL，匹配question_id

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]


