"""Planning Orchestrator - Coordinates all agents."""

import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime

from shared.state import SharedState
from shared.utils import save_to_file, create_markdown_report

from .mvp_agent import MVPAgent
from .customer_agent import CustomerAgent
from .market_research_agent import MarketResearchAgent
from .journey_map_agent import JourneyMapAgent
from .problem_hypothesis_agent import ProblemHypothesisAgent
from .ideation_agent import IdeationAgent
from .solution_selection_agent import SolutionSelectionAgent
from .business_model_agent import BusinessModelAgent
from .user_story_agent import UserStoryAgent
from .uiux_agent import UIUXAgent
from .prototype_agent import PrototypeAgent


class PlanningOrchestrator:
    """
    모든 에이전트를 조정하고 워크플로우를 관리하는 오케스트레이터
    """

    def __init__(self, project_name: str = "my_project"):
        self.project_name = project_name
        self.state = SharedState(project_name)

        # Initialize all agents
        self.agents = {
            "mvp": MVPAgent(),
            "customer": CustomerAgent(),
            "market_research": MarketResearchAgent(),
            "journey_map": JourneyMapAgent(),
            "problem_hypothesis": ProblemHypothesisAgent(),
            "ideation": IdeationAgent(),
            "solution_selection": SolutionSelectionAgent(),
            "business_model": BusinessModelAgent(),
            "user_story": UserStoryAgent(),
            "uiux": UIUXAgent(),
            "prototype": PrototypeAgent(),
        }

        # Define workflow stages
        self.workflow = [
            {
                "stage": "1. 주제 및 고객 정의",
                "agents": ["mvp", "customer"],
                "description": "MVP 주제와 대상 고객을 정의합니다."
            },
            {
                "stage": "2. 문제 발견",
                "agents": ["market_research", "journey_map", "problem_hypothesis"],
                "description": "시장 조사, 고객 여정 분석, 문제 가설을 정의합니다."
            },
            {
                "stage": "3. 솔루션 탐색",
                "agents": ["ideation", "solution_selection"],
                "description": "아이디어를 생성하고 최적의 솔루션을 선정합니다."
            },
            {
                "stage": "4. 비즈니스 모델",
                "agents": ["business_model"],
                "description": "비즈니스 모델을 기획합니다."
            },
            {
                "stage": "5. 제품 설계",
                "agents": ["user_story", "uiux"],
                "description": "유저스토리와 UI/UX를 설계합니다."
            },
            {
                "stage": "6. 프로토타입",
                "agents": ["prototype"],
                "description": "프로토타입 개발 가이드를 생성합니다."
            }
        ]

    async def run_full_workflow(self, user_input: Optional[str] = None) -> Dict[str, Any]:
        """
        전체 워크플로우를 실행합니다.

        Args:
            user_input: 사용자의 초기 입력 (MVP 주제 관련)

        Returns:
            전체 워크플로우 실행 결과
        """
        print(f"\n{'='*60}")
        print(f"🚀 서비스 기획 자동화 시작")
        print(f"프로젝트: {self.project_name}")
        print(f"{'='*60}\n")

        start_time = datetime.now()
        results = {}

        try:
            # Stage 1: MVP 주제 및 고객 정의
            print(f"\n{'='*60}")
            print(f"📋 Stage 1: 주제 및 고객 정의")
            print(f"{'='*60}\n")

            # MVP Agent
            mvp_result = await self.run_agent("mvp", {"user_input": user_input})
            if mvp_result["success"]:
                self.state.update("mvp_topic", mvp_result["content"])
                self.save_result("01_mvp_topic.md", mvp_result["content"])
                results["mvp_topic"] = mvp_result
                print("✅ MVP 주제 정의 완료")
            else:
                print("❌ MVP 주제 정의 실패")
                return {"success": False, "error": "MVP agent failed"}

            # Customer Agent
            customer_result = await self.run_agent("customer",
                                                   self.state.get_context_for_agent("customer"))
            if customer_result["success"]:
                self.state.update("target_customer", customer_result["content"])
                self.save_result("02_target_customer.md", customer_result["content"])
                results["target_customer"] = customer_result
                print("✅ 대상 고객 정의 완료")
            else:
                print("❌ 대상 고객 정의 실패")

            # Stage 2: 문제 발견
            print(f"\n{'='*60}")
            print(f"🔍 Stage 2: 문제 발견")
            print(f"{'='*60}\n")

            # Market Research Agent
            market_result = await self.run_agent("market_research",
                                                 self.state.get_context_for_agent("market_research"))
            if market_result["success"]:
                self.state.update("market_research", market_result["content"])
                self.save_result("03_market_research.md", market_result["content"])
                results["market_research"] = market_result
                print("✅ 시장 조사 완료")

            # Journey Map Agent
            journey_result = await self.run_agent("journey_map",
                                                  self.state.get_context_for_agent("journey_map"))
            if journey_result["success"]:
                self.state.update("journey_map", journey_result["content"])
                self.save_result("04_journey_map.md", journey_result["content"])
                results["journey_map"] = journey_result
                print("✅ User Journey Map 작성 완료")

            # Problem Hypothesis Agent
            problem_result = await self.run_agent("problem_hypothesis",
                                                  self.state.get_context_for_agent("problem_hypothesis"))
            if problem_result["success"]:
                self.state.update("problem_hypothesis", problem_result["content"])
                self.save_result("05_problem_hypothesis.md", problem_result["content"])
                results["problem_hypothesis"] = problem_result
                print("✅ 문제 가설 정의 완료")

            # Stage 3: 솔루션 탐색
            print(f"\n{'='*60}")
            print(f"💡 Stage 3: 솔루션 탐색")
            print(f"{'='*60}\n")

            # Ideation Agent
            ideation_result = await self.run_agent("ideation",
                                                   self.state.get_context_for_agent("ideation"))
            if ideation_result["success"]:
                self.state.update("ideation_results", ideation_result["content"])
                self.save_result("06_ideation.md", ideation_result["content"])
                results["ideation"] = ideation_result
                print("✅ 아이디에이션 완료")

            # Solution Selection Agent
            selection_result = await self.run_agent("solution_selection",
                                                    self.state.get_context_for_agent("solution_selection"))
            if selection_result["success"]:
                self.state.update("selected_solution", selection_result["content"])
                self.save_result("07_solution_selection.md", selection_result["content"])
                results["solution_selection"] = selection_result
                print("✅ 솔루션 선정 완료")

            # Stage 4: 비즈니스 모델
            print(f"\n{'='*60}")
            print(f"💼 Stage 4: 비즈니스 모델")
            print(f"{'='*60}\n")

            business_result = await self.run_agent("business_model",
                                                   self.state.get_context_for_agent("business_model"))
            if business_result["success"]:
                self.state.update("business_model", business_result["content"])
                self.save_result("08_business_model.md", business_result["content"])
                results["business_model"] = business_result
                print("✅ 비즈니스 모델 기획 완료")

            # Stage 5: 제품 설계
            print(f"\n{'='*60}")
            print(f"🎨 Stage 5: 제품 설계")
            print(f"{'='*60}\n")

            # User Story Agent
            story_result = await self.run_agent("user_story",
                                                self.state.get_context_for_agent("user_story"))
            if story_result["success"]:
                self.state.update("user_stories", story_result["content"])
                self.save_result("09_user_stories.md", story_result["content"])
                results["user_stories"] = story_result
                print("✅ 유저스토리 작성 완료")

            # UI/UX Agent
            uiux_result = await self.run_agent("uiux",
                                               self.state.get_context_for_agent("uiux"))
            if uiux_result["success"]:
                self.state.update("uiux_design", uiux_result["content"])
                self.save_result("10_uiux_design.md", uiux_result["content"])
                results["uiux"] = uiux_result
                print("✅ UI/UX 설계 완료")

            # Stage 6: 프로토타입
            print(f"\n{'='*60}")
            print(f"🛠️  Stage 6: 프로토타입")
            print(f"{'='*60}\n")

            prototype_result = await self.run_agent("prototype",
                                                    self.state.get_context_for_agent("prototype"))
            if prototype_result["success"]:
                self.state.update("prototype", prototype_result["content"])
                self.save_result("11_prototype_guide.md", prototype_result["content"])
                results["prototype"] = prototype_result
                print("✅ 프로토타입 가이드 생성 완료")

            # Save final state
            state_file = self.state.save()
            print(f"\n✅ 전체 상태 저장 완료: {state_file}")

            # Generate summary report
            self.generate_summary_report(results)

            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            print(f"\n{'='*60}")
            print(f"🎉 서비스 기획 자동화 완료!")
            print(f"소요 시간: {duration:.2f}초")
            print(f"출력 디렉토리: outputs/{self.project_name}/")
            print(f"{'='*60}\n")

            return {
                "success": True,
                "results": results,
                "duration": duration,
                "output_dir": f"outputs/{self.project_name}/"
            }

        except Exception as e:
            print(f"\n❌ 워크플로우 실행 중 오류 발생: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }

    async def run_agent(self, agent_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        특정 에이전트를 실행합니다.

        Args:
            agent_name: 실행할 에이전트 이름
            context: 에이전트 실행 컨텍스트

        Returns:
            에이전트 실행 결과
        """
        if agent_name not in self.agents:
            return {
                "success": False,
                "error": f"Agent {agent_name} not found"
            }

        agent = self.agents[agent_name]
        print(f"🤖 {agent.name} 실행 중...")

        try:
            self.state.update_workflow_status(agent_name, "running", "실행 중")
            result = await agent.execute(context)
            self.state.update_workflow_status(agent_name, "completed", "완료")
            return result
        except Exception as e:
            self.state.update_workflow_status(agent_name, "failed", str(e))
            return {
                "success": False,
                "error": str(e)
            }

    def save_result(self, filename: str, content: str) -> str:
        """결과를 파일로 저장합니다."""
        directory = f"outputs/{self.project_name}"
        filepath = save_to_file(content, filename, directory)
        return filepath

    def generate_summary_report(self, results: Dict[str, Any]) -> str:
        """전체 결과를 요약한 리포트를 생성합니다."""
        sections = {
            "프로젝트 개요": f"프로젝트명: {self.project_name}",
            "실행 결과": self._format_results_summary(results)
        }

        report = create_markdown_report(
            title=f"{self.project_name} - 서비스 기획 자동화 결과",
            sections=sections
        )

        filepath = self.save_result("00_summary_report.md", report)
        print(f"📊 요약 리포트 생성 완료: {filepath}")
        return filepath

    def _format_results_summary(self, results: Dict[str, Any]) -> str:
        """결과 요약 포맷팅"""
        summary = "## 완료된 단계\n\n"

        for key, result in results.items():
            status = "✅" if result.get("success") else "❌"
            summary += f"{status} {key}\n"

        return summary

    async def run_single_agent(self, agent_name: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        단일 에이전트만 실행합니다.

        Args:
            agent_name: 실행할 에이전트 이름
            context: 에이전트 실행 컨텍스트 (없으면 state에서 가져옴)

        Returns:
            에이전트 실행 결과
        """
        if context is None:
            context = self.state.get_context_for_agent(agent_name)

        result = await self.run_agent(agent_name, context)

        if result["success"]:
            # Save result
            filename = f"{agent_name}_result.md"
            self.save_result(filename, result["content"])

        return result

    def get_workflow_status(self) -> Dict[str, Any]:
        """현재 워크플로우 상태를 반환합니다."""
        return self.state.state["workflow_status"]

    def list_agents(self) -> List[str]:
        """사용 가능한 에이전트 목록을 반환합니다."""
        return list(self.agents.keys())
