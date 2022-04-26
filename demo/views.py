from email.headerregistry import Address
from multiprocessing import context
#fr om multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
#from scrapy import Item
from .models import emp
from .forms import empform

# Create your views here.
def  home(request):
    k= emp.objects.all()
    c=k.count()
    context={'c':c,}
    return render(request,'demo/base.html',context)
def table(request):
    k= emp.objects.all()
    k=k.values()
    #print(k)
       
    context={'k':k,}
    return render(request,'demo/table.html',context) 
def createe(request):
    
    if request.method =='POST' :
        
        print(request.POST)
        print('name',request.POST.get('name')) 
        print('DOB',request.POST.get('DOB'))
        print('DOJ',request.POST.get('DOJ'))
        print('Department',request.POST.get('Department'))
        print('post',request.POST.get('post'))
        print('Adress',request.POST.get('Adress'))
        print('City',request.POST.get('City'))
        print('Country',request.POST.get('Country'))
        e = emp.objects.create(name = request.POST.get('name'), DOB = request.POST.get('DOB'),DOJ = request.POST.get('DOJ'),Department = request.POST.get('Department'),
        post=request.POST.get('post'),Adress=request.POST.get('Adress'),City=request.POST.get('City'),Country=request.POST.get('Country'))
        return redirect('/')
    return render(request,'demo/create.html')    
    
def updateOrder(request, pk):

	order = emp.objects.get(id=pk)
	form = empform(instance=order)

	if request.method == 'POST':
		form = empform(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/table')

	context = {'form':form}
	return render(request, 'demo/up.html', context)    
def deleteOrder(request, pk):
	order =emp.objects.get(id=pk)
    
	if request.method == "POST":
		order.delete()
		return redirect('/table')

	context = {'item':order}
	return render(request, 'demo/delete.html', context)
from email.headerregistry import Address
from multiprocessing import context
#fr om multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
#from scrapy import Item
from .models import emp
from .forms import empform

# Create your views here.
def  home(request):
    k= emp.objects.all()
    c=k.count()
    context={'c':c,}
    return render(request,'demo/base.html',context)
def table(request):
    k= emp.objects.all()
    k=k.values()
    #print(k)
       
    context={'k':k,}
    return render(request,'demo/table.html',context) 
def createe(request):
    
    if request.method =='POST' :
        
        print(request.POST)
        print('name',request.POST.get('name')) 
        print('DOB',request.POST.get('DOB'))
        print('DOJ',request.POST.get('DOJ'))
        print('Department',request.POST.get('Department'))
        print('post',request.POST.get('post'))
        print('Adress',request.POST.get('Adress'))
        print('City',request.POST.get('City'))
        print('Country',request.POST.get('Country'))
        e = emp.objects.create(name = request.POST.get('name'), DOB = request.POST.get('DOB'),DOJ = request.POST.get('DOJ'),Department = request.POST.get('Department'),
        post=request.POST.get('post'),Adress=request.POST.get('Adress'),City=request.POST.get('City'),Country=request.POST.get('Country'))
        return redirect('/')
    return render(request,'demo/create.html')    
    
def updateOrder(request, pk):

	order = emp.objects.get(id=pk)
	form = empform(instance=order)

	if request.method == 'POST':
		form = empform(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/table')

	context = {'form':form}
	return render(request, 'demo/up.html', context)    
def deleteOrder(request, pk):
	order =emp.objects.get(id=pk)
    
	if request.method == "POST":
		order.delete()
		return redirect('/table')
    
	context = {'item':order}
	return render(request, 'demo/delete.html', context)
def leave(request,pk):
    blog_object=emp.objects.get(id=pk)
    if blog_object.my_field:
        blog_object.my_field = False
    else:
        blog_object.my_field = True
        blog_object. blog_views +=1
       
    blog_object.save()
    return redirect('/table') 
def k(request):
    return render(request, 'demo/ll.html')
