from django.urls import path
from . import views

# このアプリケーションのルーティングに名前を付けてる。他のアプリと重複しないように注意
app_name="diary"

urlpatterns=[
    # ルーティングした後、処理をIndexViewに渡す
    path('',views.IndexView.as_view(),name="index")
]
