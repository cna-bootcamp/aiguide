"""Shared state management for agent collaboration."""

from typing import Dict, Any, Optional
from datetime import datetime
import json
import os


class SharedState:
    """
    중앙 집중식 상태 관리 클래스
    모든 에이전트가 작업 결과를 공유하고 참조할 수 있도록 합니다.
    """

    def __init__(self, project_name: str = "default_project"):
        self.project_name = project_name
        self.state: Dict[str, Any] = {
            "project_name": project_name,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "mvp_topic": None,
            "target_customer": None,
            "market_research": None,
            "customer_experience_stages": None,
            "observation_results": None,
            "experience_results": None,
            "interview_results": None,
            "journey_map": None,
            "problem_hypothesis": None,
            "problem_validation": None,
            "business_value": None,
            "direction": None,
            "ideation_results": None,
            "selected_solution": None,
            "business_model": None,
            "presentation": None,
            "user_stories": None,
            "uiux_design": None,
            "prototype": None,
            "workflow_status": {},
        }

    def update(self, key: str, value: Any) -> None:
        """상태 업데이트"""
        self.state[key] = value
        self.state["updated_at"] = datetime.now().isoformat()

    def get(self, key: str, default: Any = None) -> Any:
        """상태 조회"""
        return self.state.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """전체 상태 조회"""
        return self.state.copy()

    def save(self, filepath: Optional[str] = None) -> str:
        """상태를 파일로 저장"""
        if filepath is None:
            os.makedirs("outputs", exist_ok=True)
            filepath = f"outputs/{self.project_name}_state.json"

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)

        return filepath

    def load(self, filepath: str) -> None:
        """파일에서 상태 로드"""
        with open(filepath, 'r', encoding='utf-8') as f:
            self.state = json.load(f)

    def update_workflow_status(self, agent_name: str, status: str, message: str = "") -> None:
        """워크플로우 상태 업데이트"""
        self.state["workflow_status"][agent_name] = {
            "status": status,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self.state["updated_at"] = datetime.now().isoformat()

    def is_task_completed(self, task_key: str) -> bool:
        """특정 작업의 완료 여부 확인"""
        return self.state.get(task_key) is not None

    def get_context_for_agent(self, agent_type: str) -> Dict[str, Any]:
        """특정 에이전트가 필요로 하는 컨텍스트 반환"""
        context = {
            "project_name": self.state["project_name"],
            "mvp_topic": self.state.get("mvp_topic"),
            "target_customer": self.state.get("target_customer"),
        }

        # 에이전트 타입에 따라 필요한 추가 컨텍스트 제공
        if agent_type in ["market_research", "customer_experience"]:
            context["mvp_topic"] = self.state.get("mvp_topic")
            context["target_customer"] = self.state.get("target_customer")

        elif agent_type == "interview":
            context["market_research"] = self.state.get("market_research")
            context["customer_experience_stages"] = self.state.get("customer_experience_stages")

        elif agent_type == "journey_map":
            context["interview_results"] = self.state.get("interview_results")
            context["observation_results"] = self.state.get("observation_results")

        elif agent_type == "problem_hypothesis":
            context["journey_map"] = self.state.get("journey_map")
            context["interview_results"] = self.state.get("interview_results")

        elif agent_type == "problem_validation":
            context["problem_hypothesis"] = self.state.get("problem_hypothesis")

        elif agent_type == "business_value":
            context["problem_hypothesis"] = self.state.get("problem_hypothesis")
            context["problem_validation"] = self.state.get("problem_validation")

        elif agent_type == "direction":
            context["business_value"] = self.state.get("business_value")
            context["problem_hypothesis"] = self.state.get("problem_hypothesis")

        elif agent_type == "ideation":
            context["direction"] = self.state.get("direction")
            context["problem_hypothesis"] = self.state.get("problem_hypothesis")

        elif agent_type == "solution_selection":
            context["ideation_results"] = self.state.get("ideation_results")

        elif agent_type == "business_model":
            context["selected_solution"] = self.state.get("selected_solution")
            context["target_customer"] = self.state.get("target_customer")

        elif agent_type == "presentation":
            context["business_model"] = self.state.get("business_model")
            context["selected_solution"] = self.state.get("selected_solution")

        elif agent_type == "user_story":
            context["selected_solution"] = self.state.get("selected_solution")
            context["target_customer"] = self.state.get("target_customer")

        elif agent_type == "uiux":
            context["user_stories"] = self.state.get("user_stories")
            context["selected_solution"] = self.state.get("selected_solution")

        elif agent_type == "prototype":
            context["uiux_design"] = self.state.get("uiux_design")
            context["user_stories"] = self.state.get("user_stories")

        return context
