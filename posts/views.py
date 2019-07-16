from django.shortcuts import render
from .forms import PostForm
from .models import Posts
from django.contrib import messages
# Create your views here.
# def add_post(request):
#     form=PostForm(request.POST or None,request.FILES or None)
#     if form.is_valid():
#         form.save()
#
#
#
#     context={
#         'form':form
#     }
#
#
#     return render(request,'addpost.html',context)


def add_post(request):

    mes=""
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        p=Posts()
        p.title=title
        p.desc=desc
        #p=Posts(title=title,desc=desc)

        #Posts.objects.create(title=title1,desc=desc)
        p.save()
        print("form saved successfully")
        messages.success(request,'form save successfully')


    # if 'delete' in request.POST:
    #     pass
    #
    # if 'add' in request.POST:
    #     pass
    #     mes='form save ho gya'
    # context={
    #     'mes':mes
    # }


    return render(request,'addpost.html',)



def showpost(request):
    #p=Posts.objects.all()
    p=Posts.objects.all().order_by('-id')
    #p=Posts.objects.all().order_by('-pk') (primary key)

    #p=Posts.objects.all()[0]
    #p=Posts.objects.first()
    #p=Posts.objects.last()


    context={
        'p':p
    }
    return  render(request,'showpost.html',context)











