import http
from django.shortcuts import render,HttpResponseRedirect
#from  crud.forms import Studentregistration
from .forms import StudentregistrationForm
from .models import User
# Create your views here.
#this function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentregistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            fm = StudentregistrationForm()
    else:
        fm = StudentregistrationForm()
    stud = User.objects.all()
    return render(request, 'crud/addandshow.html', {'form':fm,'stu':stud})


#this function will update or edir
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm= StudentregistrationForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
            pi = User.objects.get(pk=id)
            fm= StudentregistrationForm(instance=pi)
    return render(request, 'crud/updatestudent.html',{'form':fm})


#this function delete items
def delete_data(request,id):
    if request.method == 'POST':
        pi =User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')