from django.urls import path, re_path
from drf import views

urlpatterns = [
    # DRF
    path("car/", views.Car.as_view()),
    # CBV
    path("animal/", views.Animal.as_view()),
    # FBC
    path("get_dog/", views.get_dog, name="get_dog"),

    # 序列化器的使用案例-路由
    path("book/", views.BookView.as_view()),
    re_path("book/(\d+)", views.BookViewExtend.as_view()),

    # GenericSerializer使用案例
    path("user/", views.UserView.as_view())
]
