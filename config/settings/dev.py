from .base import *

DEBUG = True

# Option A (simple, clean)
#ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

#Option B (more dynamic)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")