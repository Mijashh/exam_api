from django.db import models


class ExamIndex(models.Model):
    name = models.CharField(max_length=200)
    
    university = models.CharField(max_length=100)
    date=models.DateField()
    slug=models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
    

class ExamDetails(models.Model):
    index=models.ForeignKey(ExamIndex,on_delete=models.CASCADE)
    description=models.TextField()
    syallabus=models.TextField()
    eligibility=models.TextField()
    official_website=models.URLField()
    courses_offered=models.TextField()
    # model_papers=models.FileField(upload_to="static/Exam_Details/Model_Papers")
    def __str__(self):
        return self.index.name