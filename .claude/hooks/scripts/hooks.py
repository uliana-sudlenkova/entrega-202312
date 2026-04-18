#!/usr/bin/env python3
"""
Claude Code Hook Handler — ulyana-web
Logs hook events and warns on dangerous Bash commands.
Supports all Claude Code hook events.
"""

import sys
import json
import subprocess
import re
import platform
import argparse
from pathlib import Path


# ===== DANGEROUS BASH PATTERNS =====
# Commands that require extra caution in this project
DANGEROUS_PATTERNS = [
    (r'rm\s+-rf', "⚠️  DANGER: recursive delete detected"),
    (r'git\s+push\s+.*--force', "⚠️  DANGER: force push detected"),
    (r'git\s+reset\s+--hard', "⚠️  DANGER: hard reset detected"),
    (r'netlify\s+env:set', "⚠️  WARNING: modifying Netlify environment variables"),
    (r'STRIPE_SECRET_KEY', "🚨 CRITICAL: Stripe secret key referenced in shell command"),
]

# ===== HOOK EVENT → LOG LABEL =====
HOOK_LABELS = {
    "PreToolUse": "pre_tool",
    "PostToolUse": "post_tool",
    "PostToolUseFailure": "post_tool_failure",
    "UserPromptSubmit": "user_prompt",
    "Notification": "notification",
    "Stop": "stop",
    "SubagentStart": "subagent_start",
    "SubagentStop": "subagent_stop",
    "PreCompact": "pre_compact",
    "PostCompact": "post_compact",
    "SessionStart": "session_start",
    "SessionEnd": "session_end",
    "Setup": "setup",
    "PermissionRequest": "permission_request",
    "PermissionDenied": "permission_denied",
    "TeammateIdle": "teammate_idle",
    "TaskCreated": "task_created",
    "TaskCompleted": "task_completed",
    "ConfigChange": "config_change",
    "WorktreeCreate": "worktree_create",
    "WorktreeRemove": "worktree_remove",
    "InstructionsLoaded": "instructions_loaded",
    "Elicitation": "elicitation",
    "ElicitationResult": "elicitation_result",
    "StopFailure": "stop_failure",
    "CwdChanged": "cwd_changed",
    "FileChanged": "file_changed",
}


def load_config():
    """Load hooks config with local override support."""
    script_dir = Path(__file__).parent
    config_dir = script_dir.parent / "config"

    config = {}
    for fname in ["hooks-config.json", "hooks-config.local.json"]:
        path = config_dir / fname
        if path.exists():
            try:
                with open(path, encoding="utf-8") as f:
                    config.update(json.load(f))
            except Exception:
                pass
    return config


def is_hook_disabled(event_name, config):
    key = f"disable{event_name}Hook"
    return config.get(key, False)


def log_event(hook_data, agent_name=None):
    """Append event to hooks-log.jsonl."""
    config = load_config()
    if config.get("disableLogging", False):
        return

    script_dir = Path(__file__).parent
    logs_dir = script_dir.parent / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    entry = {k: v for k, v in hook_data.items()
             if k not in ("transcript_path", "cwd")}
    if agent_name:
        entry["agent"] = agent_name

    log_path = logs_dir / "hooks-log.jsonl"
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"Log error: {e}", file=sys.stderr)


def check_dangerous_bash(hook_data):
    """
    For PreToolUse + Bash: scan command for dangerous patterns.
    Prints warnings to stderr (visible in Claude Code output).
    Returns True if a critical pattern was found (to block via exit code).
    """
    if hook_data.get("hook_event_name") != "PreToolUse":
        return False
    if hook_data.get("tool_name") != "Bash":
        return False

    command = hook_data.get("tool_input", {}).get("command", "")
    if not command:
        return False

    critical = False
    for pattern, warning in DANGEROUS_PATTERNS:
        if re.search(pattern, command):
            print(warning, file=sys.stderr)
            if "CRITICAL" in warning:
                critical = True

    return critical


def notify_mac(message):
    """Send a macOS notification (silent fallback if unavailable)."""
    try:
        subprocess.Popen(
            ["osascript", "-e",
             f'display notification "{message}" with title "Claude Code"'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass


def handle_event(hook_data, agent_name=None):
    """Main event dispatcher."""
    event = hook_data.get("hook_event_name", "")

    config = load_config()
    if not agent_name and is_hook_disabled(event, config):
        return

    log_event(hook_data, agent_name)

    # macOS notifications for key lifecycle events
    if platform.system() == "Darwin":
        if event == "Stop":
            notify_mac("Claude Code finished")
        elif event == "SubagentStop":
            agent = hook_data.get("agent_name", "agent")
            notify_mac(f"Subagent done: {agent}")
        elif event == "TaskCompleted":
            notify_mac("Task completed")
        elif event == "PermissionDenied":
            notify_mac("⚠️ Permission denied — review required")

    # Security check on Bash commands
    if event == "PreToolUse":
        check_dangerous_bash(hook_data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", type=str, default=None)
    args = parser.parse_args()

    stdin_content = sys.stdin.read().strip()
    if not stdin_content:
        sys.exit(0)

    try:
        hook_data = json.loads(stdin_content)
    except json.JSONDecodeError as e:
        print(f"Hook JSON parse error: {e}", file=sys.stderr)
        sys.exit(0)

    handle_event(hook_data, agent_name=args.agent)
    sys.exit(0)


if __name__ == "__main__":
    main()
