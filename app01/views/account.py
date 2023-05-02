import json
from django.http import JsonResponse
from app01.utils.R import error, result
from app01.models import UserInfo
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler


def login(request):
    if request.method != "POST":
        res = error(code=1, msg="访问方法错误")
        return JsonResponse(res)
    # post请求才处理
    data_json = request.POST.get("data")
    data = json.loads(data_json)
    username = data['data']["username"]
    password = data['data']["password"]  # 已经加密了

    # 数据校验
    if username and password:
        user_object = UserInfo.objects.filter(username=username).first()
        if user_object is None:
            res = error(code=1, msg="用户名不存在")
            return JsonResponse(res)
        else:
            # 比较密码是否相同
            if user_object.password == password:
                #  写入session
                # request.session["info"] = {"id": user_object.id, "username": user_object.username}
                payload = jwt_payload_handler(user_object)
                token = jwt_encode_handler(payload)
                json_token = {"token": token}
                res = result(code=0, msg="登录成功！", data=json_token)
                return JsonResponse(res)
            else:
                # 密码错误
                res = error(code=1, msg="密码错误！")
                return JsonResponse(res)
    else:
        res = error(code=1, msg="用户名和密码不能为空！")
        return JsonResponse(res)


def register(request):
    if request.method != "POST":
        res = error(code=1, msg="访问方法错误")
        return JsonResponse(res)

    # post请求才处理
    data_json = request.POST.get("data")
    data = json.loads(data_json)
    """
        注册json
        {
            "data": {
                "username": "xxx",
                "password": "xxxx"
            }
        }
    """
    username = data['data']["username"]
    password = data['data']["password"]  # 已经加密了
    if username and password:  # 都不为null
        user_object = UserInfo.objects.filter(username=username).first()
        if user_object:
            # 用户名重复
            res = error(code=1, msg="用户名重复！")
            return JsonResponse(res)
        else:
            # 写入数据库
            UserInfo.objects.create(username=username, password=password)
            res = result(code=0, msg="注册成功", data={})
            return JsonResponse(res)
    else:
        res = error(1, msg="用户名和密码不能为空！")
        return JsonResponse(res)
