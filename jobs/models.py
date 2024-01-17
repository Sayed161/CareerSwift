from django.db import models
from employee.models import Employee
from job_seeker.models import Job_seeker
from location.models import Location
from category.models import Category
# Create your models here.
JOB_TYPE = [
    ('Full Time','full_time'),
    ('Part-Time','part_time'),
    ('Remote','Remote'),
]



class Jobs(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    industry = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    Job_type = models.CharField(max_length=30,choices = JOB_TYPE,default='Full Time')
    requirements = models.TextField()
    Responsibities = models.TextField(default=None)
    qualifications = models.TextField(default=None)
    Post = models.CharField(max_length=255,default=None)
    salary = models.CharField(max_length=255,default=None)
    Benifits = models.CharField(max_length=255,default=None)
    posted_by = models.OneToOneField(Employee,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default=None)
    def __str__(self) -> str:
        return self.title
    
class JobApplication(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    seeker = models.ForeignKey(Job_seeker, on_delete=models.CASCADE)
    resume = models.TextField(default=None)
    letter = models.TextField()
    applied = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.seeker.user.username