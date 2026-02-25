import os
import sys

# Add the project directory to the sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.append(project_path)

# Set the settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()