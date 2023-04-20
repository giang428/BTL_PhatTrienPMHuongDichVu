from django.shortcuts import render
from .models import History
from user.models import User
from django.db.models import Q
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def getlistHistory(request,id):
    u=User.objects.get(id_user=id)
    listHist=History.objects.filter(user=u)
    if listHist:
        data=list(listHist.values())
        return Response({"data":data,"message":"Success","code":status.HTTP_200_OK},status=status.HTTP_200_OK)
    return Response({"data":[],"message":"Failed","code":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def stat(request):
    # is_vip = 1 : 1 month
    # is_vip = 2 : 1 year
    # params: 
    hist = History.objects.all()
    if hist:
        data = hist.values()
        res = request.query_params.get('period')
        if res: #period params
           period = parse_time(res)
           if period:
                if period[1] == '%Y-%m-%d':
                    filter = [d 
                              for d in data 
                              if datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f").date() == period[0].date()]
                    vip_1 = sum(1 for dat in filter if dat['is_vip'] == 1)
                    vip_2 = sum(1 for dat in filter if dat['is_vip'] == 2)
                    return Response({"data":filter,
                                      "statistic":{
                                        "monthly_count":vip_1,
                                        "yearly_count":vip_2,
                                        "profit":(47000*vip_1 + 436000*vip_2)
                                        },
                                    "message":"Success"})
                
                elif period[1] == '%Y-%m':
                    filter = [d 
                              for d in data 
                              if datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f") >= period[0] 
                              and datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f") <= period[0] + relativedelta(months=1)]
                    vip_1 = sum(1 for dat in filter if dat['is_vip'] == 1)
                    vip_2 = sum(1 for dat in filter if dat['is_vip'] == 2)
                    return Response({"data":filter,
                                      "statistic":{
                                        "monthly_count":vip_1,
                                        "yearly_count":vip_2,
                                        "profit":(47000*vip_1 + 436000*vip_2)
                                        },
                                    "message":"Success"})
                
                elif period[1] == '%Y':
                    filter = [d 
                              for d in data 
                              if datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f") >= period[0] 
                              and datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f") <= period[0] + relativedelta(years=1)]
                    vip_1 = sum(1 for dat in filter if dat['is_vip'] == 1)
                    vip_2 = sum(1 for dat in filter if dat['is_vip'] == 2)
                    return Response({"data":filter,
                                      "statistic":{
                                        "monthly_count":vip_1,
                                        "yearly_count":vip_2,
                                        "profit":(47000*vip_1 + 436000*vip_2)
                                        },
                                    "message":"Success"})
           else:
               return Response({"message":"Invaild format!"},status=status.HTTP_400_BAD_REQUEST)                     
        else:
            fr = request.query_params.get('from')
            to = request.query_params.get('to')
            if fr and to:
                start_time = parse_time(fr)
                end_time = parse_time(to)
                print(start_time)
                print(end_time)
                if start_time == None or end_time == None or start_time >= end_time:
                    return Response({"message":"Invaild time format!"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    filter = [d 
                                for d in data 
                                if datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f") >= start_time[0] 
                                and datetime.strptime(d['exp_vip'],"%Y-%m-%d %H:%M:%S.%f") <= end_time[0]]
                    vip_1 = sum(1 for dat in filter if dat['is_vip'] == 1)
                    vip_2 = sum(1 for dat in filter if dat['is_vip'] == 2)
                    return Response({"data":filter,
                                        "statistic":{
                                        "monthly_count":vip_1,
                                        "yearly_count":vip_2,
                                        "profit":(47000*vip_1 + 436000*vip_2)
                                        },
                                    "message":"Success"})
            else:        #if not present period params
                vip_1 = sum(1 for dat in data if dat['is_vip'] == 1)
                vip_2 = sum(1 for dat in data if dat['is_vip'] == 2)  
                return Response({
                        "data":data,
                        "statistic":{
                            "monthly_count":vip_1,
                            "yearly_count":vip_2,
                            "profit":(47000*vip_1 + 436000*vip_2)
                            },
                        "message":"Success"
                        },status=status.HTTP_200_OK)               
    else:
        return Response({"message":"No data!"})
def parse_time(period):
    formats = ['%Y-%m-%d', '%Y-%m', '%Y']
    for fmt in formats:
        try:
            return [datetime.strptime(period, fmt),fmt]
        except ValueError:
            pass
    return None