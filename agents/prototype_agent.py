"""Prototype Development Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class PrototypeAgent(BaseAgent):
    """
    프로토타입 개발 가이드를 제공하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="프로토타입 개발 에이전트",
            description="프로토타입 개발 계획과 가이드를 제공합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        uiux_design = context.get("uiux_design", "")
        user_stories = context.get("user_stories", "")
        selected_solution = context.get("selected_solution", "")

        return f"""당신은 풀스택 개발 전문가입니다.
UI/UX 설계와 유저스토리를 기반으로 프로토타입 개발 가이드를 작성해주세요.

UI/UX 설계:
{uiux_design if uiux_design else "설계 정보 없음"}

유저스토리:
{user_stories if user_stories else "유저스토리 없음"}

선정된 솔루션:
{selected_solution if selected_solution else "솔루션 정보 없음"}

다음 형식으로 프로토타입 개발 가이드를 작성해주세요:

## 1. 프로토타입 개요

### 목표
- MVP 구현 범위
- 검증하려는 가설
- 타겟 릴리즈 일정

### 프로토타입 유형
- [ ] Low-fidelity (Paper/Sketch)
- [x] High-fidelity (Interactive)
- [ ] Functional Prototype (Working Code)

## 2. 기술 스택

### Frontend
```
Framework: [예: React, Vue, Next.js]
UI Library: [예: Material-UI, Tailwind CSS]
State Management: [예: Redux, Zustand, Recoil]
Form Handling: [예: React Hook Form, Formik]
HTTP Client: [예: Axios, Fetch API]
```

### Backend
```
Framework: [예: Node.js/Express, Django, FastAPI]
Database: [예: PostgreSQL, MongoDB, Supabase]
ORM: [예: Prisma, TypeORM, Mongoose]
Authentication: [예: JWT, OAuth, Firebase Auth]
API: [예: RESTful, GraphQL]
```

### Infrastructure
```
Hosting: [예: Vercel, Netlify, AWS, Heroku]
Database Hosting: [예: Supabase, MongoDB Atlas, AWS RDS]
CDN: [예: Cloudflare, AWS CloudFront]
Monitoring: [예: Sentry, LogRocket]
Analytics: [예: Google Analytics, Mixpanel]
```

### Development Tools
```
Version Control: Git + GitHub
Package Manager: npm/yarn/pnpm
Bundler: Vite/Webpack
Testing: Jest, React Testing Library, Playwright
CI/CD: GitHub Actions, Vercel
```

## 3. 프로젝트 구조

### Frontend Structure
```
project-root/
├── src/
│   ├── components/
│   │   ├── common/
│   │   ├── layout/
│   │   └── features/
│   ├── pages/
│   ├── hooks/
│   ├── services/
│   ├── utils/
│   ├── store/
│   ├── styles/
│   └── types/
├── public/
├── tests/
└── package.json
```

### Backend Structure
```
backend/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── services/
│   ├── utils/
│   └── config/
├── tests/
└── package.json
```

## 4. 데이터 모델

### Entity Relationship Diagram
```
User
├── id (PK)
├── email (unique)
├── name
├── created_at
└── updated_at

[기타 엔티티들...]
```

### Database Schema
```sql
-- User Table
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- [추가 테이블들...]
```

## 5. API 설계

### API Endpoints

#### Authentication
```
POST   /api/auth/register    - 회원가입
POST   /api/auth/login       - 로그인
POST   /api/auth/logout      - 로그아웃
GET    /api/auth/me          - 현재 사용자 정보
```

#### [Feature A]
```
GET    /api/[resource]       - 목록 조회
GET    /api/[resource]/:id   - 상세 조회
POST   /api/[resource]       - 생성
PUT    /api/[resource]/:id   - 수정
DELETE /api/[resource]/:id   - 삭제
```

### API Response Format
```json
{
  "success": true,
  "data": {
    // 응답 데이터
  },
  "message": "Success message",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message",
    "details": {}
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## 6. 구현 로드맵

### Phase 1: 프로젝트 셋업 (Day 1-2)
- [ ] 개발 환경 설정
- [ ] Git 레포지토리 생성
- [ ] 프로젝트 구조 생성
- [ ] 기본 라우팅 설정
- [ ] 데이터베이스 연결

### Phase 2: 인증 시스템 (Day 3-5)
- [ ] 회원가입 구현
- [ ] 로그인 구현
- [ ] JWT 토큰 관리
- [ ] 인증 미들웨어

### Phase 3: 핵심 기능 1 (Day 6-10)
- [ ] UI 컴포넌트 구현
- [ ] API 엔드포인트 구현
- [ ] 데이터 CRUD
- [ ] 상태 관리

### Phase 4: 핵심 기능 2 (Day 11-15)
[동일한 형식]

### Phase 5: 통합 및 테스트 (Day 16-18)
- [ ] 통합 테스트
- [ ] E2E 테스트
- [ ] 버그 수정
- [ ] 성능 최적화

### Phase 6: 배포 (Day 19-20)
- [ ] 프로덕션 빌드
- [ ] 배포 설정
- [ ] 도메인 연결
- [ ] 모니터링 설정

## 7. 핵심 기능 구현 가이드

### 기능 1: [기능명]

#### Frontend Component
```typescript
// Example React Component
import React, { useState, useEffect } from 'react';

interface Props {
  // props definition
}

export const ComponentName: React.FC<Props> = ({ /* props */ }) => {
  const [state, setState] = useState<Type>(initialValue);

  useEffect(() => {
    // side effects
  }, []);

  return (
    <div>
      {/* JSX */}
    </div>
  );
};
```

#### Backend Controller
```typescript
// Example Express Controller
import { Request, Response } from 'express';

export const controllerName = async (req: Request, res: Response) => {
  try {
    // logic
    res.json({ success: true, data: result });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};
```

### 기능 2: [기능명]
[동일한 형식]

## 8. 보안 고려사항

### Frontend Security
- [ ] XSS 방지
- [ ] CSRF 토큰
- [ ] Input Sanitization
- [ ] Secure Storage (토큰 관리)

### Backend Security
- [ ] SQL Injection 방지
- [ ] Rate Limiting
- [ ] CORS 설정
- [ ] HTTPS 강제
- [ ] 환경변수 관리
- [ ] 비밀번호 해싱 (bcrypt)

## 9. 성능 최적화

### Frontend
- [ ] Code Splitting
- [ ] Lazy Loading
- [ ] Image Optimization
- [ ] Caching Strategy
- [ ] Bundle Size Optimization

### Backend
- [ ] Database Indexing
- [ ] Query Optimization
- [ ] Caching (Redis)
- [ ] Connection Pooling
- [ ] CDN 활용

## 10. 테스팅 전략

### Unit Tests
```typescript
describe('ComponentName', () => {
  it('should render correctly', () => {
    // test implementation
  });
});
```

### Integration Tests
```typescript
describe('API Endpoint', () => {
  it('should return correct response', async () => {
    // test implementation
  });
});
```

### E2E Tests
```typescript
describe('User Flow', () => {
  it('should complete user journey', async () => {
    // test implementation
  });
});
```

## 11. 배포 가이드

### Frontend Deployment (Vercel)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### Backend Deployment (Heroku/Railway)
```bash
# Example deployment commands
git push heroku main
```

### Environment Variables
```env
# .env.example
DATABASE_URL=
JWT_SECRET=
API_KEY=
```

## 12. 모니터링 및 유지보수

### Logging
- Application logs
- Error tracking (Sentry)
- Performance monitoring

### Analytics
- User behavior tracking
- Conversion funnel
- A/B testing

### Maintenance Checklist
- [ ] 정기 백업
- [ ] 보안 업데이트
- [ ] 성능 모니터링
- [ ] 사용자 피드백 수집

## 13. 다음 단계

### 프로토타입 검증 후
1. 사용자 테스트 실시
2. 피드백 수집 및 분석
3. 개선사항 반영
4. Scale-up 계획

### Production Ready Checklist
- [ ] 모든 핵심 기능 구현
- [ ] 테스트 커버리지 > 80%
- [ ] 보안 감사 완료
- [ ] 성능 벤치마크 통과
- [ ] 문서화 완료
- [ ] 운영 매뉴얼 작성

실제 코드 예시와 함께 구체적인 구현 가이드를 제공해주세요.
MVP는 2-3주 내에 구현 가능한 범위로 설정하세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """프로토타입 개발 가이드 생성 실행"""
        try:
            if not self.validate_context(context, ["user_stories"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=8000)

            result = self.format_output(
                content=response,
                metadata={
                    "prototype_type": "functional",
                    "timeline": "2-3 weeks",
                    "tech_stack_included": True
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Prototype agent: {str(e)}")
