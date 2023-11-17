from django import forms

#regform:
class doctorforms(forms.Form):
    fname=forms.CharField(max_length=50)
    dimage=forms.FileField()
    email=forms.EmailField()
    phone=forms.IntegerField()
    gender=forms.CharField(max_length=10)
    date=forms.DateField()
    select=forms.CharField(max_length=50)
    specialization=forms.CharField(max_length=250)
    about=forms.CharField(max_length=500)
    state=forms.CharField(max_length=100)
    address=forms.CharField(max_length=250)


#admin login:
# forms of admin page:
class adminform(forms.Form):
    adminusername=forms.CharField(max_length=50)
    adminpassw=forms.CharField(max_length=50)


#forms for customer
class customerregform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=500)
    gender=forms.CharField(max_length=20)
    place=forms.CharField(max_length=100)
    uname=forms.CharField(max_length=50)
    passw=forms.CharField(max_length=30)
    cpassw=forms.CharField(max_length=30)


#login:
# loginform here:
class patientlogin(forms.Form):
    uname=forms.CharField(max_length=50)
    passw=forms.CharField(max_length=50)

#newdiseases forms:

class newdiseasesform(forms.Form):
    dname=forms.CharField(max_length=100)
    image=forms.FileField()
    symtom=forms.CharField(max_length=500)
    remedy=forms.CharField(max_length=600)



#questions from patients:
class questionsform(forms.Form):
    pname=forms.CharField(max_length=50)
    age=forms.IntegerField()
    place=forms.CharField(max_length=50)
    quest=forms.CharField(max_length=500)


#form for comments:
class commentsform(forms.Form):
    cname=forms.CharField(max_length=100)
    comment=forms.CharField(max_length=250)


#forms for answers:

class answerforms(forms.Form):
    diname=forms.CharField(max_length=100)
    explanation=forms.CharField(max_length=1000)
    remedy=forms.CharField(max_length=500)

#forms for hospital:
class hospitalforms(forms.Form):
    hname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=100)
    himage=forms.FileField()
    about=forms.CharField(max_length=600)
