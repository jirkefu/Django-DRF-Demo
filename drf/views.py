from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from drf.models import *
from rest_framework.response import Response


# DRF
class Car(APIView):

    def get(self, request):
        print("drf request get.")
        return HttpResponse("drf response get.")


# CBV
class Animal(View):

    def get(self, request):
        print("request get.")
        return HttpResponse("response get.")


# FBV
def get_dog(request):
    return HttpResponse("response get_dog function.")


"""
结语：
    CBV基于FBV,DRF基于CBV,源码涉及面向对象的知识，即self和cls的身份和属性和方法的访问空间顺序
    核心内容是as_view(),dispatch()
    特性；
        重写request，以便支持存储和解析更多类型的数据传输
        初始化工作，提供扩展的功能，包括身份认证、权限检查、流量控制
"""

"""=================================================================================================================="""

"""
导语：
    学习Serializes类（组件：序列化器），进行数据的序列化和反序列化，难点在于序列化和反序列化的过程及前后的数据处理，还有数据（表）间的关联操作
    （涉及一对一，一对多，多对多，models的外键设置） 
"""

from drf.serializers import *


class BookView(APIView):

    def get(self, request):
        books = Book.objects.all()  # QuerySet([book1, book2, ...])
        books_data = GetOneBookModelSerializers(instance=books, many=True)
        return Response(books_data.data)

    """
    未使用save()方式封装业务逻辑
    """
    # def post(self, request):
    #     book_ser = BookSerializers(data=request.data)
    #     if book_ser.is_valid(): # serializer.validated_data serializer.errors
    #         book = Book.objects.create(**book_ser.validated_data)
    #         book_data = BookSerializers(instance=book, many=False)
    #         return Response(book_data.data)
    #     return Response(book_ser.errors)

    """save()的使用和实现序列化器的create()方法来封装业务代码"""

    # todo 处理单个和批量提交
    def post(self, request):
        book_ser = BookSerializers(data=request.data)
        if book_ser.is_valid():  # serializer.validated_data serializer.errors
            book_ser.save()
            print(book_ser.data)
            return Response(book_ser.data)
        return Response(book_ser.errors)

    """
    总结：序列化对象调用save()方法在执行重写的create()或update()之后，
    我们自定义将创建或更新后返回的对象赋给instance属性，接着，
    通过序列器的data属性方法将instance属性进行序列化成json字符串格式返回。
    （即，序列器的data属性方法，针对self.instance进行序列化）
    """


class BookViewExtend(APIView):

    def get(self, request, id):
        book = Book.objects.get(id=id)  # models对象
        # 通过不同序列化器控制所需返回的字段，使用ModelSerializer
        book_ser = GetOneBookModelSerializers(instance=book, many=False)
        return Response(book_ser.data)

    def put(self, request, id):
        book = Book.objects.get(id=id)
        book_ser = BookSerializers(data=request.data, instance=book)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        return Response(book_ser.errors)

    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response("成功")
        except Book.DoesNotExist:
            return Response("失败")


"""
总结：
1、使用 ModelSerializer,其作用和Serializer一致，只是帮我们简化了字段的配置和完成create()、update(),并满足一对多、多对多的处理
2、通过配置不同的序列化器以满足不同需求，如控制返回的所需字段，create()和update()的业务逻辑等
"""


"""
其他视图类：GenericAPIView
"""
from rest_framework.generics import GenericAPIView


class UserView(GenericAPIView):
    def get(self, request):
        user_list = User.objects.all()
        serializer = UserModelSerializer(instance=user_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

