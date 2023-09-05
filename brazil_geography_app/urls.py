from rest_framework.routers import DefaultRouter
from brazil_geography_app.views import StatesViewSet


app_name = 'brazil_geography_app'

router = DefaultRouter(trailing_slash=False)
router.register(r'states', StatesViewSet)

urlpatterns = router.urls
