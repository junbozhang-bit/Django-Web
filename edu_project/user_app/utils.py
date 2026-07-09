'''
user的唯一标识 通过 加密算法 生成token
'''
import jwt
import time
from django.conf import settings
def generate_token(data):
    #增加要加密的过期时间，现在时间+过期时长
    data.update({'exp':settings.JWT_EXPIRED + int(time.time())})
    #通过加密算法生成token
    # token = jwt.encode(data,'123456789',algorithm='HS256')
    token = jwt.encode(data,settings.JWT_SECRET_KEY,algorithm='HS256')
    #返回token
    return token
def verify_token(token):
    #通过解密算法验证token
    try:
        # data = jwt.decode(token,'123456789',algorithms='HS256')
        data = jwt.decode(token,settings.JWT_SECRET_KEY,algorithms='HS256')
    except Exception as e:
        return None
    '''
    # 以下逻辑不需要我们实现，jwt已经实现
    #获取token中的过期时间
    exp_time = data.get('exp')
    #获取当前时间
    now_time = time.time()
    if now_time > exp_time:
        return None
    '''
    #返回token中的user_id
    return data

if __name__ == '__main__':
    data = {'phone':'12345678901'}
    t = generate_token(data)
    print(f'生成token:{t}')
    d = verify_token(t)
    print(f'验证token:{d}')