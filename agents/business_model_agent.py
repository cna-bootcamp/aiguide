"""Business Model Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class BusinessModelAgent(BaseAgent):
    """
    비즈니스 모델을 기획하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="비즈니스 모델 기획 에이전트",
            description="Lean Canvas 기반 비즈니스 모델을 기획합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        selected_solution = context.get("selected_solution", "")
        target_customer = context.get("target_customer", "")
        problem_hypothesis = context.get("problem_hypothesis", "")

        return f"""당신은 비즈니스 모델 설계 전문가입니다.
Lean Canvas를 사용하여 체계적인 비즈니스 모델을 기획해주세요.

선정된 솔루션:
{selected_solution if selected_solution else "솔루션 정보 없음"}

대상 고객:
{target_customer if target_customer else "고객 정보 없음"}

문제 가설:
{problem_hypothesis if problem_hypothesis else "문제 가설 없음"}

다음 형식으로 비즈니스 모델을 작성해주세요:

## Lean Canvas

### 1. Problem (문제)
- 해결하려는 주요 문제 Top 3
- 기존 대안 (Existing Alternatives)

### 2. Customer Segments (고객 세그먼트)
- **Primary Target**: 주요 타겟 고객
- **Early Adopters**: 얼리어답터 특성
- **Customer Jobs**: 고객이 완수하려는 일

### 3. Unique Value Proposition (고유 가치 제안)
- **한 문장 핵심 가치**:
- **High-level Concept**: "X를 위한 Y" 형식
- 예: "바쁜 직장인을 위한 Spotify (음악 → 도시락)"

### 4. Solution (솔루션)
- 각 문제에 대한 해결책 Top 3
- 핵심 기능 목록

### 5. Channels (채널)
- **획득 채널**: 고객을 어떻게 찾을 것인가?
- **전달 채널**: 제품을 어떻게 전달할 것인가?
- **유지 채널**: 고객을 어떻게 유지할 것인가?

### 6. Revenue Streams (수익 흐름)
- **수익 모델**: 구독, 거래 수수료, 광고, 프리미엄 등
- **가격 전략**:
- **LTV (Life Time Value)**: 예상 고객 생애 가치
- **수익 예측**:
  - Year 1:
  - Year 2:
  - Year 3:

### 7. Cost Structure (비용 구조)
- **고정 비용**:
  - 인건비
  - 사무실
  - 인프라
- **변동 비용**:
  - 마케팅
  - 서버 비용
  - 고객 지원
- **예상 초기 투자**:
- **BEP (손익분기점)**:

### 8. Key Metrics (핵심 지표)
- **Acquisition**: 획득 지표 (CAC, 가입자 수)
- **Activation**: 활성화 지표 (첫 사용률)
- **Retention**: 유지 지표 (재방문율, Churn)
- **Revenue**: 수익 지표 (ARPU, MRR)
- **Referral**: 추천 지표 (바이럴 계수)

### 9. Unfair Advantage (경쟁 우위)
- 쉽게 복제할 수 없는 차별화 요소
- 독자적 기술, 네트워크 효과, 전문성 등

## 2. Business Model Canvas (추가)

| 핵심 파트너 | 핵심 활동 | 가치 제안 | 고객 관계 | 고객 세그먼트 |
|-----------|----------|----------|----------|-------------|
| | | | | |
| **핵심 자원** | | | **채널** | |
| **비용 구조** | | **수익원** | | |

## 3. 경쟁 분석 및 포지셔닝

### 경쟁 매트릭스
| 경쟁사 | 가격 | 기능 | UX | 우리의 차별점 |
|--------|------|------|-----|-------------|
| 경쟁사A | | | | |
| 경쟁사B | | | | |
| 우리 | | | | |

### 포지셔닝 맵
[2x2 매트릭스로 시장 포지셔닝 설명]

## 4. Go-to-Market 전략

### Launch 전략
- **Pre-launch**:
- **Launch**:
- **Post-launch**:

### Growth 전략
- 단기 (0-3개월):
- 중기 (3-12개월):
- 장기 (12개월+):

## 5. 재무 계획

### 예상 손익계산서 (3년)
| 항목 | Year 1 | Year 2 | Year 3 |
|------|--------|--------|--------|
| 매출 | | | |
| 비용 | | | |
| 영업이익 | | | |

### 자금 조달 계획
- Seed:
- Series A:
- 사용 계획:

현실적이고 실행 가능한 비즈니스 모델을 제시해주세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """비즈니스 모델 기획 실행"""
        try:
            if not self.validate_context(context, ["selected_solution", "target_customer"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=8000)

            result = self.format_output(
                content=response,
                metadata={
                    "framework": "Lean Canvas",
                    "financial_projection": "3_years"
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Business Model agent: {str(e)}")
