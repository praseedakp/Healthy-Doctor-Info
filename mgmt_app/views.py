from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib import messages



#index page:
def indexpage(request):
    return render(request,'index.html')

# Create your views here.
def doctorreg(request):
    if request.method=='POST':
        a=doctorforms(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['fname']
            em=a.cleaned_data['dimage']
            ph=a.cleaned_data['email']
            po=a.cleaned_data['phone']
            ge=a.cleaned_data['gender']
            da=a.cleaned_data['date']
            se=a.cleaned_data['select']
            ad=a.cleaned_data['specialization']
            ab=a.cleaned_data['about']
            st=a.cleaned_data['state']
            ar=a.cleaned_data['address']
            b=doctorinfomodel(fname=nm,dimage=em,email=ph,phone=po,gender=ge,date=da,select=se,specialization=ad,about=ab,state=st,address=ar)
            b.save()
            return redirect(fullpaydisplaynew)
        else:
            return HttpResponse("failed....")
    return render(request,'doctorregistration.html')


#display of complete infor:
def fullpaydisplaynew(request):
    f=doctorinfomodel.objects.all()
    id1=[]
    k=[]
    l=[]
    m=[]
    n=[]
    o=[]
    p=[]
    q=[]
    r=[]
    s=[]
    t=[]
    u=[]
    for i in f:
        id2=i.id
        id1.append(id2)
        a=i.fname
        k.append(a)
        b=str(i.dimage).split('/')[-1]
        l.append(b)
        c=i.email
        m.append(c)
        d=i.phone
        n.append(d)
        e=i.gender
        o.append(e)
        g=i.date
        p.append(g)
        h=i.select
        q.append(h)
        j=i.specialization
        r.append(j)
        w=i.about
        s.append(w)
        v=i.state
        t.append(v)
        x=i.address
        u.append(x)
    dt=zip(id1,k,l,m,n,o,p,q,r,s,t,u)
    return render(request,'doctorfulldisplay.html',{'dt':dt})

####delete button:
def deletedetails(request,id):
    s=doctorinfomodel.objects.get(id=id)
    os.remove(str(s.dimage))
    s.delete()
    return redirect(fullpaydisplaynew)

#edit details:
def editdoctors(request,id):
    a=doctorinfomodel.objects.get(id=id)
    im=str(a.dimage).split('/')[-1]
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.specialization=request.POST.get('specialization')
        a.about=request.POST.get('about')
        a.state=request.POST.get('state')
        a.address=request.POST.get('address')
        if request.POST.get('date')=='':
            a.save()
        else:
            a.date=request.POST.get('date')
        if len(request.FILES)!=0:
            if len(a.dimage)>0:
                os.remove(a.dimage.path)
            a.dimage=request.FILES['dimage']
        a.save()
        return redirect(fullpaydisplaynew)
    return render(request,'doctordataedit.html',{'a':a,'im':im})



#single page details:
def singledisplay(request,id):
    a=doctorinfomodel.objects.get(id=id)
    im=str(a.dimage).split('/')[-1]
    return render(request,'singleview.html',{'a':a,'im':im})

#single page for patients:
def singleforpatients(request,id):
    a=doctorinfomodel.objects.get(id=id)
    im=str(a.dimage).split('/')[-1]
    return render(request,'singledoctorpatient.html',{'a':a,'im':im})



###admin login
def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['adminusername']
            password=a.cleaned_data['adminpassw']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(admindashboard)
            else:
                return HttpResponse("Login failed")
    return render(request,'adminlogin.html')


#dashbord:
def admindashboard(request):
    return render(request,'admindashboard.html')


#customer registration:
#registration function
def patientregview(request):
    if request.method=='POST':
        a=customerregform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            un=a.cleaned_data['email']
            em=a.cleaned_data['phone']
            pho=a.cleaned_data['address']
            fi=a.cleaned_data['gender']
            pn=a.cleaned_data['place']
            cp=a.cleaned_data['uname']
            cs=a.cleaned_data['passw']
            cw=a.cleaned_data['cpassw']
            cud=int('101'+str(em))
            if cs==cw:
                b=customerregmodel(fname=fn,lname=ln,email=un,phone=em,address=pho,gender=fi,place=pn,uname=cp,passw=cs,cu_num=cud)
                b.save()
                return redirect(patientloginview)
            else:
                return HttpResponse("failed registration!!!")

    return render(request,'customerreg.html')



# login code:
def patientloginview(request):
    if request.method=='POST':
        s=patientlogin(request.POST)
        if s.is_valid():
            ue=s.cleaned_data['uname']
            pm=s.cleaned_data['passw']
            r=customerregmodel.objects.all()
            for i in r:
                if i.uname==ue and i.passw==pm:
                    request.session['id']=i.id
                    return redirect(patientprofile)
            else:
                return HttpResponse("login failed!!!")
    return render(request,'patientlogin.html')


# profile page display:
def patientprofile(request):
    try:
        id1=request.session['id']
        a=customerregmodel.objects.get(id=id1)
        return render(request,'patientprofile.html',{'a':a})
    except:
        return redirect(patientloginview)


#def deletedetails(request,id):
    # s=doctorinfomodel.objects.get(id=id)
    # os.remove(str(s.dimage))
    # s.delete()
    # return redirect(fullpaydisplaynew)

#edit details:
def editpatient(request,id):
    a=customerregmodel.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get('lname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.address=request.POST.get('address')
        a.place=request.POST.get('place')
        a.uname=request.POST.get('uname')
        a.save()
        return redirect(patientprofile)
    return render(request,'patientedit.html',{'a':a})


# logout:after login the page want to logout use this function
def logout_view(request):
    logout(request)
    return redirect(patientloginview)


#for customers
def displaydoctorspatients(request):
    a=doctorinfomodel.objects.all()
    id1=[]
    k=[]
    l=[]
    m=[]
    n=[]
    q=[]
    r=[]
    s=[]
    t=[]
    u=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        a=i.fname
        k.append(a)
        b=str(i.dimage).split('/')[-1]
        l.append(b)
        c=i.email
        m.append(c)
        d=i.phone
        n.append(d)
        h=i.select
        q.append(h)
        j=i.specialization
        r.append(j)
        w=i.about
        s.append(w)
        v=i.state
        t.append(v)
        x=i.address
        u.append(x)
    ct=zip(id1,k,l,m,n,q,r,s,t,u)
    return render(request,'doctordisppatient.html',{'ct':ct})

#diseases model new:

def diseasesupload(request):
    if request.method=='POST':
        a=newdiseasesform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['dname']
            em=a.cleaned_data['image']
            ph=a.cleaned_data['symtom']
            po=a.cleaned_data['remedy']
            b=newdiseasesmodel(dname=nm,image=em,symtom=ph,remedy=po)
            b.save()
            return redirect(displaynewdisease)
        else:
            return HttpResponse("failed....")
    return render(request,'newdiseasesupload.html')


#display the newdisease for admin:
def displaynewdisease(request):
    a=newdiseasesmodel.objects.all()
    id1=[]
    k=[]
    l=[]
    m=[]
    n=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        a=i.dname
        k.append(a)
        b=str(i.image).split('/')[-1]
        l.append(b)
        c=i.symtom
        m.append(c)
        d=i.remedy
        n.append(d)
    di=zip(id1,k,l,m,n)
    return render(request,'newdiseasedisplay.html',{'di':di})

# ####delete button:
def deletenewdisease(request,id):
    s=newdiseasesmodel.objects.get(id=id)
    os.remove(str(s.image))
    s.delete()
    return redirect(displaynewdisease)

#edit details of newdisease:
def editnewdisease(request,id):
    a=newdiseasesmodel.objects.get(id=id)
    im=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.dname=request.POST.get('dname')
        a.symtom=request.POST.get('symtom')
        a.remedy=request.POST.get('remedy')
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.save()
        return redirect(displaynewdisease)
    return render(request,'newdiseaseedit.html',{'a':a,'im':im})



#display for patients:
def dispnewdiseasepatient(request):
    a=newdiseasesmodel.objects.all()
    id1=[]
    k=[]
    l=[]
    m=[]
    n=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        a=i.dname
        k.append(a)
        b=str(i.image).split('/')[-1]
        l.append(b)
        c=i.symtom
        m.append(c)
        d=i.remedy
        n.append(d)
    pi=zip(id1,k,l,m,n)
    return render(request,'newdiseasedisppatient.html',{'pi':pi})


#single page details:for patients
def singledispdisease(request,id):
    a=newdiseasesmodel.objects.get(id=id)
    im=str(a.image).split('/')[-1]
    return render(request,'singleviewdisease.html',{'a':a,'im':im})


#livesessions:for admin
def displaylivedoctors(request):
    a=doctorinfomodel.objects.all()
    id1 = []
    k = []
    l = []
    m = []
    n=[]
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    for i in a:
        id2 = i.id
        id1.append(id2)
        a = i.fname
        k.append(a)
        b = str(i.dimage).split('/')[-1]
        l.append(b)
        c = i.email
        m.append(c)
        d = i.phone
        n.append(d)
        h = i.select
        q.append(h)
        j = i.specialization
        r.append(j)
        w = i.about
        s.append(w)
        v = i.state
        t.append(v)
        x = i.address
        u.append(x)
    li=zip(id1,k,l,m,n,q,r,s,t,u)
    return render(request,'doctorlivedisp.html',{'li':li})



#doctor live for patients:
def displaylivepatient(request):
    a=doctorinfomodel.objects.all()
    id1=[]
    k = []
    l = []
    m = []
    n = []
    q = []
    r = []
    s = []
    t = []
    u = []
    for i in a:
        id2 = i.id
        id1.append(id2)
        a = i.fname
        k.append(a)
        b = str(i.dimage).split('/')[-1]
        l.append(b)
        c = i.email
        m.append(c)
        d = i.phone
        n.append(d)
        h = i.select
        q.append(h)
        j = i.specialization
        r.append(j)
        w = i.about
        s.append(w)
        v = i.state
        t.append(v)
        x = i.address
        u.append(x)
    pa=zip(id1,k,l,m,n,q,r,s,t,u)
    return render(request,'doctorlivepatient.html',{'pa':pa})


#add questions:
def patientquestions(request):
    if request.method=='POST':
        a=questionsform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['pname']
            em=a.cleaned_data['age']
            ph=a.cleaned_data['place']
            po=a.cleaned_data['quest']
            b=questionsmodel(pname=nm,age=em,place=ph,quest=po)
            b.save()
            return redirect(dispques)
        else:
            return HttpResponse("failed....")
    return render(request,'questions.html')

#view the questions for admin and patient
def dispques(request):
    h=questionsmodel.objects.all()
    return render(request,'questionspatientdisp.html',{'h':h})



#delete the questions:
def deletequestions(request,id):
    f=questionsmodel.objects.get(id=id)
    f.delete()
    return redirect(dispques)


#edit the questions by patients:
def editquestions(request,id):
    a=questionsmodel.objects.get(id=id)
    if request.method =='POST':
        a.pname=request.POST.get('pname')
        a.age=request.POST.get('age')
        a.place=request.POST.get('place')
        a.quest=request.POST.get('quest')
        a.save()
        return redirect(dispques)
    return render(request,'questionsedit.html',{'a': a})


#view the questions for admin:
def dispquesadmin(request):
    j=questionsmodel.objects.all()
    return render(request,'questionsadmindisp.html',{'j':j})




#answer from admin and view
def answersquest(request):
    if request.method=='POST':
        a=answerforms(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['diname']
            em=a.cleaned_data['explanation']
            ph=a.cleaned_data['remedy']
            b=answermodel(diname=nm,explanation=em,remedy=ph)
            b.save()
            return redirect(dispanswersadmin)
        else:
            return HttpResponse("failed....")
    return render(request,'answerupload.html')

#display the answers for admin:
def dispanswersadmin(request):
    a=answermodel.objects.all()
    return render(request,'answeradmindisp.html',{'a':a})


#edit the answers:
def editanswers(request,id):
    a=answermodel.objects.get(id=id)
    if request.method =='POST':
        a.diname=request.POST.get('diname')
        a.explanation=request.POST.get('explanation')
        a.remedy=request.POST.get('remedy')
        a.save()
        return redirect(dispanswersadmin)
    return render(request,'answersedit.html',{'a': a})


#delete answers:
def deleteanswers(request,id):
    f=answermodel.objects.get(id=id)
    f.delete()
    return redirect(dispanswersadmin)


#patient answers display:
def answerspatientdisp(request):
    g=answermodel.objects.all()
    return render(request,'answerspatientdisp.html',{'g':g})

#comments add delete and edit:
def commentsupload(request):
    if request.method=='POST':
        a=commentsform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['cname']
            em=a.cleaned_data['comment']
            b=commentsmodel(cname=nm,comment=em)
            b.save()
            return redirect(commentsdisplay)
        else:
            return HttpResponse("failed....")
    return render(request,'patientcommentupload.html')


#comments display
def commentsdisplay(request):
    d=commentsmodel.objects.all()
    return render(request,'commentsdisplay.html',{'d':d})

#comments edit:
def editcomments(request,id):
    a=commentsmodel.objects.get(id=id)
    if request.method =='POST':
        a.cname=request.POST.get('cname')
        a.comment=request.POST.get('comment')
        a.save()
        return redirect(commentsdisplay)
    return render(request,'commentedit.html',{'a': a})


#delete comments:
def deletecomments(request,id):
    f=commentsmodel.objects.get(id=id)
    f.delete()
    return redirect(commentsdisplay)


#comments display for admin
def commentsdisplayadmin(request):
    a=commentsmodel.objects.all()
    return render(request,'commentsdisplayadmin.html',{'a':a})



#about us:
def aboutus(request):
    return render(request,'aboutus.html')

#contact us:
def contactus(request):
    return render(request,'contactus.html')


#hospital uploads
def uploadhospital(request):
    if request.method=='POST':
        a=hospitalforms(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['hname']
            em=a.cleaned_data['lname']
            ph=a.cleaned_data['himage']
            po=a.cleaned_data['about']
            b=hospitalmodel(hname=nm,lname=em,himage=ph,about=po)
            b.save()
            return redirect(displayhospital)
        else:
            return HttpResponse("failed....")
    return render(request,'newhospitalup.html')

#display the hosptals:
def displayhospital(request):
    a=hospitalmodel.objects.all()
    id1=[]
    k=[]
    m=[]
    l=[]
    n=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        a=i.hname
        k.append(a)
        c=i.lname
        m.append(c)
        b=str(i.himage).split('/')[-1]
        l.append(b)
        d=i.about
        n.append(d)
    ht=zip(id1,k,l,m,n)
    return render(request,'hospitaladmindisplay.html',{'ht':ht})



# ####delete hospital:
def deletehospitals(request,id):
    s=hospitalmodel.objects.get(id=id)
    os.remove(str(s.himage))
    s.delete()
    return redirect(displayhospital)

#edit details of newdisease:
def edithospitals(request,id):
    a=hospitalmodel.objects.get(id=id)
    im=str(a.himage).split('/')[-1]
    if request.method=='POST':
        a.hname=request.POST.get('hname')
        a.lname=request.POST.get('lname')
        a.about=request.POST.get('about')
        if len(request.FILES)!=0:
            if len(a.himage)>0:
                os.remove(a.himage.path)
            a.himage=request.FILES['himage']
        a.save()
        return redirect(displayhospital)
    return render(request,'hospitaledit.html',{'a':a,'im':im})








#display the hosptals for patients:
def disppatienthos(request):
    a=hospitalmodel.objects.all()
    id1=[]
    k=[]
    m=[]
    l=[]
    n=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        a=i.hname
        k.append(a)
        c=i.lname
        m.append(c)
        b=str(i.himage).split('/')[-1]
        l.append(b)
        d=i.about
        n.append(d)
    ph=zip(id1,k,l,m,n)
    return render(request,'hospatientdisplay.html',{'ph':ph})

