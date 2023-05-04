from django.shortcuts import render
import pandas as pd
import pickle
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import StudyPlan, PredictionResult
from rest_framework.decorators import api_view
from joblib import load
from django.http import JsonResponse





@api_view(['POST'])
def upload_study_plan(request):
    # Step 1: Extract uploaded file and read data into dataframe
    file = request.FILES['study_plan']
    df = pd.read_csv(file)

    # Step 2: Clean and preprocess data
    # ... (code to clean and preprocess dataframe)

    # Step 3: Load pre-trained machine learning model
    model = joblib.load('path/to/pretrained/model.pkl')

    # Step 4: Use model to make predictions
    X = df.drop(['user_id'], axis=1)  # drop user_id column
    predictions = model.predict(X)

    # Step 5: Save study plan data to database
    user_id = request.user.id  # or however you get the user id
    for i, row in df.iterrows():
        studyplan = StudyPlan(
            studyplan_name=row['studyplan_name'],
            user_id=user_id,
            prediction_result=predictions[i]
        )
        studyplan.save()

    # Step 6: Return JSON response
    return JsonResponse({'success': True, 'message': 'Study plan uploaded successfully.'})

