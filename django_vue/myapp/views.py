from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Book
from .models import my_User
from .models import minsheng
from .form import RegisterForm
from .database import propertybydate
from .database import streeteventbydate
from .database import getabnormal
from .database import achievebydate
from .database import hotcommunity
from .database import getabnormal_form
from. database import achieved
# Create your views here.

username_logined = ''

@require_http_methods(["GET"])
def add_book(request):
    print('fuck')
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def get_date_event(request):
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    ans = propertybydate(date1, date2)
    print(ans)
    return JsonResponse(ans)

def get_date_street(request):
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    ans = streeteventbydate(date1, date2)
    test = {'市容城管':1,'工业噪声':2,'占道经营':3,'绿化养护':4,'公用部件':5,'公共交通管理':6}
    test['市容城管'] = ans[0]
    test['工业噪声'] = ans[1]
    test['占道经营'] = ans[2]
    test['绿化养护'] = ans[3]
    test['公用部件'] = ans[4]
    test['公共交通管理'] = ans[5]
    print(test)
    return JsonResponse(test)

def get_problem_handled(request):
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    ans1, ans2, ans3 = achievebydate(date1, date2)
    print(ans1, ans2, ans3)
    res = {}
    res['data1'] = ans1
    res['data2'] = ans2
    res['data3'] = ans3
    return JsonResponse(res)


def get_hotcommunity(request):
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    ans = hotcommunity(date1, date2)
    print(ans)
    return JsonResponse(ans)

def getdata_abnormal(request):
    count, ans = getabnormal()
    response = {}
    response['number'] = count
    response['data'] = ans
    return JsonResponse(response,safe=False)

def getabnormal_plus(request):
    cnt, ans = getabnormal_form()
    ans['cnt'] = cnt
    return JsonResponse(ans, safe=False)

def finish_rec_id(request):
    rec_id = request.GET.get('rec_id')
    achieved(rec_id)
    return HttpResponse("nice")

def get_name(request):
    res = {}
    res['name'] = username_logined
    # res['image']='../../assets/'+username_logined+'.png'
    return JsonResponse(res)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
# Create your views here.

def login(request):
    register_form = RegisterForm()  # 实例化表单
    return render(request, "login.html", {'register_form': register_form})


def login_action(request):
    request.encoding = 'utf-8'
    register_form = RegisterForm(request.POST)
    context = { }
    if request.method == "POST":
        result = {'error': ''}
        username = str(request.POST.get('username'))
        password = str(request.POST.get('password'))
        userdata = my_User.objects.values() # 从数据库中取出数据，格式为QuerySet
        for x in userdata:  # 查询字典
            if  username == x['username'] and password == x['password'] :
                if register_form.is_valid():
                    # 登录成功
                    global username_logined
                    username_logined = x['username']
                    context['user'] = x['username']
                    return render(request, 'index.html', {'result': context } )
                else:result['error'] = '验证码错误！'
                return render(request, 'login.html', {'result': result, 'register_form': RegisterForm()})
                break
        result['error'] = '账号密码错误！'
        return render(request, 'login.html', {'result': result,'register_form': RegisterForm()})

def minsheng_submit(request):
    submit_info = minsheng()
    submit_info.street = request.POST.get('street')
    submit_info.community = request.POST.get('community')
    submit_info.type = request.POST.get('problem')
    submit_info.phone_num = request.POST.get('phone_num')
    submit_info.detail = request.POST.get('detail')
    submit_info.status = 0  # 未结办
    submit_info.save()
    return render(request, 'Submit_succes.html', {'danhao':submit_info.id+1000})

def minsheng_query(request):
    data = minsheng.objects.values()
    danhao = request.GET.get('id')
    for x in data :
        tmp = int(danhao)-1000
        if(x['id'] == tmp ):
            if x['status'] == '0':
                ans = '未处理'
            else:
                ans = '已处理'
        else:
            ans = '查无此单号'
    return render(request, 'quiry_result.html', {'ans':ans, 'danhao':danhao})

def minsheng_query_phone_num(request):
    data = minsheng.objects.values()
    phone_num = request.GET.get('phone')
    for x in data :
        if(x['phone_num'] == phone_num ):
            if x['status'] == '0':
                ans = '未处理'
                danhao = x['id']+1000
                break
            else:
                ans = '已处理'
                danhao = x['id']+1000
                break
        else:
            ans = '查无此手机号'
            danhao = '无'
    return render(request, 'quiry_result.html', {'ans':ans, 'danhao':danhao})
