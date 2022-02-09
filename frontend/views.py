from django.shortcuts import redirect, render
from .forms import UserCreationForm,KeyWordForm
from django.contrib.auth.models import User
from api.models import keyword

# Create your views here.
def home(request):
    context=dict()
    userForm=UserCreationForm()
    keyForm=KeyWordForm()
    context['userForm']=userForm
    context['keyForm']=keyForm
    context['user']=User.objects.all()
    context['key']=keyword.objects.all()
    return render(request,'index.html',context=context)

def insert_key(request):
    if(request.method == "POST"):
        form=KeyWordForm(request.POST)
        if(form.is_valid()):
            obj=form.save(commit=False)
            obj.save()
            return redirect('/')