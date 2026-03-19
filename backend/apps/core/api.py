from ninja import Schema, Router
from typing import List
from .models import Project

router = Router()

class ProjectSchema(Schema):
    id: int
    title: str
    description: str
    tech_stack: List[str]
    github_url: str | None
    live_url: str | None
    featured: bool

@router.get("/projects", response=list[ProjectSchema])
def list_projects(request):
    return Project.objects.all().order_by("-created_at")