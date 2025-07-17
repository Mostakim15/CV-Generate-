from django.shortcuts import render
from cv_app_1.models import CV
# Create your views here.
def show(request):
    cvs = CV.objects.all()
    if request.method == "GET":
        search_query = request.GET.get("Search", "")
        if search_query:
            cvs = cvs.filter(name__icontains=search_query)
    else:
        cvs = CV.objects.all()
    # Render the show template with the list of CVs
    return render(request, 'show/show.html', {'cvs': cvs})