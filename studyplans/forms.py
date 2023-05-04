from django import forms

class StudyPlanUploadForm(forms.Form):
    study_plan_file = forms.FileField()
