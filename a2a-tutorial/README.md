# A2A (Agent-to-Agent) 튜토리얼

이 프로젝트는 Agent-to-Agent (A2A) 통신을 구현한 예제입니다.

## 아키텍처

- **user-facing-agent**: 클라이언트 역할을 하는 메인 에이전트 (Google ADK 사용)
- **remote_adk_agent**: 서버 역할을 하는 역사 도움 에이전트 (포트 8001, Google ADK 사용)
- **langgraph_agent**: 서버 역할을 하는 철학 도움 에이전트 (포트 8002, LangGraph 사용)

## 동작 방식

1. user-facing-agent가 학생 도움 에이전트 역할을 하며, 두 개의 remote agent를 sub-agents로 가짐
2. 각 remote agent들은 A2A 프로토콜을 통해 독립적으로 실행되는 서버 에이전트들
3. 클라이언트가 특정 과목(역사/철학)에 대한 질문을 하면 해당 remote agent와 A2A 통신하여 응답을 받음

## 실행 방법

### 1. Remote Agent 서버들 실행

#### 역사 도움 에이전트 (포트 8001)

```bash
cd remote_adk_agent
uvicorn agent:app --port 8001 --reload
```

#### 철학 도움 에이전트 (포트 8002)

```bash
cd langgraph_agent
uvicorn server:app --port 8002 --reload
```

### 2. User-facing Agent 클라이언트 실행

```bash
cd user-facing-agent
adk web
```

## Agent Card 확인

- 역사 에이전트: http://127.0.0.1:8001/.well-known/agent-card.json
- 철학 에이전트: http://127.0.0.1:8002/.well-known/agent-card.json

## 참고 자료

- [A2A 프로토콜 Python SDK 문서](https://a2a-protocol.org/latest/sdk/python/api/a2a.html#a2a.types.SendMessageSuccessResponse)
