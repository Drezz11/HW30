from django.urls import path
from rest_framework import routers

from ads.views.selection import *

urlpatterns = []
router = routers.SimpleRouter()
router.register('', SelectionViewSet)

urlpatterns += router.urls