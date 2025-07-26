import streamlit_authenticator as stauth

credentials = {
    "usernames": {
        "familytlc": {
            "email": "familytlc321@gmail.com",
            "name": "familytlc",
            "password": "familytlc@123"
        }
    }
}
hasher = stauth.Hasher()  # No arguments here
hashed_credentials = hasher.hash_passwords(credentials)

print(hashed_credentials)