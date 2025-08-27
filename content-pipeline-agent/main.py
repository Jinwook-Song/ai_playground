from crewai import Agent, LLM
from crewai.flow.flow import Flow, listen, start, router, or_
from seo_crew import SeoCrew
from tools import web_search_tool
from models import BlogPost, ContentPipelineState, Linkedin, Tweet
from virality_crew import ViralityCrew


class ContentPipelineFlow(Flow[ContentPipelineState]):
    """
    This flow is used to create content for a given topic.
    It will conduct research, make the content, and score it.
    """

    ################# 🚀 INIT CONTENT PIPELINE 🚀 #################
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

    ################# 🔍 CONDUCT RESEARCH 🔍 #################
    @listen(init_content_pipeline)
    def conduct_research(self):
        researcher = Agent(
            role="Head Researcher",
            backstory="""
                You're like a digital detective who loves digging up fascinating facts and insights. You have a knack for finding the good stuff that others miss.
                """,
            goal=f"Find the most interesting and useful info about {self.state.topic}",
            tools=[web_search_tool],
            llm="openai/gpt-5-mini-2025-08-07",
        )

        self.state.research = researcher.kickoff(
            f"Find the most interesting and useful info about {self.state.topic}"
        )

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

    ################# 📝 MAKE CONTENT 📝 #################
    @listen(or_("make_blog", "remake_blog"))
    def handle_make_blog(self):
        blog_post = self.state.blog_post

        llm = LLM(
            model="openai/gpt-5-mini-2025-08-07",
            response_format=BlogPost,
        )

        if blog_post is None:  # make it
            result = llm.call(f"""
            Make a blog post on the topic of {self.state.topic} using the following research:

            <research>
            ========================= 
            {self.state.research}
            =========================
            </research>
            """)
        else:  # improve it
            result = llm.call(f"""
            You wrote this blog post, but it does not have a good SEO score because of {self.state.score.reason}

            <goal>
            ========================= 
            Improve the blog post so that it has a good SEO score.
            =========================
            </goal>

            <blog_post>
            ========================= 
            {self.state.blog_post.model_dump_json()}
            =========================
            </blog_post>

            Use the following research to make the blog post:

            <research>
            ========================= 
            {self.state.research}
            =========================
            """)

        self.state.blog_post = BlogPost.model_validate_json(result)

    @listen(or_("make_tweet", "remake_tweet"))
    def handle_make_tweet(self):
        tweet = self.state.tweet

        llm = LLM(
            model="openai/gpt-5-mini-2025-08-07",
            response_format=Tweet,
        )

        if tweet is None:  # make it
            result = llm.call(f"""
            Make a tweet on the topic of {self.state.topic} using the following research:

            <research>
            ========================= 
            {self.state.research}
            =========================
            </research>
            """)
        else:  # improve it
            result = llm.call(f"""
            You wrote this tweet, but it does not have a good virality score because of {self.state.score.reason}

            <goal>
            ========================= 
            Improve the tweet so that it has a good virality score.
            =========================
            </goal>

            <tweet>
            ========================= 
            {self.state.tweet.model_dump_json()}
            =========================
            </tweet>

            Use the following research to make the tweet:

            <research>
            ========================= 
            {self.state.research}
            =========================
            </research>
            """)

        self.state.tweet = Tweet.model_validate_json(result)

    @listen(or_("make_linkedin", "remake_linkedin"))
    def handle_make_linkedin(self):
        linkedin = self.state.linkedin

        llm = LLM(
            model="openai/gpt-5-mini-2025-08-07",
            response_format=Linkedin,
        )

        if linkedin is None:  # make it
            result = llm.call(f"""
            Make a linkedin post on the topic of {self.state.topic} using the following research:

            <research>
            ========================= 
            {self.state.research}
            =========================
            </research>
            """)
        else:  # improve it
            result = llm.call(f"""
            You wrote this linkedin post, but it does not have a good virality score because of {self.state.score.reason}

            <goal>
            ========================= 
            Improve the linkedin post so that it has a good virality score.
            =========================
            </goal>

            <linkedin>
            ========================= 
            {self.state.linkedin.model_dump_json()}
            =========================
            </linkedin>

            Use the following research to make the linkedin post:

            <research>
            ========================= 
            {self.state.research}
            =========================
            </research>
            """)

        self.state.linkedin = Linkedin.model_validate_json(result)

    ################# 📊 CHECK QUALITY 📊 #################
    @listen(handle_make_blog)
    def check_seo(self):
        result = (
            SeoCrew()
            .crew()
            .kickoff(
                inputs={
                    "topic": self.state.topic,
                    "blog_post": self.state.blog_post.model_dump_json(),
                }
            )
        )
        self.state.score = result.pydantic

    @listen(or_(handle_make_tweet, handle_make_linkedin))
    def check_virality(self):
        result = (
            ViralityCrew()
            .crew()
            .kickoff(
                inputs={
                    "topic": self.state.topic,
                    "content_type": self.state.content_type,
                    "content": (
                        self.state.tweet.model_dump_json()
                        if self.state.contenty_type == "tweet"
                        else self.state.linkedin_post.model_dump_json()
                    ),
                }
            )
        )
        self.state.score = result.pydantic

    @router(or_(check_seo, check_virality))
    def score_router(self):
        content_type = self.state.content_type
        score = self.state.score

        print(score)

        if score.score >= 7:
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
        """Finalize the content"""
        print("🎉 Finalizing content...")

        if self.state.content_type == "blog":
            print(f"📝 Blog Post: {self.state.blog_post.title}")
            print(f"🔍 SEO Score: {self.state.score.score}/10")
        elif self.state.content_type == "tweet":
            print(f"🐦 Tweet: {self.state.tweet}")
            print(f"🚀 Virality Score: {self.state.score.score}/10")
        elif self.state.content_type == "linkedin":
            print(f"💼 LinkedIn: {self.state.linkedin_post.title}")
            print(f"🚀 Virality Score: {self.state.score.score}/10")

        print("✅ Content ready for publication!")


flow = ContentPipelineFlow()


# flow.plot()

flow.kickoff(
    inputs={
        "content_type": "blog",
        "topic": "CPR Training",
    }
)
