import json
import redis
from django import http
from django.shortcuts import render
import pandas as pd
# Create your views here.
from django.views import View
from .models import DataAll


red = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)


class IndexView(View):
    def get(self, request):
        # 查询最新cycle的索引

        return render(request, "index/index.html", {"confirmedCount": red.get("confirmed_all"), "curedCount": red.get("cured_all")})


class ApiImpView(View):
    def post(self, request):
        data = json.loads(request.body.decode())
        code = data["code"]

        if code == "importance":
            ret = {
                "name": red.lrange("serious_index", 0, red.llen("line_data_date")),
                'data': red.lrange("serious_value", 0, red.llen("serious_value"))
            }

        elif code == "speed_add":
            ret = {
                "name": red.lrange("add_nums_index", 0, red.llen("add_nums_index")),
                'data': red.lrange("add_nums_value", 0, red.llen("add_nums_value"))
            }

        elif code == "all_type_add":
            ret = {
                "name": ["康复", "死亡"],
                'data': red.lrange("bar_num", 0, red.llen("bar_num"))
            }

        elif code == "plot_two":
            ret = {
                "name": red.lrange("line_data_date", 0, red.llen("line_data_date")),
                'data': red.lrange("line_data_value1", 0, red.llen("line_data_value1")),
                "data1": red.lrange("line_data_value2", 0, red.llen("line_data_value2"))
            }

        elif code == "par_cycle":
            ret = {
                "data": [20388, 20455, 19000, 20000, 20000]
            }

        elif code == "pie_all_info":
            ret = {
                "data": red.lrange("confirmed_num", 0, red.llen("confirmed_num"))

            }

        elif code == "par_deed":
            ret = {
                "data": red.lrange("deed_num", 0, red.llen("deed_num"))
            }

        elif code == "pie_adds":
            ret = {
                "data": red.lrange("add_nums", 0, red.llen("add_nums"))
            }
        elif code == "code_map":
            ret = {
                "name": red.lrange("map_index", 0, red.llen("map_index")),
                "value": red.lrange("map_value", 0, red.llen("map_value"))
            }
        else:
            ret = {}

        return http.JsonResponse(ret)


class MepInfoView(View):
    def post(self, request):
        return http.JsonResponse("ok")
