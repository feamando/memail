#!/usr/bin/env python3
"""
Config Loader - Centralized configuration management for memail

Loads configuration from config.yaml and environment variables.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Find project root (directory containing config.yaml)
def get_root_path() -> Path:
    """Find the project root directory."""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "config.yaml").exists():
            return parent
        if (parent / "CLAUDE.md").exists():
            return parent
    # Fallback: assume 3 levels up from this file
    return Path(__file__).resolve().parent.parent.parent.parent


ROOT_PATH = get_root_path()
CONFIG_PATH = ROOT_PATH / "config.yaml"


def load_config() -> Dict[str, Any]:
    """Load configuration from config.yaml."""
    if not CONFIG_PATH.exists():
        return {}

    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f) or {}


def get_config() -> Dict[str, Any]:
    """Get the full configuration dict."""
    return load_config()


def get_project_config() -> Dict[str, Any]:
    """Get project-specific configuration."""
    config = load_config()
    return config.get('project', {})


def get_gemini_config() -> Dict[str, Any]:
    """Get Gemini API configuration with resolved API key."""
    config = load_config()
    gemini_config = config.get('gemini', {})

    # Resolve API key from environment
    api_key_env = gemini_config.get('api_key_env', 'GEMINI_API_KEY')
    gemini_config['api_key'] = os.getenv(api_key_env)

    return gemini_config


def get_paths() -> Dict[str, Path]:
    """Get resolved paths from configuration."""
    config = load_config()
    paths_config = config.get('paths', {})

    return {
        'root': ROOT_PATH,
        'source': ROOT_PATH / paths_config.get('source', 'src'),
        'tests': ROOT_PATH / paths_config.get('tests', 'tests'),
        'docs': ROOT_PATH / paths_config.get('docs', 'docs'),
        'brain': ROOT_PATH / paths_config.get('brain', 'AI_Guidance/Brain'),
        'tools': ROOT_PATH / paths_config.get('tools', 'AI_Guidance/Tools'),
    }


def get_ralph_config() -> Dict[str, Any]:
    """Get Ralph (long-running tasks) configuration."""
    config = load_config()
    ralph_config = config.get('ralph', {})

    # Resolve state file path
    state_file = ralph_config.get('state_file', '.ralph_state.json')
    ralph_config['state_path'] = ROOT_PATH / state_file

    return ralph_config


def get_testing_config() -> Dict[str, Any]:
    """Get testing configuration."""
    config = load_config()
    return config.get('testing', {
        'framework': 'pytest',
        'command': 'pytest',
        'coverage_threshold': 80
    })


def get_quality_config() -> Dict[str, Any]:
    """Get code quality tools configuration."""
    config = load_config()
    return config.get('quality', {
        'linter': 'ruff',
        'formatter': 'black',
        'type_checker': 'mypy'
    })


def get_git_config() -> Dict[str, Any]:
    """Get git configuration."""
    config = load_config()
    return config.get('git', {
        'main_branch': 'main',
        'commit_style': 'conventional',
        'require_tests': True
    })


# Convenience exports
__all__ = [
    'get_root_path',
    'get_config',
    'get_project_config',
    'get_gemini_config',
    'get_paths',
    'get_ralph_config',
    'get_testing_config',
    'get_quality_config',
    'get_git_config',
    'ROOT_PATH',
]
