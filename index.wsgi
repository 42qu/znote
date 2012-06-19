import sae
from application import application
application = sae.create_wsgi_app(application)
