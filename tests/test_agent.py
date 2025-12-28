"""Tests for the Pivot Advisor agent."""

from pathlib import Path

def test_system_prompt_exists():
    prompt_path = Path(__file__).parent.parent / "src" / "ideation_agent_pivot_advisor" / "prompts" / "system.md"
    assert prompt_path.exists()

def test_cli_import():
    from ideation_agent_pivot_advisor.main import cli
    assert cli is not None
