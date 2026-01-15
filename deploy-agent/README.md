# Deploy Agent

OpenAI Conversation API를 활용한 AI 에이전트 서비스입니다. FastAPI로 구축되었으며 Railway 플랫폼에 배포됩니다.

## 기능

- OpenAI Agents SDK를 활용한 대화형 AI 에이전트
- 대화 상태 유지 및 관리
- 실시간 스트리밍 응답 지원
- RESTful API 설계

## 기술 스택

- **Backend**: FastAPI (Python)
- **AI**: OpenAI Agents SDK
- **배포**: Railway
- **패키지 관리**: uv

## 설치 및 실행

### 로컬 개발 환경

1. **의존성 설치**

   ```bash
   pip install -r requirements.txt
   # 또는 uv를 사용하는 경우
   uv sync
   ```

2. **환경 변수 설정**
   `.env` 파일을 생성하고 OpenAI API 키를 설정하세요:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **서버 실행**
   ```bash
   uvicorn main:app --reload
   ```

## API 엔드포인트

### 기본 상태 확인

- `GET /` - 서버 상태 확인

### 대화 관리

- `POST /conversations` - 새로운 대화 생성
- `POST /conversations/{conversation_id}/message` - 메시지 전송 및 응답 받기
- `POST /conversations/{conversation_id}/message/stream` - 실시간 스트리밍 응답
- `POST /conversations/{conversation_id}/message/stream/all` - 모든 이벤트 스트리밍

## Railway 배포

1. **Railway CLI 설치**

   ```bash
   npm install -g @railway/cli
   ```

2. **프로젝트 초기화 및 배포**
   ```bash
   railway init
   railway up
   ```

## 관련 링크

- [OpenAI Conversation API](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses#manually-manage-conversation-state)
- [Railway CLI 문서](https://docs.railway.com/guides/cli)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
