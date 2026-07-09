from .utils import verify_token
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        #判断用户访问的接口是否是与用户相关的接口
        if request.path.startswith('/api/user/'):
            #判断是否登录
            if not verify_token(request.META.get('HTTP_AUTHORIZATION')):
                #未登录
                # return Response({
                #     'code':status.HTTP_401_UNAUTHORIZED,
                #     'msg':'用户未登录'
                # })
                return JsonResponse(
                    {
                    'code':status.HTTP_401_UNAUTHORIZED,
                    'msg':'用户未登录'
                    },
                    json_dump_params={'ensure_ascii':False}
                    )                  
        #已登陆，执行后续代码
        return self.get_response(request)