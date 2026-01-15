cd user-facing-agent
adk web

cd remote_adk_agent
uvicorn agent:app --port 8001 --reload
http://127.0.0.1:8001/.well-known/agent-card.json
