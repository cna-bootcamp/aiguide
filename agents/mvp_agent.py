"""MVP Topic Definition Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class MVPAgent(BaseAgent):
    """
    MVP 주제를 정의하는 에이전트
    대상 비즈니스 도메인을 결정합니다.
    """

    def __init__(self):
        super().__init__(
            name="MVP 주제 정의 에이전트",
            description="대상 비즈니스 도메인을 정의하고 MVP 주제를 선정합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        user_input = context.get("user_input", "")

        return f"""당신은 비즈니스 도메인 전문가입니다.
사용자의 관심사나 아이디어를 기반으로 MVP(Minimum Viable Product) 주제를 정의해야 합니다.

사용자 입력: {user_input if user_input else "입력 없음"}

다음 형식으로 MVP 주제를 정의해주세요:

## MVP 주제
[구체적인 비즈니스 도메인 명시]

## 주제 선정 이유
[왜 이 주제를 선택했는지 3-5가지 이유]

## 시장 잠재력
[해당 도메인의 시장 잠재력 분석]

## 주요 특징
[이 도메인의 주요 특징 3-5가지]

예시 주제:
- 여행지 추천
- 음식배달
- 생활 구독관리
- 건강진단 및 예측
- 맞춤형 학습 플랫폼

사용자 입력이 없다면, 현재 트렌드와 시장 수요를 고려하여 적절한 MVP 주제를 제안해주세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """MVP 주제 정의 실행"""
        try:
            # Pre-execution validation
            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            # Generate prompt and call Claude
            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt)

            # Format and return result
            result = self.format_output(
                content=response,
                metadata={
                    "has_user_input": bool(context.get("user_input")),
                    "domain": self._extract_domain(response)
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in MVP agent execution: {str(e)}")

    def _extract_domain(self, response: str) -> str:
        """응답에서 도메인 추출"""
        lines = response.split('\n')
        for i, line in enumerate(lines):
            if '## MVP 주제' in line and i + 1 < len(lines):
                return lines[i + 1].strip()
        return "Unknown"
