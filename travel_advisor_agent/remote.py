import vertexai
from vertexai import agent_engines

PROJECT_ID = "gen-lang-client-xxxxxxx"
LOCATION = "asia-northeast1"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

# deployments = agent_engines.list()

# for deployment in deployments:
#     print(deployment)

DEPLOYMENT_ID = "projects/644711056427/locations/asia-northeast1/reasoningEngines/8962286403769597952"

SESSION_ID = "6410113757271293952"

remote_app = agent_engines.get(DEPLOYMENT_ID)

remote_app.delete(force=True)


# remote_session = remote_app.create_session(user_id="u_123")

# print(remote_session["id"])

# for event in remote_app.stream_query(
#     user_id="u_123",
#     session_id=SESSION_ID,
#     message="12월에 동남아 여행가고싶은데, 추천해줘",
# ):
#     print(event, "\n", "=" * 50)
