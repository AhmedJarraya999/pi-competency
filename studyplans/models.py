from django.db import models
from django.contrib.auth.models import User

class StudyPlan(models.Model):
    csv_file = models.FileField(upload_to='study_plans')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prediction_result = models.CharField(max_length=255)

    def __str__(self):
        return f"Study Plan {self.id} for {self.user.username}"
