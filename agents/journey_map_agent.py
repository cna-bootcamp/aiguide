"""User Journey Map Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class JourneyMapAgent(BaseAgent):
    """
    User Journey Map을 작성하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="User Journey Map 작성 에이전트",
            description="고객 여정 지도를 작성합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        mvp_topic = context.get("mvp_topic", "")
        target_customer = context.get("target_customer", "")
        customer_experience = context.get("customer_experience", "")

        return f"""당신은 UX 디자인 전문가입니다.
고객의 여정을 시각화하고 분석하는 User Journey Map을 작성해주세요.

MVP 주제: {mvp_topic}
대상 고객: {target_customer}

고객 경험 조사 결과 (인터뷰, 관찰, 체험):
{customer_experience if customer_experience else "고객 경험 데이터 없음"}

**중요**: 고객 경험 조사 결과에서 다음 항목들을 적극 활용하세요:
- 인터뷰에서 발견된 Pain Points와 Needs
- 관찰에서 파악된 행동 패턴
- 체험에서 경험한 실제 고객 감정과 만족도

다음 형식으로 User Journey Map을 작성해주세요:

## 1. 페르소나 (Persona)
- 이름, 나이, 직업
- 배경 및 상황
- 목표와 동기
- 기술 친숙도

## 2. 여정 단계 (Journey Stages)

각 단계별로 다음 항목을 분석:

### 단계 1: [인지/발견 단계]
- **고객 행동**: 무엇을 하는가?
- **사고**: 무엇을 생각하는가?
- **감정**: 어떻게 느끼는가? (감정 곡선)
- **터치포인트**: 어디서 서비스와 만나는가?
- **Pain Points**: 어려움과 장애물
- **Gain Points**: 긍정적 경험과 만족 요소

### 단계 2: [고려 단계]
[동일한 항목 분석]

### 단계 3: [구매/이용 결정]
[동일한 항목 분석]

### 단계 4: [사용 경험]
[동일한 항목 분석]

### 단계 5: [사후 관리/재구매]
[동일한 항목 분석]

## 3. 핵심 인사이트
- 가장 큰 Pain Point 3가지
- 개선 기회 영역
- 감정적 고점과 저점
- 이탈 위험 구간

## 4. 기회 영역 (Opportunity Areas)
- 우선순위가 높은 개선 영역
- 혁신 가능한 터치포인트
- 차별화 포인트

감정 곡선은 이모지나 텍스트로 표현해주세요.
예: 😊 긍정적, 😐 중립적, 😞 부정적
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """User Journey Map 작성 실행"""
        try:
            if not self.validate_context(context, ["mvp_topic", "target_customer"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=6000)

            result = self.format_output(
                content=response,
                metadata={
                    "has_customer_experience": bool(context.get("customer_experience")),
                    "journey_type": "end_to_end"
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Journey Map agent: {str(e)}")
