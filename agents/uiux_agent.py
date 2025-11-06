"""UI/UX Design Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class UIUXAgent(BaseAgent):
    """
    UI/UX 설계서를 작성하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="UI/UX 설계 에이전트",
            description="사용자 경험과 인터페이스 설계서를 작성합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        user_stories = context.get("user_stories", "")
        selected_solution = context.get("selected_solution", "")

        return f"""당신은 UX/UI 디자인 전문가입니다.
유저스토리를 기반으로 상세한 UI/UX 설계서를 작성해주세요.

유저스토리:
{user_stories if user_stories else "유저스토리 없음"}

선정된 솔루션:
{selected_solution if selected_solution else "솔루션 정보 없음"}

다음 형식으로 UI/UX 설계서를 작성해주세요:

## 1. 디자인 원칙

### 핵심 원칙 5가지
1. **[원칙 1]**: [설명]
2. **[원칙 2]**: [설명]
3. **[원칙 3]**: [설명]
4. **[원칙 4]**: [설명]
5. **[원칙 5]**: [설명]

### 디자인 언어
- **톤앤매너**: [예: 친근하고 직관적인]
- **브랜드 키워드**: [3-5개 키워드]

## 2. 정보 구조 (Information Architecture)

### 사이트맵
```
Home
├── 기능 A
│   ├── 하위기능 A-1
│   └── 하위기능 A-2
├── 기능 B
│   ├── 하위기능 B-1
│   └── 하위기능 B-2
├── 마이페이지
│   ├── 프로필
│   └── 설정
└── 고객지원
```

### 내비게이션 구조
- **Primary Navigation**: [주요 메뉴]
- **Secondary Navigation**: [보조 메뉴]
- **Footer Navigation**: [하단 메뉴]

## 3. 화면 흐름도 (User Flow)

### Flow 1: [주요 기능 플로우]
```
시작
 ↓
[화면 1: 랜딩] → [화면 2: 선택]
 ↓                ↓
[화면 3: 입력] ← [화면 4: 확인]
 ↓
완료
```

**플로우 설명**:
1. Step 1: [설명]
2. Step 2: [설명]
3. Step 3: [설명]

### Flow 2: [다른 주요 기능]
[동일한 형식]

## 4. 와이어프레임 (Wireframe)

### 화면 1: 홈 화면
```
+----------------------------------+
|  [로고]    [메뉴] [메뉴] [메뉴]   |
+----------------------------------+
|                                  |
|     [Hero Section]               |
|     - 주요 메시지                 |
|     - CTA 버튼                   |
|                                  |
+----------------------------------+
|  [기능 1]  [기능 2]  [기능 3]    |
|   설명      설명      설명        |
+----------------------------------+
|                                  |
|     [주요 콘텐츠 영역]            |
|                                  |
+----------------------------------+
|  Footer                          |
+----------------------------------+
```

**주요 요소**:
- Header: [설명]
- Hero Section: [설명]
- Content Area: [설명]
- CTA: [설명]

### 화면 2: [화면명]
[동일한 형식으로 최소 5개 주요 화면]

## 5. 컴포넌트 라이브러리

### Button
- **Primary Button**: 주요 액션 (예: "시작하기", "구매하기")
- **Secondary Button**: 보조 액션
- **Text Button**: 텍스트 링크

### Form Elements
- Input Field
- Dropdown
- Checkbox / Radio
- Date Picker
- File Upload

### Cards
- Content Card
- Product Card
- User Card

### Navigation
- Top Navigation Bar
- Sidebar
- Breadcrumb
- Pagination

### Feedback
- Toast / Snackbar
- Modal / Dialog
- Alert / Error Messages
- Loading Spinner

## 6. 스타일 가이드

### 색상 팔레트
```
Primary Color: #[HEX] - 주요 브랜드 색상
Secondary Color: #[HEX] - 보조 색상
Accent Color: #[HEX] - 강조 색상

Text Colors:
- Primary Text: #[HEX]
- Secondary Text: #[HEX]
- Disabled Text: #[HEX]

Background:
- Light: #[HEX]
- Dark: #[HEX]

Status Colors:
- Success: #[HEX]
- Warning: #[HEX]
- Error: #[HEX]
- Info: #[HEX]
```

### 타이포그래피
```
Font Family: [폰트명]

Headings:
- H1: [크기]px, [굵기], [행간]
- H2: [크기]px, [굵기], [행간]
- H3: [크기]px, [굵기], [행간]

Body:
- Body 1: [크기]px, [굵기], [행간]
- Body 2: [크기]px, [굵기], [행간]

Caption: [크기]px, [굵기], [행간]
```

### 간격 (Spacing)
```
XS: 4px
S: 8px
M: 16px
L: 24px
XL: 32px
XXL: 48px
```

### 아이콘
- 아이콘 라이브러리: [예: Material Icons, Font Awesome]
- 크기: 16px, 24px, 32px

## 7. 반응형 디자인

### Breakpoints
```
Mobile: < 768px
Tablet: 768px - 1024px
Desktop: > 1024px
```

### 화면별 레이아웃
- **Mobile**: Single column, hamburger menu
- **Tablet**: Two columns, sidebar
- **Desktop**: Multi-column, full navigation

## 8. 인터랙션 디자인

### 애니메이션
- Transition Duration: 300ms
- Easing: ease-in-out
- Hover Effects: [설명]
- Click Feedback: [설명]

### 마이크로인터랙션
1. 버튼 클릭: [효과]
2. 폼 입력: [효과]
3. 페이지 전환: [효과]
4. 로딩: [효과]

## 9. 접근성 (Accessibility)

### WCAG 2.1 준수사항
- [ ] 키보드 네비게이션 지원
- [ ] 스크린 리더 호환
- [ ] 명도 대비 4.5:1 이상
- [ ] Alt text for images
- [ ] ARIA labels

### 사용성 테스트 체크리스트
- [ ] 5초 테스트 (첫인상)
- [ ] 태스크 완료율
- [ ] 오류율
- [ ] 만족도

## 10. 프로토타입 링크 (생성 예정)

**Figma**: [URL]
**Adobe XD**: [URL]
**InVision**: [URL]

## 11. 디자인 시스템 도구

추천 도구:
- **디자인**: Figma, Adobe XD
- **프로토타이핑**: Figma, InVision, Proto.io
- **협업**: Zeplin, Abstract
- **디자인 토큰**: Style Dictionary
- **컴포넌트 문서**: Storybook

ASCII 아트나 텍스트 기반 와이어프레임을 사용하여
각 화면의 레이아웃을 명확하게 표현해주세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """UI/UX 설계 실행"""
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
                    "design_system": True,
                    "responsive": True,
                    "accessibility": "WCAG 2.1"
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in UI/UX agent: {str(e)}")
