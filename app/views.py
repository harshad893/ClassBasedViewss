from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.
# FBV for returning string
from app.forms import *

def fbv_string(request):
    return HttpResponse('This FBV string')

# CBV for returning string
class Cbv_string(View):
    def get(self,request):
        return HttpResponse('this CBV string')

# FBV for returning HTML page
def fbv_template(request):
    d={'name':'Ashu'}
    return render(request,'fbv_template.html',d)

# CBV for returning HTML page
class Cbv_template(View):
    def get(self,request):
        d={'name':'Nikky'}
        return render(request,'Cbv_template.html',d)

# forms with FBv

def fbv_form(request):
    form=NameForm()
    if request.method=='POST':
        fd=NameForm(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))
    return render(request,'fbv_form.html',context={'form':form})

# forms with Class Based View
class Cbv_form(View):
    def get(self,request):
        form=NameForm()
        return render(request,'Cbv_form.html',context={'form':form})
    
    def post(self,request):
        fd=NameForm(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))


#rendering HTML with TEmplateView

class Cbv(TemplateView):
    template_name='Cbv_template.html'
