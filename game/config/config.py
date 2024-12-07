import os
class Connection:
    REDIRECT_URI = "https://your-production-url.onrender.com/spotify_callback" if 'RENDER' in os.environ else "https://your-production-url.com/spotify_callback"
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")