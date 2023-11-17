from django.urls import path
from .views import *

urlpatterns=[
    path('index/', indexpage),
    path('doctorregistration/',doctorreg),
    path('displaydoctors/',fullpaydisplaynew),
    path('deletedetails/<int:id>',deletedetails),
    path('detailsview/<int:id>',singledisplay),
    path('adminlogin/',adminlogin),
    path('admindashboard/',admindashboard),
    path('editdetails/<int:id>',editdoctors),
    path('patientregview/',patientregview),
    path('patientloginview/',patientloginview),
    path('patientprofile/',patientprofile),
    path('patientedit/<int:id>',editpatient),
    path('logout_view/',logout_view),
    path('doctorspatientdisplay/',displaydoctorspatients),
    path('singleforpatients/<int:id>',singleforpatients),
    path('diseasesupload/',diseasesupload),
    path('displaynewdisease/',displaynewdisease),
    path('deletenewdisease/<int:id>',deletenewdisease),
    path('editnewdisease/<int:id>',editnewdisease),
    path('dispnewdiseasepatient/',dispnewdiseasepatient),
    path('singledispdisease/<int:id>',singledispdisease),
    path('displaylivedoctors/',displaylivedoctors),
    path('displaylivepatient/',displaylivepatient),
    path('patientquestions/',patientquestions),
    path('dispquestions/',dispques),
    path('deletequest/<int:id>',deletequestions),
    path('editquest/<int:id>',editquestions),
    path('dispquesadmin/',dispquesadmin),
    path('answersquestions/',answersquest),
    path('dispanswersadmin/',dispanswersadmin),
    path('editanswers/<int:id>',editanswers),
    path('deleteanswers/<int:id>',deleteanswers),
    path('answerspatientdis/',answerspatientdisp),
    path('commentsupload/',commentsupload),
    path('commentsdisplay/',commentsdisplay),
    path('editcomments/<int:id>',editcomments),
    path('deletecomments/<int:id>',deletecomments),
    path('commentsdisplayadmin/',commentsdisplayadmin),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path('uploadhospital/',uploadhospital),
    path('displayhospital/',displayhospital),
    path('deletehospitals/<int:id>',deletehospitals),
    path('edithospitals/<int:id>',edithospitals),
    path('disppatienthos/',disppatienthos),


]