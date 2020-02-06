import json
from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, "index/index.html")


class ApiImpView(View):
    def post(self, request):
        data = json.loads(request.body.decode())
        print(data)
        code = data["code"]
        if code == "importance":
            ret = {
                'name': ["北京", "上海", "广州", "西安", "深圳", "宿迁", "杭州"],
                'data': [1, 2, 3, 4, 5, 6, 7]
            }
        elif code == "speed_add":
            ret = {
                "name": ["武汉", "黄冈", "孝感", "随州", "襄阳", "荆州", "宣昌"],
                'data': [80, 60, 55, 42, 33, 31, 29]
            }
        elif code == "all_type_add":
            ret = {
                "name": ["确诊", "疑似", "死亡", "康复"],
                'data': [3287, 5072, 65, 240]
            }
        elif code == "plot_two":
            ret = {
                "name": ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                       '18', '19', '20', '21', '22', '23', '24'],
                'data': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                "data1": [2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 19, 30, 13, 11, 19, 20, 22, 25, 26, 27, 28, 29, 30]
            }
        elif code == "par_cycle":
            ret = {
                "data": [20388, 20455, 19000, 20000, 20000]
            }
        elif code == "par_deed":
            ret = {
                "data": [300, 200]
            }
        elif code == "pie_all_info":
            ret = {
                "data": [50, 10, 60, 20]
            }
        elif code == "pie_cure":
            ret = {
                "data": [15000, 800]
            }
        else:
            ret = {}

        return http.JsonResponse(ret)


class MepInfoView(View):
    def post(self, request):
        return http.JsonResponse("ok")
