# app.py
from config import PERMISSIONS, APPS, DIRECTORIES, CNN_CONSTANTS

# Check if user has permission to access app1
if 'app1' in PERMISSIONS['user']:
    print("User has access to app1")
else:
    print("User does not have access to app1")

# Use CNN constants
image_size = CNN_CONSTANTS['IMAGE_SIZE']
print("Image size:", image_size)
