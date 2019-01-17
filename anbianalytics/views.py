
from django.shortcuts import render


def     homepage( request):
            return render(request,'home.html')

def   submit(request):
            data=request.GET['dname']
            data1=request.GET['ename']

            return render(request,'input.html',{'dn':data,'dn1':data1})
            
