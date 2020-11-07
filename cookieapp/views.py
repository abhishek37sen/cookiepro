from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
def create_cookie(request):
    if not request.COOKIES.get('color'):
        respose=HttpResponse("cookies is created")
        respose.set_cookie('color','blue')
        return respose
    else:
         return HttpResponse("your favorite color is {0}".format(request.COOKIES['color']))

def count_cookies(request):
    if not request.COOKIES.get('visits'):
        response=HttpResponse("This is your fist visit Now i will track your visit to this site..")
        response.set_cookie('visits','1')
        return response
    else:
        visits=int(request.COOKIES.get('visits'))+1
        response=HttpResponse("This is Your {0} visit".format(visits))
        response.set_cookie('visits',str(visits))
        return response

def delete_cookie(request):
    if request.COOKIES.get('visits'):
        response=HttpResponse("cookies cleared")
        response.delete_cookie(("visits"))
        return response
    else:
        response=HttpResponse("we ate not tracking your")
        return response