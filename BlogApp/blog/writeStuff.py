from django.conf import settings
settings.configure()

from models import Data
from django.contrib.auth.models import User
from random import randint

me = User.objects.get(username='cxd')
for i in range(0,10):
    # Data.objects.create(author = me , income = randint(100,10000))
    print("hey da bin ich")



