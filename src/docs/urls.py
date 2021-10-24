from rest_framework.routers import SimpleRouter

from .views import DocumentViewset, DocumentTypeViewset, CourseRunDocTypeViewset

docs_router = SimpleRouter()

docs_router.register(r'docs', DocumentViewset)
docs_router.register(r'docTypes', DocumentTypeViewset)
docs_router.register(r'courseRunDocTypes', CourseRunDocTypeViewset)