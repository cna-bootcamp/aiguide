"""Solution Selection Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class SolutionSelectionAgent(BaseAgent):
    """
    솔루션을 평가하고 선정하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="솔루션 선정 에이전트",
            description="아이디어를 평가하고 최적의 솔루션을 선정합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        ideation_results = context.get("ideation_results", "")
        problem_hypothesis = context.get("problem_hypothesis", "")

        return f"""당신은 제품 전략 전문가입니다.
아이디어들을 체계적으로 평가하고 최적의 솔루션을 선정해주세요.

아이디에이션 결과:
{ideation_results if ideation_results else "아이디어 없음"}

문제 가설:
{problem_hypothesis if problem_hypothesis else "문제 가설 없음"}

다음 형식으로 솔루션 평가 및 선정을 수행해주세요:

## 1. 평가 프레임워크

### ICE 스코어링
각 아이디어를 다음 기준으로 1-10점 평가:
- **I**mpact (영향도): 문제 해결 효과
- **C**onfidence (확신도): 성공 가능성
- **E**ase (용이성): 구현 난이도 (역수)

ICE Score = (Impact + Confidence + Ease) / 3

### RICE 스코어링 (선택적)
- **R**each (도달 범위): 영향받는 사용자 수
- **I**mpact (영향도): 개인당 영향
- **C**onfidence (확신도): 데이터 신뢰도
- **E**ffort (노력): 필요한 인력-월

RICE Score = (Reach × Impact × Confidence) / Effort

## 2. 아이디어 평가표

| # | 아이디어 | Impact | Confidence | Ease | ICE Score | 순위 |
|---|---------|--------|-----------|------|-----------|-----|
| 1 | [아이디어명] | 8 | 7 | 6 | 7.0 | 3 |
| 2 | [아이디어명] | 9 | 8 | 7 | 8.0 | 1 |
[계속...]

## 3. 상위 3개 아이디어 상세 분석

### 1위: [아이디어명]
- **강점**:
- **약점**:
- **기회**:
- **위험**:
- **차별화 요소**:
- **MVP 범위**:

### 2위: [아이디어명]
[동일한 형식]

### 3위: [아이디어명]
[동일한 형식]

## 4. 최종 선정 솔루션

### 선정된 솔루션: [솔루션명]

**선정 이유**:
1. [이유 1]
2. [이유 2]
3. [이유 3]

**핵심 기능 (Must-have)**:
- 기능 1: [설명]
- 기능 2: [설명]
- 기능 3: [설명]

**부가 기능 (Nice-to-have)**:
- 기능 1: [설명]
- 기능 2: [설명]

**기술 스택 권장안**:
- Frontend:
- Backend:
- Database:
- Infrastructure:
- Third-party Services:

## 5. MVP 로드맵

### Phase 1: MVP (1-2개월)
- [ ] 핵심 기능 1
- [ ] 핵심 기능 2
- [ ] 핵심 기능 3

### Phase 2: 성장 (3-4개월)
- [ ] 부가 기능 추가
- [ ] 성능 최적화

### Phase 3: 확장 (5-6개월)
- [ ] 신규 기능
- [ ] 시장 확대

## 6. 성공 지표 (KPI)
- 핵심 지표 1: [목표치]
- 핵심 지표 2: [목표치]
- 핵심 지표 3: [목표치]

## 7. 리스크 관리
| 리스크 | 영향도 | 발생가능성 | 대응 전략 |
|--------|--------|-----------|----------|
| [리스크1] | 높음 | 중간 | [대응책] |

평가는 객관적이고 데이터 기반이어야 하며,
선정된 솔루션은 MVP로 구현 가능해야 합니다.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """솔루션 선정 실행"""
        try:
            if not self.validate_context(context, ["ideation_results"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=8000)

            result = self.format_output(
                content=response,
                metadata={
                    "evaluation_framework": "ICE",
                    "selection_complete": True
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Solution Selection agent: {str(e)}")
