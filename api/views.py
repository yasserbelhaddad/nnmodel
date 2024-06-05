from django.shortcuts import redirect, render
# from django.conf import settings
# Create your views here.
from sklearn.preprocessing import StandardScaler  # Import StandardScaler for data scaling
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from rest_framework.decorators import api_view
from rest_framework.response import Response
from keras.models import load_model
import joblib


import pandas as pd
from .dictionery import (
    boite_encoding,
    energie_encoding,
    modele_encoding,
    marque_encoding
)







@api_view(['POST'])
def predict(request):
    # Load the saved model
    # scaler = joblib.load('api/modelss/scaler.pkl')
    # model = load_model('api/modelss/car_price_predictor.h5')
    # model = joblib.load('api/modelss/modell.pkl')
    # model = settings.model2
    # Get input data from the request body
    scaler = joblib.load('api/modelss/scaler.pkl')
    model = load_model('api/modelss/car_price_predictor.h5')
    input_data = request.data
    
    # Extract features from input data
    features = {
        'Kilométrage': input_data.get('Kilométrage'),
        'Année': input_data.get('Année'),
        'MoteurType': input_data.get('MoteurType'),
        'Boite_encoded': boite_encoding.get(input_data.get('Boite_encoded')),
        'Energie_encoded': energie_encoding.get(input_data.get('Energie_encoded')),
        'Modèle_encoded': modele_encoding.get(input_data.get('Modèle_encoded')),
        'Marque_encoded': marque_encoding.get(input_data.get('Marque_encoded')),
    }
    
    # Convert features to pandas DataFrame for prediction
    features_df = pd.DataFrame([features])
    X_new_scaled = scaler.transform(features_df)
    # Perform prediction
    prediction = model.predict(X_new_scaled)
    return render(request, 'prediction.html', {'prediction': prediction})
    # Return prediction as JSON response
    # return Response({'features_array': features,'prediction':prediction})


    # Render HTML template with prediction result
    # return render(request, 'prediction.html', {'prediction': prediction})
@api_view(['GET'])
def hello(request):
    # Load the saved model
    
    
    return render(request, 'form.html')
    # Return prediction as JSON response
    # return render(request, 'prediction.html', {'prediction': 'hello'})
