import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def authenticate_drive():
    scope = ['https://www.googleapis.com/auth/drive.readonly']
    
    if "GOOGLE_DRIVE_JSON" not in os.environ:
        raise EnvironmentError("❌ GOOGLE_DRIVE_JSON secret not found.")

    # Load and parse the JSON string from environment
    key_dict = json.loads(os.environ["GOOGLE_DRIVE_JSON"])
    
    creds = service_account.Credentials.from_service_account_info(key_dict, scopes=scope)
    service = build('drive', 'v3', credentials=creds)

    print("✅ Google Drive connected successfully.")
    return service
