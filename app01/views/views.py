from django.http import JsonResponse
from app01.utils.R import result, error
from app01.models import BreastCancer
from app01.utils.cancerPredict import cancerPredict
import json


def predict(request):
    if request.method != "POST":
        res = error(code=1, msg="访问方法错误")
        return JsonResponse(res)

    # 如果是post请求则开始处理逻辑
    # todo:获取请求数据
    data_json = request.POST.get("data")
    data = json.loads(data_json)
    # info = json.loads(request.body.decode('utf-8')) 可以直接发送json
    """
    0.444444	0.000000	0.000000	0.000000	0.111111	0.000000	0.222222	0.000000	0.000000
    {
      "data": {
        "clump_thickness": 0.444444,
        "uniformity_of_cell_size": 0.000000,
        "uniformity_of_cell_shape": 0.000000,
        "marginal_adhesion": 0.000000,
        "single_epithelial_cell_size": 0.111111,
        "bare_nuclei": 0.000000,
        "bland_chromatin": 0.222222,
        "normal_nucleoli": 0.000000,
        "mitoses": 0.000000
      }
    }
    
    """
    # 封装数据
    data_list = []
    key_list = ["clump_thickness", "uniformity_of_cell_size", "uniformity_of_cell_shape", "marginal_adhesion",
                "single_epithelial_cell_size",
                "bare_nuclei", "bland_chromatin", "normal_nucleoli", "mitoses"]
    for key in key_list:
        data_list.append(data['data'][key])
    # 预测调用
    isCancer = cancerPredict(data_list)
    # 写入数据库
    BreastCancer.objects.create(clump_thickness=data_list[0], uniformity_of_cell_size=data_list[1],
                                uniformity_of_cell_shape=data_list[2], marginal_adhesion=data_list[3],
                                single_epithelial_cell_size=data_list[4],
                                bare_nuclei=data_list[5], bland_chromatin=data_list[6],
                                normal_nucleoli=data_list[7], mitoses=data_list[8], result=isCancer)
    res = result(code=0, msg="success", data=isCancer)
    return JsonResponse(res)
