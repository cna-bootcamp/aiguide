# 🚀 빠른 시작 가이드

## 5분 안에 시작하기

### 1단계: 설치 (1분)

```bash
# 의존성 설치
pip install anthropic python-dotenv pyyaml pydantic aiohttp
```

### 2단계: API Key 설정 (1분)

```bash
# 환경변수 설정
export ANTHROPIC_API_KEY='your-api-key-here'
```

또는 `.env` 파일 생성:

```bash
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

### 3단계: 실행 (1분)

```bash
# 대화형 모드로 시작
python main.py --interactive
```

또는 직접 실행:

```bash
# 전체 기획 자동 실행
python main.py --project my_first_project --full --input "음식 배달 서비스"
```

### 4단계: 결과 확인 (2분)

```bash
# 생성된 파일 확인
ls outputs/my_first_project/

# Markdown 파일 읽기
cat outputs/my_first_project/01_mvp_topic.md
```

## 🎯 사용 예시

### 예시 1: 간단한 프로젝트

```bash
python main.py --project food_app --full --input "건강식 배달"
```

**결과**: 12개의 상세한 기획 문서가 `outputs/food_app/`에 생성됩니다.

### 예시 2: 단계별 실행

```bash
# 1단계: MVP 주제만
python main.py --project travel_app --agent mvp --input "여행 계획"

# 2단계: 대상 고객 정의
python main.py --project travel_app --agent customer

# 3단계: 시장 조사
python main.py --project travel_app --agent market_research
```

### 예시 3: 대화형 모드

```bash
python main.py --interactive
```

그 다음:
1. 프로젝트 이름 입력: `my_awesome_app`
2. 선택: `1` (전체 프로세스)
3. MVP 아이디어 입력: `AI 기반 학습 플랫폼`

## 📊 생성되는 결과물

```
outputs/my_first_project/
├── 00_summary_report.md        ← 전체 요약
├── 01_mvp_topic.md             ← MVP 주제
├── 02_target_customer.md       ← 대상 고객 (JTBD)
├── 03_market_research.md       ← 시장 조사 (SWOT)
├── 04_journey_map.md           ← 고객 여정 지도
├── 05_problem_hypothesis.md    ← 문제 가설
├── 06_ideation.md              ← 10+ 아이디어
├── 07_solution_selection.md    ← ICE 스코어링 결과
├── 08_business_model.md        ← Lean Canvas
├── 09_user_stories.md          ← 20+ 유저스토리
├── 10_uiux_design.md           ← UI/UX 설계 (와이어프레임)
└── 11_prototype_guide.md       ← 개발 가이드 (코드 포함)
```

## 🎨 활용 방법

### 1. 문서 보기

VSCode나 Cursor에서:
- `Cmd/Ctrl + Shift + V`: Markdown 미리보기
- Markdown Preview Enhanced 플러그인 설치 권장

### 2. 기획서로 활용

생성된 문서를:
- 발표자료로 변환 (PPT, Google Slides)
- 팀과 공유
- 투자 제안서로 활용

### 3. 개발 시작

`11_prototype_guide.md`의:
- 기술 스택 참고
- API 설계 활용
- 코드 예시 복사

## 🔧 문제 해결

### API Key 오류

```
⚠️ Warning: ANTHROPIC_API_KEY not found!
```

**해결**: `.env` 파일 생성 또는 환경변수 설정

### 실행 안됨

```bash
# Python 버전 확인 (3.8+ 필요)
python --version

# 의존성 재설치
pip install -r requirements.txt --force-reinstall
```

## 💡 다음 단계

1. **결과물 검토**: 생성된 문서를 읽고 이해하기
2. **수정 및 보완**: 필요한 부분 직접 편집
3. **팀 공유**: 기획서를 팀원들과 공유
4. **프로토타입 개발**: 가이드에 따라 개발 시작

## 📚 더 알아보기

- [README_AGENTS.md](README_AGENTS.md): 전체 시스템 설명
- [README.md](README.md): 원본 기획 가이드
- [examples/](examples/): 예제 출력물

## 🤔 자주 묻는 질문

### Q: API 비용은 얼마나 드나요?

A: 전체 프로세스 1회 실행에 약 $1-2 정도 예상됩니다.

### Q: 오프라인에서도 사용 가능한가요?

A: Anthropic API를 사용하므로 인터넷 연결이 필요합니다.

### Q: 한국어로 결과가 나오나요?

A: 네, 프롬프트가 한국어로 작성되어 있어 한국어 결과가 생성됩니다.

### Q: 결과물을 상업적으로 사용할 수 있나요?

A: 생성된 결과물은 자유롭게 사용하실 수 있습니다.

## 🎉 완료!

이제 AI 에이전트를 활용한 서비스 기획 자동화를 시작할 준비가 되었습니다!

```bash
# 지금 바로 시작하세요!
python main.py --interactive
```
