from ninja import NinjaAPI
from apps.core.api import router as core_router
from apps.blog.api import router as blog_router
from apps.leads.api import router as leads_router


api = NinjaAPI(title="Nonware API", version="1.0.0")

@api.get("/health")
def health(request):
    return {"status": "ok"}

api.add_router("/core/", core_router)
api.add_router("/blog/", blog_router)
api.add_router("/leads/", leads_router)