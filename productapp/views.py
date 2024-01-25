from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self, request):
        return render(request,'productinput.html')

class InsertView(View):
    def get(self, request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        resp=HttpResponse("product insert sucessfully")
        return resp

class DisplayView(View):
    def get(self, request):
        qs=Product.objects.all()
        con_dict={"pro":qs}
        return render(request,'display.html',con_dict)

class UpdateInput(View):
    def get(self, request):
        return render(request,'updateinput.html')

class UpdateView(View):
    def post(self, request):
        p_id = int(request.POST["t1"])
        p_name = request.POST["t2"]
        p_cost = float(request.POST["t3"])
        p_mfdt = request.POST["t4"]
        p_expdt = request.POST["t5"]
        prod=Product.objects.get(pid=p_id)
        prod.pname=p_name
        prod.pcost=p_cost
        prod.pmfdt=p_mfdt
        prod.pexpdt=p_expdt
        prod.save()
        resp=HttpResponse("product updates successfully")
        return resp

class DeleteInput(View):
    def get(self, request):
        return render(request,'deleteinput.html')

class DeleteView(View):
    def get(self, request):
        p_id=int(request.GET["t1"])
        prod=Product.objects.filter(pid=p_id)
        prod.delete()
        resp=HttpResponse("Product deleted successfully")
        return resp
