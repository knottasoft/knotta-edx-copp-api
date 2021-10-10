from rest_framework.routers import SimpleRouter

from .views import FilesViewset

files_router = SimpleRouter()

files_router.register(r'files', FilesViewset)
#files_router.register(r'files', FileDetail.as_view(), basename='File')

#urlpatterns = files_router.urls
