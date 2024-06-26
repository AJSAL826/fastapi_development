from __future__ import annotations
from pydantic import BaseModel
from typing import List


class PostIn(BaseModel):
    body: str = None


class Post(PostIn):
    id: int


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int


class UserPostwithComment(BaseModel):
    post: Post
    Comment: List[Comment]
