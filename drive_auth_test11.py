import os
import io
import pandas as pd
from PyPDF2 import PdfReader
from pptx import Presentation
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_drive():
    scope = ['https://www.googleapis.com/auth/drive.readonly']
    

    SERVICE_ACCOUNT_PATH = r"C:\Users\selvi\Downloads\Streamlit-bot\familytlc-chatbot-5b74c357eb87.json"
    
    if not os.path.exists(SERVICE_ACCOUNT_PATH):
        raise FileNotFoundError(f"❌ Service account file not found: {SERVICE_ACCOUNT_PATH}")

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_PATH,
        scopes=scope
    )
    
    service = build('drive', 'v3', credentials=creds)
    return service
