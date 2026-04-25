import requests
import json

def emotion_detector(text_to_analyze):
    # Alamat API Watson
    url = 'https://skills.network'
    
    # Header yang diperlukan API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Data yang dikirim (teks dari user)
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Mengirim permintaan POST
    response = requests.post(url, json = myobj, headers=header)
    
    return response.text
