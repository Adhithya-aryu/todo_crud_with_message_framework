from django.urls import path
from message_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('update/<int:id>',views.update,name="update"),
    path('add',views.add,name="add"),
    path('all',views.all,name="all"),
    path('delete/<int:id>',views.delete,name="delete")
]
