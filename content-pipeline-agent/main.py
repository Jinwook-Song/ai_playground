from crewai.flow.flow import Flow, listen, start, router, and_, or_
from pydantic import BaseModel


class ContentPipelineState(BaseModel):
    # Inputs
    content_type: str = ""
    topic: str = ""

    # Internal
    max_length: int = 0
    score: int = 0

    # Content
    blog_post: str = ""
    tweet: str = ""
    linkedin: str = ""


class ContentPipelineFlow(Flow[ContentPipelineState]):
    @start()
    def init_content_pipeline(self):
        if self.state.topic == "":
            raise ValueError("Topic is required")

        if self.state.content_type == "blog":
            self.state.max_length = 800
        elif self.state.content_type == "tweet":
            self.state.max_length = 150
        elif self.state.content_type == "linkedin":
            self.state.max_length = 500
        else:
            raise ValueError("Invalid content type")

    @listen(init_content_pipeline)
    def conduct_research(self):
        print(f"Conducting research for {self.state.topic}")
        return True

    @router(conduct_research)
    def conduct_research_router(self):
        content_type = self.state.content_type
        if content_type == "blog":
            return "make_blog"
        elif content_type == "tweet":
            return "make_tweet"
        elif content_type == "linkedin":
            return "make_linkedin"
        else:
            raise ValueError("Invalid content type")

    @listen(or_("make_blog", "remake_blog"))
    def handle_make_blog(self):
        # if blog post has been maed, show the old one to the ai and ask it to improve it, else just make a new one
        print(f"Making blog for {self.state.topic}")

    @listen(or_("make_tweet", "remake_tweet"))
    def handle_make_tweet(self):
        # if tweet has been made, show the old one to the ai and ask it to improve it, else just make a new one
        print(f"Making tweet for {self.state.topic}")

    @listen(or_("make_linkedin", "remake_linkedin"))
    def handle_make_linkedin(self):
        # if linkedin has been made, show the old one to the ai and ask it to improve it, else just make a new one
        print(f"Making linkedin for {self.state.topic}")

    @listen(handle_make_blog)
    def check_seo(self):
        print(f"Checking SEO for {self.state.topic}")

    @listen(or_(handle_make_tweet, handle_make_linkedin))
    def check_virality(self):
        print(f"Checking virality for {self.state.topic}")

    @router(or_(check_seo, check_virality))
    def score_router(self):
        content_type = self.state.content_type
        score = self.state.score

        if score >= 8:
            return "checks_passed"
        else:
            if content_type == "blog":
                return "remake_blog"
            elif content_type == "tweet":
                return "remake_tweet"
            elif content_type == "linkedin":
                return "remake_linkedin"
            else:
                raise ValueError("Invalid content type")

    @listen("checks_passed")
    def finalize_content(self):
        print(f"Finalizing content for {self.state.topic}")


flow = ContentPipelineFlow()


flow.plot()

# flow.kickoff(
#     inputs={
#         "content_type": "blog",
#         "topic": "AI",
#     }
# )
