import json
import os

fp = os.getenv('GOOGLE_CREDS_FILENAME')
if fp:
    with open(fp, "w") as f:
        json.dump({
            'type': os.getenv('TYPE'),
            'project_id': os.getenv('PROJECT_ID'),
            'private_key_id': os.getenv('PRIVATE_KEY_ID'),
            'private_key': os.getenv('PRIVATE_KEY'),
            'client_email': os.getenv('CLIENT_EMAIL'),
            'client_id': os.getenv('CLIENT_ID'),
            'auth_uri': os.getenv('AUTH_URI'),
            'token_uri': os.getenv('TOKEN_URI'),
            'auth_provider_x509_cert_url': os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
            'client_x509_cert_url': os.getenv('CLIENT_X509_CERT_URL')
        }, f)


from app import app

app.run(port=5000)

# To Run:
# python run.py
# or
# python -m flask run
