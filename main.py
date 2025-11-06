#!/usr/bin/env python3
"""
AI 서비스 기획 자동화 시스템
Main Entry Point
"""

import asyncio
import sys
import os
from typing import Optional
import argparse

from agents.orchestrator import PlanningOrchestrator


def setup_environment():
    """환경 설정"""
    # .env 파일에서 환경변수 로드
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("Warning: python-dotenv not installed. Using system environment variables.")

    # ANTHROPIC_API_KEY 확인
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n⚠️  Warning: ANTHROPIC_API_KEY not found!")
        print("Please set your Anthropic API key:")
        print("  export ANTHROPIC_API_KEY='your-api-key'")
        print("\nOr create a .env file with:")
        print("  ANTHROPIC_API_KEY=your-api-key")
        print("\n🔧 Running in MOCK MODE (for testing structure only)\n")


async def run_full_planning(project_name: str, user_input: Optional[str] = None):
    """전체 기획 프로세스 실행"""
    orchestrator = PlanningOrchestrator(project_name)

    print(f"\n🎯 프로젝트: {project_name}")
    if user_input:
        print(f"💭 사용자 입력: {user_input}")

    result = await orchestrator.run_full_workflow(user_input)

    if result["success"]:
        print("\n" + "="*60)
        print("📁 생성된 파일 목록:")
        print("="*60)
        print(f"  📂 outputs/{project_name}/")
        print(f"    ├── 00_summary_report.md")
        print(f"    ├── 01_mvp_topic.md")
        print(f"    ├── 02_target_customer.md")
        print(f"    ├── 03_market_research.md")
        print(f"    ├── 04_customer_experience.md")
        print(f"    ├── 05_journey_map.md")
        print(f"    ├── 06_problem_hypothesis.md")
        print(f"    ├── 07_ideation.md")
        print(f"    ├── 08_solution_selection.md")
        print(f"    ├── 09_business_model.md")
        print(f"    ├── 10_event_storming.md")
        print(f"    ├── 11_user_stories.md")
        print(f"    ├── 12_uiux_design.md")
        print(f"    ├── 13_prototype_guide.md")
        print(f"    └── {project_name}_state.json")
        print("="*60 + "\n")
    else:
        print(f"\n❌ Error: {result.get('error')}")
        sys.exit(1)


async def run_single_agent(project_name: str, agent_name: str, user_input: Optional[str] = None):
    """단일 에이전트만 실행"""
    orchestrator = PlanningOrchestrator(project_name)

    print(f"\n🎯 프로젝트: {project_name}")
    print(f"🤖 에이전트: {agent_name}")

    # Load existing state if available
    state_file = f"outputs/{project_name}_state.json"
    if os.path.exists(state_file):
        orchestrator.state.load(state_file)
        print(f"📥 기존 상태 로드: {state_file}")

    context = {"user_input": user_input} if user_input else None
    result = await orchestrator.run_single_agent(agent_name, context)

    if result["success"]:
        print(f"\n✅ {agent_name} 완료")
        print(f"📁 결과 저장: outputs/{project_name}/{agent_name}_result.md")
    else:
        print(f"\n❌ Error: {result.get('error')}")
        sys.exit(1)


def list_agents():
    """사용 가능한 에이전트 목록 출력"""
    orchestrator = PlanningOrchestrator("temp")
    agents = orchestrator.list_agents()

    print("\n" + "="*60)
    print("🤖 사용 가능한 에이전트:")
    print("="*60)

    agent_descriptions = {
        "mvp": "MVP 주제 정의",
        "customer": "대상 고객 정의 (JTBD)",
        "market_research": "시장 조사",
        "customer_experience": "고객 경험 조사 (인터뷰/관찰/체험)",
        "journey_map": "User Journey Map 작성",
        "problem_hypothesis": "문제 가설 정의",
        "ideation": "아이디어 생성",
        "solution_selection": "솔루션 평가 및 선정",
        "business_model": "비즈니스 모델 기획 (Lean Canvas)",
        "event_storming": "이벤트 스토밍 및 시퀀스 다이어그램",
        "user_story": "유저스토리 작성",
        "uiux": "UI/UX 설계서 작성",
        "prototype": "프로토타입 개발 가이드"
    }

    for i, agent in enumerate(agents, 1):
        desc = agent_descriptions.get(agent, "")
        print(f"  {i:2d}. {agent:20s} - {desc}")

    print("="*60 + "\n")


def interactive_mode():
    """대화형 모드"""
    print("\n" + "="*60)
    print("🎨 AI 서비스 기획 자동화 시스템")
    print("="*60 + "\n")

    project_name = input("프로젝트 이름을 입력하세요: ").strip()
    if not project_name:
        project_name = "my_project"

    print("\n선택하세요:")
    print("  1. 전체 기획 프로세스 실행")
    print("  2. 특정 에이전트만 실행")
    print("  3. 에이전트 목록 보기")

    choice = input("\n선택 (1-3): ").strip()

    if choice == "1":
        user_input = input("\nMVP 주제나 아이디어를 입력하세요 (선택사항): ").strip()
        asyncio.run(run_full_planning(project_name, user_input or None))

    elif choice == "2":
        list_agents()
        agent_name = input("에이전트 이름을 입력하세요: ").strip()
        user_input = input("추가 입력 (선택사항): ").strip()
        asyncio.run(run_single_agent(project_name, agent_name, user_input or None))

    elif choice == "3":
        list_agents()

    else:
        print("잘못된 선택입니다.")


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="AI 서비스 기획 자동화 시스템",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 전체 기획 프로세스 실행
  python main.py --project my_service --full

  # 사용자 입력과 함께 실행
  python main.py --project my_service --full --input "음식 배달 서비스"

  # 특정 에이전트만 실행
  python main.py --project my_service --agent mvp --input "여행 추천"

  # 대화형 모드
  python main.py --interactive

  # 에이전트 목록 보기
  python main.py --list
        """
    )

    parser.add_argument("--project", "-p", type=str, default="my_project",
                       help="프로젝트 이름")
    parser.add_argument("--full", "-f", action="store_true",
                       help="전체 기획 프로세스 실행")
    parser.add_argument("--agent", "-a", type=str,
                       help="실행할 에이전트 이름")
    parser.add_argument("--input", "-i", type=str,
                       help="사용자 입력 (MVP 주제, 아이디어 등)")
    parser.add_argument("--interactive", action="store_true",
                       help="대화형 모드로 실행")
    parser.add_argument("--list", "-l", action="store_true",
                       help="사용 가능한 에이전트 목록 보기")

    args = parser.parse_args()

    # Setup environment
    setup_environment()

    # Execute based on arguments
    if args.list:
        list_agents()

    elif args.interactive:
        interactive_mode()

    elif args.full:
        asyncio.run(run_full_planning(args.project, args.input))

    elif args.agent:
        asyncio.run(run_single_agent(args.project, args.agent, args.input))

    else:
        # No arguments provided, show help
        parser.print_help()
        print("\n💡 Tip: 대화형 모드를 사용하려면 --interactive 옵션을 사용하세요.\n")


if __name__ == "__main__":
    main()
