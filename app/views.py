from django.shortcuts import render

# Create your views here.


# Create your views here.
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def update(request):
    try:
        if request.method == 'POST':
           
            user = Data(id=request.POST['id1'],name=request.POST['name'], department=request.POST['department'],  dob=request.POST['dob'], address=request.POST['address'], others=request.POST['others'],gender=request.POST['gender'])
            user.save()
            return redirect('form_view')
    except:
        pass

    data = Data.objects.all().values().order_by('-id')
    return render(request, 'form.html', {'data': data})
def formview(request):
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})
def delete(request):
    try:
        employee = Data.objects.get(id=request.POST['id1'])
        print(employee.dob.year)
        employee.delete()
        data = Data.objects.all().values().order_by('-id')
        return render(request, 'form.html', {'data': data})
    except:
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})
def up(request):
    try:
        employee = Data.objects.get(id=request.POST['id1'])
        new_value = request.POST.get('value')
        print(new_value)
        setattr(employee, request.POST['field'], new_value)
        employee.save()
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})
    except:
        data=Data.objects.all().values().order_by('-id')
        return render(request,'form.html',{'data':data})

def tables(request):
    data = Data.objects.all().values().order_by('-id')
    return render(request, 'tables.html', {'data': data})
def delete2(request):
    try:
        employee = Data.objects.get(id=request.POST['id1'])
        print(employee.dob.year)
        employee.delete()
        data = Data.objects.all().values().order_by('-id')
        return render(request, 'tables.html', {'data': data})
    except:
        data=Data.objects.all().values().order_by('-id')
        return render(request,'tables.html',{'data':data})
    #  dob_date = datetime.strptime(request.POST['dob'], '%Y-%m-%d')