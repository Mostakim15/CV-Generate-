from django.db import models

# Create your models here.
class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True, null=True)
    summary = models.TextField()
    address = models.TextField()
    education = models.TextField()
    certifications = models.TextField()
    projects = models.TextField()
    experience = models.TextField()
    skills = models.TextField(choices=[
        ("Basic", "Basic"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ], max_length=50, default="Basic")

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CVs'