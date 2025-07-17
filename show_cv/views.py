from django.shortcuts import render
from cv_app_1.models import CV
# Create your views here.
def show(request):
    cvs = CV.objects.all()
    return render(request, 'show/show.html', {'cvs': cvs})