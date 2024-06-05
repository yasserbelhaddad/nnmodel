import logging
from django.shortcuts import render
from rest_framework.decorators import api_view
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
import joblib
import pandas as pd
from .dictionery import boite_encoding, energie_encoding, modele_encoding, marque_encoding

logger = logging.getLogger(__name__)

@api_view(['POST'])
def predict(request):
    scaler = joblib.load('api/modelss/scaler.pkl')
    model = load_model('api/modelss/car_price_predictor.h5')
    input_data = request.data
    logger.info(f"Input data received: {input_data}")

    features = {
        'Kilométrage': input_data.get('Kilométrage'),
        'Année': input_data.get('Année'),
        'MoteurType': input_data.get('MoteurType'),
        'Boite_encoded': boite_encoding.get(input_data.get('Boite_encoded')),
        'Energie_encoded': energie_encoding.get(input_data.get('Energie_encoded')),
        'Modèle_encoded': modele_encoding.get(input_data.get('Modèle_encoded')),
        'Marque_encoded': marque_encoding.get(input_data.get('Marque_encoded')),
    }
    logger.info(f"Extracted features: {features}")

    features_df = pd.DataFrame([features])
    X_new_scaled = scaler.transform(features_df)
    logger.info(f"Scaled data: {X_new_scaled}")

    prediction = model.predict(X_new_scaled)
    logger.info(f"Model prediction: {prediction}")
    print(prediction)

    return render(request, 'prediction.html', {'prediction': prediction})

@api_view(['GET'])
def hello(request):
    return render(request, 'form.html')
