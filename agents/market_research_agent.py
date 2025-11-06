"""Market Research Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class MarketResearchAgent(BaseAgent):
    """
    시장 조사를 수행하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="시장 조사 에이전트",
            description="MVP 주제에 대한 시장 조사를 수행합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        mvp_topic = context.get("mvp_topic", "")
        target_customer = context.get("target_customer", "")

        return f"""당신은 시장 분석 전문가입니다.
주어진 MVP 주제와 대상 고객에 대한 심층 시장 조사를 수행해주세요.

MVP 주제: {mvp_topic}
대상 고객: {target_customer}

다음 항목들을 포함하여 시장 조사 보고서를 작성해주세요:

## 1. 시장 규모 및 성장성
- 현재 시장 규모 (TAM, SAM, SOM)
- 연평균 성장률 (CAGR)
- 향후 5년 전망

## 2. 경쟁 환경 분석
- 주요 경쟁사 3-5개
- 각 경쟁사의 강점과 약점
- 시장 점유율 분포

## 3. 고객 트렌드
- 최근 소비자 행동 변화
- 주요 트렌드 3-5가지
- 기술 혁신의 영향

## 4. 규제 및 법적 환경
- 관련 규제 사항
- 진입 장벽
- 컴플라이언스 요구사항

## 5. SWOT 분석
- Strengths (강점)
- Weaknesses (약점)
- Opportunities (기회)
- Threats (위협)

## 6. 시장 진입 전략 제안
- 권장 진입 방식
- 차별화 포인트
- 예상 리스크 및 대응 방안

실제 데이터와 통계를 기반으로 작성하고, 출처를 명시해주세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """시장 조사 실행"""
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
                    "research_type": "market_analysis",
                    "depth": "comprehensive"
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Market Research agent: {str(e)}")
