---
name: service-planning
description: Orchestrates complete AI service planning workflow from MVP topic to prototype. Automatically activates all planning skills in sequence when user provides a service or product idea.
---

# AI Service Planning Workflow

Complete end-to-end service planning automation from MVP concept to prototype development.

## When to Use

- User provides an MVP topic or product idea
- Starting a new service planning project
- Need complete planning workflow from scratch
- User mentions: "plan a service", "create MVP", "full planning process"

## Workflow Overview

This skill orchestrates 6 stages with 13 specialized skills:

```
Stage 1: Definition (MVP + Customer)
   ↓
Stage 2: Problem Discovery (Market + Experience + Journey + Hypothesis)
   ↓
Stage 3: Solution (Ideation + Selection)
   ↓
Stage 4: Business Model
   ↓
Stage 5: Product Design (Event Storming + User Stories + UI/UX)
   ↓
Stage 6: Prototype
```

## Instructions

When user provides an MVP topic, execute this complete workflow:

### Stage 1: Topic Definition & Customer Analysis (5-10 min)

**Step 1.1: MVP Definition**
```
Invoke mvp-definition skill with user's topic
Output: Clear MVP scope, domain, and market potential
Save to: outputs/01-mvp-definition.md
```

**Step 1.2: Customer Analysis**
```
Use mvp-definition output
Invoke customer-analysis skill
Output: Target customer personas with JTBD
Save to: outputs/02-customer-analysis.md
```

### Stage 2: Problem Discovery (15-20 min)

**Step 2.1: Market Research**
```
Use MVP topic + customer analysis
Invoke market-research skill
Output: Market analysis, competition, trends
Save to: outputs/03-market-research.md
```

**Step 2.2: Customer Experience Data**
```
Use customer personas
Invoke customer-experience skill
Output: Interview data, observations, pain points
Save to: outputs/04-customer-experience.md
```

**Step 2.3: Journey Mapping**
```
Use customer analysis + experience data
Invoke journey-mapping skill
Output: Complete user journey maps
Save to: outputs/05-journey-map.md
```

**Step 2.4: Problem Hypothesis**
```
Use journey map insights
Invoke problem-hypothesis skill
Output: Core problem statements to solve
Save to: outputs/06-problem-hypothesis.md
```

### Stage 3: Solution Exploration (10-15 min)

**Step 3.1: Ideation**
```
Use problem hypothesis
Invoke ideation skill
Output: Multiple solution ideas (10-20)
Save to: outputs/07-ideation.md
```

**Step 3.2: Solution Selection**
```
Use ideation output
Invoke solution-selection skill
Output: Selected optimal solution with rationale
Save to: outputs/08-solution-selection.md
```

### Stage 4: Business Modeling (10 min)

**Step 4.1: Business Model Canvas**
```
Use selected solution + customer analysis
Invoke business-modeling skill
Output: Complete Lean Canvas
Save to: outputs/09-business-model.md
```

### Stage 5: Product Design (20-25 min)

**Step 5.1: Event Storming**
```
Use selected solution + customer journey
Invoke event-storming skill
Output: Domain events, commands, aggregates
Save to: outputs/10-event-storming.md
```

**Step 5.2: User Stories**
```
Use event storming + customer journey
Invoke user-stories skill
Output: Complete user stories with acceptance criteria
Save to: outputs/11-user-stories.md
```

**Step 5.3: UI/UX Design**
```
Use user stories + customer personas
Invoke uiux-design skill
Output: UI/UX specifications and wireframes
Save to: outputs/12-uiux-design.md
```

### Stage 6: Prototype Development (15-20 min)

**Step 6.1: Prototype Guide**
```
Use all previous outputs
Invoke prototype-development skill
Output: Complete development guide with tech stack
Save to: outputs/13-prototype-development.md
```

## Execution Guidelines

### Sequential Processing
- Complete each stage before moving to next
- Pass previous outputs as context to next skills
- Validate outputs before proceeding
- Save all outputs to `outputs/` directory

### Context Accumulation
Each skill receives:
- All previous stage outputs
- Original MVP topic
- User's additional inputs or clarifications

### Progress Reporting
After each stage, report:
- ✅ Completed stage name
- 📄 Files generated
- ⏭️ Next stage preview
- ⏱️ Estimated time remaining

### Error Handling
If a skill fails:
1. Report the error clearly
2. Ask user for clarification/input
3. Retry the failed skill
4. Continue from where stopped

## Example Usage

**User Input:**
> "음식 배달 서비스 MVP를 기획해줘"

**System Response:**
```
🚀 AI 서비스 기획 자동화 시작
프로젝트: 음식 배달 서비스
예상 소요 시간: 80-100분

📋 Stage 1: 주제 및 고객 정의
  ✅ MVP 정의 완료 → outputs/01-mvp-definition.md
  ✅ 고객 분석 완료 → outputs/02-customer-analysis.md

📋 Stage 2: 문제 발견
  ✅ 시장 조사 완료 → outputs/03-market-research.md
  ✅ 고객 경험 조사 완료 → outputs/04-customer-experience.md
  ✅ 고객 여정 맵 완료 → outputs/05-journey-map.md
  ✅ 문제 가설 정의 완료 → outputs/06-problem-hypothesis.md

📋 Stage 3: 솔루션 탐색
  ✅ 아이디어 발상 완료 → outputs/07-ideation.md
  ✅ 솔루션 선정 완료 → outputs/08-solution-selection.md

📋 Stage 4: 비즈니스 모델
  ✅ 비즈니스 모델 완료 → outputs/09-business-model.md

📋 Stage 5: 제품 설계
  ✅ 이벤트 스토밍 완료 → outputs/10-event-storming.md
  ✅ 유저스토리 완료 → outputs/11-user-stories.md
  ✅ UI/UX 설계 완료 → outputs/12-uiux-design.md

📋 Stage 6: 프로토타입
  ✅ 프로토타입 가이드 완료 → outputs/13-prototype-development.md

🎉 서비스 기획 완료!
📁 모든 산출물: outputs/ 디렉토리
```

## Output Structure

```
outputs/
├── 01-mvp-definition.md
├── 02-customer-analysis.md
├── 03-market-research.md
├── 04-customer-experience.md
├── 05-journey-map.md
├── 06-problem-hypothesis.md
├── 07-ideation.md
├── 08-solution-selection.md
├── 09-business-model.md
├── 10-event-storming.md
├── 11-user-stories.md
├── 12-uiux-design.md
└── 13-prototype-development.md
```

## Tips for Best Results

1. **Be Specific**: Provide detailed MVP topic (domain, target users, core features)
2. **Stay Engaged**: Review intermediate outputs and provide feedback
3. **Ask Questions**: Request clarification at any stage
4. **Iterate**: Request refinements on any stage output
5. **Save Work**: All outputs are saved incrementally

## Alternative Usage

### Partial Workflow
Run only specific stages:
- "Stage 1-2만 실행해줘" (Definition + Problem Discovery)
- "Stage 5부터 시작해줘" (Start from Product Design)

### Single Skill
Run individual skills directly:
- "고객 여정 맵만 그려줘" → Use journey-mapping skill alone
- "이벤트 스토밍만 해줘" → Use event-storming skill alone

### Resume Workflow
Continue from previous work:
- "이전 기획에서 Stage 4부터 계속해줘"
- Provide previous outputs location
