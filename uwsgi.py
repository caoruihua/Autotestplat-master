import os
import sys

# 将系统的编码设置为UTF8
from imp import reload

reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Autotestplat-master.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()