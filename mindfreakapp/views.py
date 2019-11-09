from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from mindfreakapp.models import Quiz,Content
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        exists = User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(email=email, username=username, password=password)
            return redirect("/")
        else:
            return render(request, "signup.html",{"error":"User already exists"})
    
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, "signin.html")

@login_required(login_url="/login")
def signout(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login")
def contentpage(request,level="all"):
    if level == "all":
        Allcontent = Content.objects.all()
    else:
        Allcontent = Content.objects.filter(level=level)
    return render(request, "contentpage.html",{"Allcontent":Allcontent})

@login_required(login_url="/login")
def addcontent(request):
    if request.method == "POST":
        print(request.POST.keys())
        subject = request.POST["subject"]
        topicname = request.POST["topicname"]
        description = request.POST["description"]
        level = request.POST["level"]
        link = request.POST["link"]
        Addcontent = Content.objects.create(user=request.user,subject=subject, topicname=topicname, description=description, level=level, link=link)
        return redirect("/contentpage/")
       
    return render(request, "addcontent.html")

@login_required(login_url="/login")
def quizpage(request,level="all"):
    if request.method == "POST":
        anslist =[]
        if level == "all":
            Allquiz = Quiz.objects.all()
        else:
            Allquiz = Quiz.objects.filter(level=level)
        for i in range(len(Allquiz)):
            ans = request.POST.get('q'+str(i))
            qname = Allquiz[i].questiontitle
            corans = Allquiz[i].correctans
            if ans!= corans:
                anslist.append(['false',corans, Allquiz[i].description,ans])
            else:
                anslist.append(['true',corans, Allquiz[i].description,ans])
        li=[i for i in range(len(Allquiz))]
        return render(request, "quizpage.html",{"done":2,"Allquiz":zip(Allquiz,li,anslist)})
    else:
        if level == "all":
            Allquiz = Quiz.objects.all()
        else:
            Allquiz = Quiz.objects.filter(level=level)
        li=[i for i in range(len(Allquiz))]
        return render(request, "quizpage.html",{"done":1,"Allquiz":zip(Allquiz,li)})

@login_required(login_url="/login")
def addquiz(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        questiontitle = request.POST["question"]
        option1 = request.POST["option1"]
        option2 = request.POST["option2"]
        option3 = request.POST["option3"]
        option4 = request.POST["option4"]
        correctans = request.POST["correctans"]
        description = request.POST["description"]
        level = request.POST["level"].lower()
        Addquiz = Quiz.objects.create(user=request.user,questiontitle=questiontitle, subject=subject, option1=option1, option2 =option2, option3=option3, option4 =option4, correctans=correctans,  level=level, description=description)
        return redirect("/quizpage/")
       
    return render(request, "addquiz.html")