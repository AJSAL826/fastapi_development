import json
from fastapi import APIRouter, HTTPException, Request
from models.structure import Post, CommentIn, Comment, PostIn, UserPostwithComment
from typing import List, Dict
from Exception.handler import CustomException, common_exception

error = 0
router = APIRouter()

post_body = {}


@router.post("/post", status_code=200, response_model=Dict[int, Post])
async def user_post_in(details: PostIn):
    function = "user_post_in"
    try:
        id = len(post_body)
        details = dict(details)
        new_post = {"id": id, **details}
        post_body[id] = new_post
        return post_body
    except Exception as e:
        common_exception(e, error, function)


@router.get("/post/get_post_details/{id}")
async def user_post(id: int):
    function = "user_post"
    try:
        error = 0
        if id in post_body.keys():
            return post_body[id]
        else:
            error = 1
            raise
    except Exception as e:
        e = None if error else e
        common_exception(e, error, function)


comments = {}


@router.post("/comment", tags=["add_comments"])
##have to check whether the post_id inside the user_post
async def comment_post(details: CommentIn):
    function = "comment_post"
    try:
        error = 0
        if details.post_id not in list(post_body):
            error = 1
            raise
        details = dict(details)
        comments[details["post_id"]] = {"id": len(comments), **details}
        return details
    except Exception as e:
        e = None if error else e
        common_exception(e, error, function)


@router.get("/get_comment/{ids}")
async def get_comments(ids: int):
    function = "get_comments"
    try:
        error = 0
        return [comments for value in comments.values() if value["post_id"] == ids]
    except Exception as e:
        e = None if error else e
        common_exception(e, error, function)


@router.get("/UserPostwithComment/{ids}", response_model=UserPostwithComment)
async def get_comments_and_post(ids: int):
    function = "get_comments and post"
    try:
        error = 0
        post = await user_post(ids)
        if not post:
            error = 1
            raise
        return {"post": post, "Comment": await get_comments(ids)}
    except Exception as e:
        e = None if error else e
        common_exception(e, error, function)
