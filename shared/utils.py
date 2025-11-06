"""Utility functions for agent operations."""

import os
import json
from typing import Any, Dict
from datetime import datetime


def save_to_file(content: str, filename: str, directory: str = "outputs") -> str:
    """파일에 콘텐츠 저장"""
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def load_from_file(filepath: str) -> str:
    """파일에서 콘텐츠 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def save_json(data: Dict[str, Any], filename: str, directory: str = "outputs") -> str:
    """JSON 형식으로 데이터 저장"""
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return filepath


def load_json(filepath: str) -> Dict[str, Any]:
    """JSON 파일에서 데이터 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_markdown_report(title: str, sections: Dict[str, str]) -> str:
    """마크다운 리포트 생성"""
    report = f"# {title}\n\n"
    report += f"생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += "---\n\n"

    for section_title, content in sections.items():
        report += f"## {section_title}\n\n"
        report += f"{content}\n\n"

    return report


def extract_key_insights(text: str, max_length: int = 500) -> str:
    """텍스트에서 핵심 인사이트 추출 (간단한 요약)"""
    if len(text) <= max_length:
        return text

    # 간단한 문장 단위 요약 (실제로는 LLM을 사용하는 것이 좋음)
    sentences = text.split('.')
    summary = []
    current_length = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        if current_length + len(sentence) <= max_length:
            summary.append(sentence)
            current_length += len(sentence)
        else:
            break

    return '. '.join(summary) + '.'


def format_agent_output(agent_name: str, output: str, status: str = "completed") -> Dict[str, Any]:
    """에이전트 출력 포맷팅"""
    return {
        "agent": agent_name,
        "timestamp": datetime.now().isoformat(),
        "status": status,
        "output": output
    }
