"""Target Customer Definition Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class CustomerAgent(BaseAgent):
    """
    대상 고객 유형을 정의하는 에이전트
    JTBD(Jobs To Be Done) 형식으로 정의합니다.
    """

    def __init__(self):
        super().__init__(
            name="대상 고객 정의 에이전트",
            description="JTBD 형식으로 대상 고객 유형을 정의합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        mvp_topic = context.get("mvp_topic", "")

        return f"""당신은 고객 분석 전문가입니다.
JTBD(Jobs To Be Done) 프레임워크를 사용하여 대상 고객 유형을 정의해야 합니다.

MVP 주제: {mvp_topic}

다음 형식으로 대상 고객을 정의해주세요:

## 대상 고객 유형 (JTBD 형식)
[사용자군 + 완수하려는 과업]

예시:
- 집에서 조리된 음식을 먹고 싶은 음식소비자
- 가성비 좋은 생활 구독서비스를 이용하고 싶은 구독서비스 이용자
- 맞춤형 여행 일정을 계획하고 싶은 여행 계획자

## 사용자 세그먼트
[주요 사용자 그룹 3-5개와 각각의 특징]

## 완수하려는 과업 (Job to be Done)
[고객이 달성하고자 하는 목표와 동기]

## 고객의 Pain Points
[고객이 현재 겪고 있는 주요 어려움 5-7가지]

## 고객의 기대와 욕구
[고객이 원하는 결과와 이상적인 경험]

완수하려는 과업은 구체적으로 작성해야 이후 기획이 명확하게 진행됩니다.
'원하는 것'이나 '서비스를 이용하는 이유'를 명확히 표현하세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """대상 고객 정의 실행"""
        try:
            # Validate required context
            if not self.validate_context(context, ["mvp_topic"]):
                return self.format_error("Missing required context: mvp_topic")

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
                    "mvp_topic": context.get("mvp_topic"),
                    "jtbd_format": True
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Customer agent execution: {str(e)}")
