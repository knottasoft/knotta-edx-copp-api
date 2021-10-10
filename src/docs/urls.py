from rest_framework.routers import SimpleRouter

from .views import DocumentViewset, DocumentTypeViewset

docs_router = SimpleRouter()

docs_router.register(r'docs', DocumentViewset)
docs_router.register(r'docTypes', DocumentTypeViewset)