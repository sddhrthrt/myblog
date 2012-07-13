import os
import sys

sys.path = ['/srv/www/myblog']+sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
