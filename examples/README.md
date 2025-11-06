# 예제 출력물

이 디렉토리에는 에이전트 시스템이 생성한 예제 결과물이 저장됩니다.

## 사용 예시

```bash
# 예제 프로젝트 실행
python main.py --project food_delivery_example --full --input "음식 배달 서비스"

# 결과는 outputs/food_delivery_example/ 에 생성됩니다
```

## 예제 프로젝트 아이디어

1. **음식 배달 서비스**
   ```bash
   python main.py --project food_delivery --full --input "건강식 배달 플랫폼"
   ```

2. **여행 계획 서비스**
   ```bash
   python main.py --project travel_planner --full --input "AI 맞춤형 여행 일정 추천"
   ```

3. **구독 관리 서비스**
   ```bash
   python main.py --project subscription_manager --full --input "개인 구독 서비스 통합 관리"
   ```

4. **건강 관리 앱**
   ```bash
   python main.py --project health_tracker --full --input "개인 맞춤형 건강 진단 및 예측"
   ```

5. **학습 플랫폼**
   ```bash
   python main.py --project learning_platform --full --input "적응형 온라인 학습 플랫폼"
   ```

## 출력물 구조

```
outputs/
└── [project_name]/
    ├── 00_summary_report.md        # 전체 요약
    ├── 01_mvp_topic.md             # MVP 주제
    ├── 02_target_customer.md       # 대상 고객
    ├── 03_market_research.md       # 시장 조사
    ├── 04_journey_map.md           # 고객 여정
    ├── 05_problem_hypothesis.md    # 문제 가설
    ├── 06_ideation.md              # 아이디어
    ├── 07_solution_selection.md    # 솔루션 선정
    ├── 08_business_model.md        # 비즈니스 모델
    ├── 09_user_stories.md          # 유저스토리
    ├── 10_uiux_design.md           # UI/UX 설계
    ├── 11_prototype_guide.md       # 프로토타입 가이드
    └── [project_name]_state.json   # 상태 파일
```

## 출력물 활용 방법

### 1. Markdown 뷰어로 보기

VSCode나 Cursor에서:
- Mac: `Cmd + Shift + V`
- Windows: `Ctrl + Shift + V`

또는 Markdown Preview Enhanced 플러그인 사용

### 2. PDF로 변환

```bash
# pandoc 사용 (설치 필요)
pandoc outputs/[project]/01_mvp_topic.md -o mvp_topic.pdf
```

### 3. 발표자료 생성

생성된 문서를 기반으로:
- Google Slides
- PowerPoint
- Keynote

에서 발표자료 작성

### 4. 개발 시작

`11_prototype_guide.md`의 가이드를 따라 실제 개발 시작

## 팁

- 각 단계의 결과물을 검토하고 필요시 수정
- 특정 단계만 다시 실행 가능:
  ```bash
  python main.py --project my_project --agent ideation
  ```
- 상태 파일을 백업하여 버전 관리
