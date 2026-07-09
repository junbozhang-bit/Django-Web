from rest_framework.views import APIView
from user_app.models import User
from rest_framework import status,generics
from rest_framework.response import Response
from .serializer import RegisterSerializer,UserDetailSerializer
from .utils import generate_token
# Create your views here.
class LoginView(APIView):
    '''
    登录功能
    '''
    def post(self,request):
        # 获取参数
        phone = request.data.get('phone')
        password = request.data.get('password')
        #根据参数获取数据
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({'code':status.HTTP_404_NOT_FOUND,'msg':'用户不存在'})
        #校验密码
        if user.check_password(password):
            #生成token
            token = generate_token({'phone':phone})
            return Response({'code':status.HTTP_200_OK,'msg':'登录成功','token':token})
        else:
            return Response({'code':status.HTTP_400_BAD_REQUEST,'msg':'密码错误'})
        
class RegisterView(APIView):
    '''
    注册功能
    '''
    def post(self,request):
        #创建序列化器
        serializer = RegisterSerializer(data=request.data)
        #校验参数
        if serializer.is_valid():
            #成功
            user = serializer.save()
            return Response({
                'code':status.HTTP_201_CREATED,
                'msg':'注册成功'
            })
        #失败
        else:
            return Response({
                'code':status.HTTP_400_BAD_REQUEST,
                'msg':f'注册失败{serializer.errors}'
            })

#获取用户信息
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer