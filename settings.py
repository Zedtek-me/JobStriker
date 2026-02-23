import os


DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
CAREER_JET_API_URL = os.getenv("CAREER_JET_API_URL", "https://api.careerjet.net/api")