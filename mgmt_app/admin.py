from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(doctorinfomodel)
admin.site.register(customerregmodel)
admin.site.register(newdiseasesmodel)
admin.site.register(questionsmodel)
admin.site.register(answermodel)
admin.site.register(commentsmodel)
admin.site.register(hospitalmodel)