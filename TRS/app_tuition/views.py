from django.shortcuts import render
from django.http import  JsonResponse
import pandas as pd

def home(request):
    return render(request, 'app_tuition/home.html')

dt_tuition = pd.read_csv('app_tuition/dataset/tuition_tuition.csv', sep=',')

data={}
for idx, row in dt_tuition.iterrows():
    data[row['category']] = eval(row['tuition'])

del dt_tuition

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def api_get_year_tuition(request):
    cate = request.POST.get('program_category')
    topk = request.POST.get('topk')
    topk = int(topk)
    print(cate, topk)

    chart_data, wf_pairs = get_category_tuition(cate, topk)
    response = {
        'chart_data': chart_data,
          'wf_pairs': wf_pairs,
         }
    #print(response)
    return JsonResponse(response)

def get_category_tuition(cate, topk=10):
    wf_pairs = data[cate][0:topk]
    words = [w for w, f in wf_pairs]
    freqs = [f for w, f in wf_pairs]
    chart_data = {
        "category": cate,
        "labels": words,
        "values": freqs}
    return chart_data, wf_pairs

print("app_tuition--日間學士班學費載入成功!")



    