import firebase_admin
from firebase_admin import credentials, db as firebase_db
import os
from datetime import datetime
from app.core.config import settings

current_dir = os.path.dirname(__file__)

service_account_path = os.path.join(current_dir, "../../serviceAccountKey.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': settings.firebase_database_url
    })

def add_chat_message(session_id, role, content):
    try:
        ref = firebase_db.reference(f'chat_sessions/{session_id}/messages')
        new_message_ref = ref.push({
            'role': role,
            'content': content,
            'timestamp': datetime.utcnow().isoformat()
        })
        return new_message_ref.key
    except Exception as e:
        return None
