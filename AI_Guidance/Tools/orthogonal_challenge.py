#!/usr/bin/env python3
"""
Orthogonal Challenge - Devil's Advocate Review Tool

Generates counter-arguments and identifies blind spots in code,
architecture decisions, and implementations.

Usage:
    python orthogonal_challenge.py --file src/module.py
    python orthogonal_challenge.py --diff                    # Review staged changes
    python orthogonal_challenge.py --adr Architecture/decisions/001-choice.md
    python orthogonal_challenge.py --idea "Use microservices"
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional, List

# Add common to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'common'))
import config_loader

# Gemini configuration
gemini_config = config_loader.get_gemini_config()


def get_gemini_model():
    """Initialize Gemini model."""
    try:
        import google.generativeai as genai
    except ImportError:
        print("Error: google-generativeai not installed")
        print("Run: pip install google-generativeai")
        sys.exit(1)

    api_key = gemini_config.get('api_key')
    if not api_key:
        print("Error: GEMINI_API_KEY not set")
        sys.exit(1)

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(gemini_config.get('model', 'gemini-2.0-flash'))


def challenge_code(code: str, filename: str = "code") -> str:
    """Generate challenges for code."""
    model = get_gemini_model()

    prompt = f"""You are a senior code reviewer acting as a devil's advocate.
Your job is to challenge this code and identify potential issues.

File: {filename}

```
{code}
```

Provide a structured critique covering:

## Security Concerns
- Potential vulnerabilities (injection, auth, data exposure)
- Input validation gaps

## Performance Issues
- Algorithmic complexity concerns
- Resource usage (memory, connections, file handles)
- Potential bottlenecks

## Maintainability Risks
- Code complexity and readability
- Coupling and cohesion issues
- Missing error handling

## Edge Cases
- Boundary conditions not handled
- Race conditions or concurrency issues
- Failure modes not considered

## Alternative Approaches
- Simpler solutions that could work
- Standard library alternatives
- Patterns that might fit better

Be specific and cite line numbers or code snippets when relevant.
If the code is solid, say so briefly and note what makes it good.
"""

    response = model.generate_content(prompt)
    return response.text


def challenge_diff(diff: str) -> str:
    """Generate challenges for a diff."""
    model = get_gemini_model()

    prompt = f"""You are a senior code reviewer acting as a devil's advocate.
Review this diff and identify potential issues with the changes.

```diff
{diff}
```

Provide a structured critique covering:

## Breaking Changes
- API changes that could break consumers
- Behavior changes that could cause regressions

## Security Implications
- New attack surfaces introduced
- Security measures removed or weakened

## Testing Gaps
- What tests should accompany these changes?
- Edge cases that should be tested

## Code Quality
- Does this follow project conventions?
- Are there simpler approaches?

## Risks
- What could go wrong in production?
- Rollback considerations

Be specific and constructive. If the changes look good, note what's done well.
"""

    response = model.generate_content(prompt)
    return response.text


def challenge_adr(content: str, title: str = "ADR") -> str:
    """Generate challenges for an Architecture Decision Record."""
    model = get_gemini_model()

    prompt = f"""You are a senior architect acting as a devil's advocate.
Challenge this Architecture Decision Record and identify gaps or risks.

# {title}

{content}

Provide a structured critique covering:

## Assumptions to Challenge
- What assumptions is this decision based on?
- Which assumptions might be wrong?

## Alternatives Not Considered
- What other approaches could solve this problem?
- Why might those be better?

## Long-term Implications
- How does this scale?
- What technical debt does it create?
- Migration/reversal difficulty

## Operational Concerns
- Monitoring and observability gaps
- Failure modes and recovery
- On-call burden

## Dependencies and Risks
- External dependencies introduced
- Vendor lock-in concerns
- Team capability requirements

## Questions to Answer
- What questions should be answered before proceeding?
- What experiments could validate assumptions?

Be thorough but constructive. Suggest improvements where possible.
"""

    response = model.generate_content(prompt)
    return response.text


def challenge_idea(idea: str) -> str:
    """Generate challenges for an idea or proposal."""
    model = get_gemini_model()

    prompt = f"""You are a senior engineer acting as a devil's advocate.
Challenge this idea/proposal and identify potential issues.

IDEA: {idea}

Provide a structured critique covering:

## Core Assumptions
- What must be true for this to work?
- Which assumptions are risky?

## Why This Might Fail
- Technical obstacles
- Organizational obstacles
- Market/user obstacles

## Hidden Costs
- Implementation complexity
- Ongoing maintenance burden
- Opportunity cost

## Alternative Approaches
- Simpler solutions
- Proven alternatives
- Hybrid approaches

## Prerequisites
- What needs to be true first?
- Dependencies on other work

## Red Flags
- Signs this is going wrong
- When to abandon this approach

Be direct and specific. The goal is to strengthen the idea by identifying weaknesses.
"""

    response = model.generate_content(prompt)
    return response.text


def get_staged_diff() -> str:
    """Get git diff for staged changes."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached'],
            capture_output=True,
            text=True,
            cwd=config_loader.ROOT_PATH
        )
        return result.stdout
    except Exception as e:
        return f"Error getting diff: {e}"


def main():
    parser = argparse.ArgumentParser(description='Orthogonal Challenge - Devil\'s Advocate Review')
    parser.add_argument('--file', type=str, help='File to review')
    parser.add_argument('--diff', action='store_true', help='Review staged git diff')
    parser.add_argument('--adr', type=str, help='ADR file to challenge')
    parser.add_argument('--idea', type=str, help='Idea/proposal to challenge')
    parser.add_argument('--output', type=str, help='Output file (default: stdout)')

    args = parser.parse_args()

    result = None

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            file_path = config_loader.ROOT_PATH / args.file

        if not file_path.exists():
            print(f"Error: File not found: {args.file}")
            sys.exit(1)

        with open(file_path, 'r') as f:
            code = f.read()

        print(f"Challenging: {file_path}")
        result = challenge_code(code, file_path.name)

    elif args.diff:
        diff = get_staged_diff()
        if not diff.strip():
            print("No staged changes to review")
            print("Stage changes with: git add <files>")
            sys.exit(0)

        print("Challenging staged changes...")
        result = challenge_diff(diff)

    elif args.adr:
        adr_path = Path(args.adr)
        if not adr_path.exists():
            adr_path = config_loader.ROOT_PATH / "AI_Guidance/Brain/Architecture/decisions" / args.adr

        if not adr_path.exists():
            print(f"Error: ADR not found: {args.adr}")
            sys.exit(1)

        with open(adr_path, 'r') as f:
            content = f.read()

        print(f"Challenging ADR: {adr_path}")
        result = challenge_adr(content, adr_path.stem)

    elif args.idea:
        print(f"Challenging idea: {args.idea}")
        result = challenge_idea(args.idea)

    else:
        parser.print_help()
        sys.exit(0)

    if result:
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Output written to: {args.output}")
        else:
            print("\n" + "=" * 60)
            print("ORTHOGONAL CHALLENGE")
            print("=" * 60 + "\n")
            print(result)


if __name__ == "__main__":
    main()
