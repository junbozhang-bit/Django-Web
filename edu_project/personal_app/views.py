from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCourseNameListSerializer,UserCourseListSerializer,MySectionListSerializer,UserAddSectionSerializer,OrderListSerializer
from user_app.utils import verify_token
from user_app.models import User
from .models import UserCourse,UserSection
from course_app.models import Section
# Create your views here.
class UserCourseNameListView(APIView):
    def get(self,request,format=None):
        #根据token获取用户唯一标识
        data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
        #根据用户唯一标识获取用户信息
        if data:
            try:
                user = User.objects.filter(phone=data.get('phone')).first()
            except Exception as e:
                return Response({'message':'用户信息有误','code':400},status=400)
            #根据用户信息查询用户课程
            user_course = UserCourse.objects.filter(user=user)
            serializer = UserCourseNameListSerializer(user_course,many=True)
            return Response(serializer.data)
        return Response({'message':'用户不存在','code':401},status=401)
    
class UserCourseListView(APIView):
    def get(self,request,format=None):
        #根据token获取用户唯一标识
        data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
        #根据用户唯一标识获取用户信息
        if data:
            try:
                user = User.objects.filter(phone=data.get('phone')).first()
                user_course = UserCourse.objects.filter(user=user)
                serializer = UserCourseListSerializer(user_course,many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'message':'用户信息有误','code':400},status=400)
        else:
            return Response({'message':'用户不存在','code':401},status=401)

class MySectionListView(APIView):
    def get(self,request,format=None):
        #根据token获取用户唯一标识
        data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
        #根据用户唯一标识获取用户信息
        if data:
            try:
                user = User.objects.filter(phone=data.get('phone')).first()
                user_section = UserSection.objects.filter(user=user)
                serializer = MySectionListSerializer(user_section,many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'message':'用户信息有误','code':400},status=400)
        else:
            return Response({'message':'用户不存在','code':401},status=401)
        
class UserAddSectionView(APIView):
    def post(self,request,format=None):
        #检验section是否传递
        serializer = UserAddSectionSerializer(data=request.data)
        if serializer.is_valid():
            data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
            if data:
                try:
                    user = User.objects.filter(phone=data.get('phone')).first()
                    section = Section.objects.filter(pk=serializer.data.get('section')).first()
                    UserSection.objects.create(user=user,section=section)
                    return Response({'message':'添加收藏成功','code':200},status=200)
                except Exception as e:
                    return Response({'message':'用户信息有误','code':400},status=400)
        return Response({'message':'请传递要保存的小节ID','code':401},status=401)
    
from rest_framework import generics
from order_app.models import Order

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        data = verify_token(self.request.META.get('HTTP_AUTHORIZATION'))
        user = User.objects.filter(phone=data.get('phone')).first()
        queryset = Order.objects.filter(user=user)
        return queryset
    # def get(selfmself,request,format=None):
    #     data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
    #     if data:
    #         try:
    #             user = User.objects.filter(phone=data.get('phone')).first()
    #             order = Order.objects.filter(user=user)
    #             serializer = OrderListSerializer(order,many=True)
    #             return Response(serializer.data)
    #         except Exception as e:
    #             return Response({'message':'用户信息有误','code':400},status=400)
    #     return Response({'message':'用户不存在','code':401},status=401)