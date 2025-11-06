"""Base Agent class for all specialized agents."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import os
from anthropic import Anthropic


class BaseAgent(ABC):
    """
    모든 전문 에이전트의 기본 클래스
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if self.api_key:
            self.client = Anthropic(api_key=self.api_key)
        else:
            self.client = None
            print(f"Warning: ANTHROPIC_API_KEY not set. Agent {name} will run in mock mode.")

    @abstractmethod
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        에이전트의 핵심 실행 로직
        모든 하위 클래스는 이 메서드를 구현해야 함

        Args:
            context: 에이전트 실행에 필요한 컨텍스트 정보

        Returns:
            실행 결과를 담은 딕셔너리
        """
        pass

    @abstractmethod
    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        """
        에이전트의 프롬프트 템플릿 생성

        Args:
            context: 프롬프트 생성에 필요한 컨텍스트

        Returns:
            완성된 프롬프트 문자열
        """
        pass

    async def call_claude(self, prompt: str, max_tokens: int = 4000) -> str:
        """
        Claude API 호출

        Args:
            prompt: Claude에게 전달할 프롬프트
            max_tokens: 최대 토큰 수

        Returns:
            Claude의 응답
        """
        if not self.client:
            return f"[MOCK MODE] {self.name} would process: {prompt[:200]}..."

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=max_tokens,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            return f"Error calling Claude API: {str(e)}"

    def validate_context(self, context: Dict[str, Any], required_keys: list) -> bool:
        """
        컨텍스트에 필수 키가 있는지 검증

        Args:
            context: 검증할 컨텍스트
            required_keys: 필수 키 목록

        Returns:
            모든 필수 키가 있으면 True, 아니면 False
        """
        missing_keys = [key for key in required_keys if key not in context or context[key] is None]

        if missing_keys:
            print(f"Warning: {self.name} missing required context keys: {missing_keys}")
            return False

        return True

    def format_output(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        에이전트 출력을 표준 형식으로 포맷팅

        Args:
            content: 주요 출력 내용
            metadata: 추가 메타데이터

        Returns:
            표준 형식의 출력 딕셔너리
        """
        output = {
            "agent": self.name,
            "content": content,
            "success": True
        }

        if metadata:
            output["metadata"] = metadata

        return output

    def format_error(self, error_message: str) -> Dict[str, Any]:
        """
        에러를 표준 형식으로 포맷팅

        Args:
            error_message: 에러 메시지

        Returns:
            에러 정보가 담긴 딕셔너리
        """
        return {
            "agent": self.name,
            "content": error_message,
            "success": False,
            "error": True
        }

    async def pre_execute(self, context: Dict[str, Any]) -> bool:
        """
        실행 전 검증 및 준비 작업
        필요시 하위 클래스에서 오버라이드

        Args:
            context: 실행 컨텍스트

        Returns:
            준비가 완료되면 True, 아니면 False
        """
        return True

    async def post_execute(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        실행 후 처리 작업
        필요시 하위 클래스에서 오버라이드

        Args:
            result: 실행 결과

        Returns:
            후처리된 결과
        """
        return result

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __repr__(self) -> str:
        return f"BaseAgent(name='{self.name}', description='{self.description}')"
