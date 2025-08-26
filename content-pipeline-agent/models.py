from typing import List
from pydantic import BaseModel


class BlogPost(BaseModel):
    title: str
    subtitle: str
    sections: List[str]


class Tweet(BaseModel):
    content: str
    hashtags: str


class Linkedin(BaseModel):
    hook: str
    content: str
    call_to_action: str


class Score(BaseModel):
    score: int = 0
    reason: str = ""


class ContentPipelineState(BaseModel):
    # Inputs
    content_type: str = ""
    topic: str = ""

    # Internal
    max_length: int = 0
    research: str = ""
    score: Score | None = None

    # Content
    blog_post: BlogPost | None = None
    tweet: Tweet | None = None
    linkedin: Linkedin | None = None
