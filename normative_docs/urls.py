from rest_framework import routers
from normative_docs.api import (
    BoltAreaViewSet,
    ResCrushingViewSet,
    ResShearViewSet,
    StallMarkViewSet
)

API_V1 = 'api'

router = routers.DefaultRouter()
router.register(f'{API_V1}/bolt', BoltAreaViewSet, 'bolt_area')
router.register(f'{API_V1}/rescrush', ResCrushingViewSet, 'resistance_crush')
router.register(f'{API_V1}/resshear', ResShearViewSet, 'resistance_shear')
router.register(f'{API_V1}/stall', StallMarkViewSet, 'stall_mark')

urlpatterns = router.urls
