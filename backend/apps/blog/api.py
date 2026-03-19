from ninja import Schema, Router
from typing import List
from .models import Post

router = Router()

class PostSchema(Schema):
    id: int
    title: str
    slug: str
    excerpt: str
    content: str


@router.get("/posts", response=list[PostSchema])
def list_posts(request):
    return Post.objects.filter(is_published=True).order_by("-published_at")

@router.get("/posts/{slug}", response=PostSchema)
def get_post(request, slug: str):
    return Post.objects.get(slug=slug)