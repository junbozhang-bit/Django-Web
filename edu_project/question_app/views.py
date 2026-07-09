from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionAddSerializer,AnswerSerializer,QuestionListSerializer,QuestionDetailSerializer
from .models import Question
from course_app.models import Section
from user_app.models import User
from user_app.utils import verify_token
from rest_framework import generics
# Create your views here.
class QuestionView(APIView):
    def post(self,request,format=None):
        serializer = QuestionAddSerializer(data=request.data)
        if serializer.is_valid():
            data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
            user = User.objects.filter(phone=data.get('phone')).first()
            section = Section.objects.get(id=serializer.validated_data.get('section'))
            #创建问题
            Question.objects.create(
                title = serializer.validated_data.get('title'),
                content = serializer.validated_data.get('content'),
                section = section,
                user = user
            )
            return Response({'message':'创建成功','code':201},status=201)
        return Response({'message':'创建失败','code':400},status=400)
    
class AnswerView(APIView):
    def post(self,request,format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
            user = User.objects.filter(phone=data.get('phone')).first()
            section = Section.objects.get(id=serializer.validated_data.get('section'))
            question = Question.objects.get(id=serializer.validated_data.get('question'))
            Question.objects.create(
                content = serializer.validated_data.get('content'),
                section = section,
                user = user,
                answers = question
            )
            return Response({'message':'创建成功','code':201},status=201)
        return Response({'message':'创建失败','code':400},status=400)
    
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.filter(answers=None).all().order_by('-create_time')
    serializer_class = QuestionListSerializer

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

class QuestionSectionListView(generics.ListAPIView):
    serializer_class = QuestionDetailSerializer
    def get_queryset(self):
        #获取小结id
        section_id = self.request.query_params.get('section')
        return Question.objects.filter(section=section_id).filter(answers=None).all().order_by('-create_time')
    