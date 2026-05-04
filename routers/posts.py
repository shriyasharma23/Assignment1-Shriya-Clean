from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Post

router = APIRouter()


@router.get("/getPostsUploaded")
def getPostsUploaded(
    page: int     = 1,
    per_page: int = 10,
    db: Session = Depends(get_db)
):
    if page < 1:
        raise HTTPException(status_code=400, detail="page must be 1 or greater")
    if per_page < 1 or per_page > 100:
        raise HTTPException(status_code=400, detail="per_page must be between 1 and 100")

    total_posts = db.query(Post).count()

    if total_posts == 0:
        raise HTTPException(status_code=404, detail="No posts found in the database")

    total_pages = (total_posts + per_page - 1) // per_page

    if page > total_pages:
        raise HTTPException(
            status_code=404,
            detail=f"Page {page} does not exist. Total pages: {total_pages}"
        )

    offset = (page - 1) * per_page

    posts = (
        db.query(Post)
        .order_by(Post.post_dt.desc())
        .limit(per_page)
        .offset(offset)
        .all()
    )

    posts_list = [
        {
            "id":           post.id,
            "post_by":      post.post_by,
            "post_date":    post.post_dt.strftime("%Y-%m-%d"),
            "post_details": post.post_details
        }
        for post in posts
    ]

    return {
        "status":       "success",
        "page":         page,
        "per_page":     per_page,
        "total_posts":  total_posts,
        "total_pages":  total_pages,
        "has_next":     page < total_pages,
        "has_previous": page > 1,
        "posts":        posts_list
    }