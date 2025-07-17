from django.shortcuts import render, redirect
from cv_app_1.models import CV
from django.contrib import messages


# Create your views here.
def home(request):
    """Render the home page."""
    if request.method == 'POST':
        name = request.POST.get('name',)
        email = request.POST.get('email',)
        phone = request.POST.get('phone',) 
        image = request.FILES.get('image',)
        summary = request.POST.get('summary',)
        address = request.POST.get('address',)
        education = request.POST.get('education',)
        certifications = request.POST.get('certifications',)
        projects = request.POST.get('projects',)
        experience = request.POST.get('experience',)
        skills = request.POST.get('skills',)

        if name:
            cv = CV.objects.create(
                name=name,
                email=email,
                phone=phone,
                image=image,
                summary=summary,
                address=address,
                education=education,
                certifications=certifications,
                projects=projects,
                experience=experience,
                skills=skills
            )
            cv.save()
            messages.success(request, "CV created successfully!")
            return redirect('show')

        else:
            messages.error(request, "Please fill in all required fields.")
    return render(request, 'home/home.html')