from django.db import models

# Create your models here.
#doctor registration:
class doctorinfomodel(models.Model):
    choice=[('MBBS','MBBS'),
            ('MD','MD'),
            ('MS','MS'),
            ('BAMS','BAMS'),
            ('BHMS','BHMS')
            ]
    fname=models.CharField(max_length=50)
    dimage=models.FileField(upload_to='mgmt_app/static')
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    date=models.DateField()
    select=models.CharField(max_length=50,choices=choice)
    specialization=models.CharField(max_length=250)
    about=models.CharField(max_length=500)
    state=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    def __str__(self):
        return self.fname


#customer registration:
class customerregmodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=100)
    uname=models.CharField(max_length=50)
    passw=models.CharField(max_length=30)
    cu_num=models.IntegerField()

#for token:cu_num

#newdiseasemodel:
class newdiseasesmodel(models.Model):
    dname=models.CharField(max_length=100)
    image=models.FileField(upload_to='mgmt_app/static')
    symtom=models.CharField(max_length=500)
    remedy=models.CharField(max_length=600)



#ask questions:
class questionsmodel(models.Model):
    pname=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=50)
    quest=models.CharField(max_length=500)


#model for answer:
class answermodel(models.Model):
    diname=models.CharField(max_length=100)
    explanation=models.CharField(max_length=1000)
    remedy=models.CharField(max_length=500)


#comments models:
class commentsmodel(models.Model):
    cname=models.CharField(max_length=100)
    comment=models.CharField(max_length=250)

#hospital model:
class hospitalmodel(models.Model):
    hname=models.CharField(max_length=50)
    lname=models.CharField(max_length=100)
    himage=models.FileField(upload_to='mgmt_app/static')
    about=models.CharField(max_length=600)
