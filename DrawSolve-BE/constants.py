from dotenv import load_dotenv
import os
load_dotenv()

# SERVER_URL = 'localhost'
# PORT = '8900'
# ENV = 'dev'

SERVER_URL = 'https://draw-solve-ai-be.vercel.app'
PORT = '443'  # Port 443 is standard for HTTPS
ENV = 'production'  # Assuming it's a live environment

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")