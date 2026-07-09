from django.shortcuts import render
from .serializers import OrdersSerializers
from .models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from user_app.utils import verify_token
from user_app.models import User
from plan_app.models import ClassType
from time import time
from .alipay_tool import get_qr
from json import loads
# Create your views here.
class OrdersView(APIView):
    def post(self,request,format=None):
        serializer = OrdersSerializers(data=request.data)
        if serializer.is_valid():
            data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
            user = User.objects.filter(phone=data.get('phone')).first()
            ct = ClassType.objects.filter(id=serializer.validated_data.get('class_type')).first()
            order_id = f'{user.id}{ct.id}{int(time())}'
            Order.objects.create(
                id = order_id,
                user = user,
                class_type = ct,
                amount = ct.price,
                course = ct.course
            )
            # 获取支付二维码
            info = f'{ct.course.name}-{ct.name}-{ct.price}'
            content = get_qr(order_id,info,float(ct.price))
            content = loads(content)
            qr_code = content.get('qr_code')
            return Response({'msg':'下单成功','code':200,'url':qr_code})
        else:
            return Response(serializer.errors)
        
class PayCallBackView(APIView):
    def post(self,request):
        # 获取订单号
        out_trade_no = request.POST.get('out_trade_no')
        # 获取支付的时间
        gmt_payment = request.POST.get('gmt_payment')
        # 获取订单支付金额
        total_amount = request.POST.get('total_amount')
        # 获取订单信息
        order = Order.objects.get(id = out_trade_no)
        # 修改订单状态
        order.order_type = 1
        order.total_amount = total_amount
        order.gmt_payment = gmt_payment
        # 保存支付信息
        order.save()
        # 返回结果
        return Response({'msg':'支付成功','code':200})