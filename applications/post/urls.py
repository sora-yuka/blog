from django.urls import path, include
from applications.post.views import PostAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PostAPIView)

urlpatterns = [
    # path('', PostAPIView.as_view({'get': 'list', 'post': 'create'})),
    # path('', include(router.urls))
]

#* способ написания
urlpatterns += router.urls
