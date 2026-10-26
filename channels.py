"""Channel gating for the Discord AI-agent bot — pure logic, no Discord import.

The bot is only needed in learning / discussion channels. It stays silent
in announcement, rules-only, and admin/staff-only channels, so it never
spams important or admin-only places.

Matching is by channel-name substring, so exact Discord channel names do
not have to match perfectly: e.g. "eh-basics" matches, and a channel named
"eh-basics-chat" would also match because it contains "eh-basics".
The one exception is the welcome *event* (on_member_join in bot.py):
that still posts to the welcome channel even though commands are gated.

Explicit allow-list wins over the block-list: "welcome-and-rules" is in
ALLOWED_CHANNELS, so it is allowed even though it contains "rules".
A channel named just "rules" is blocked.
"""

ALLOWED_CHANNELS = [
    "welcome",
    "welcome-and-rules",
    "doubts-help",
    "eh-basics",
    "networking-linux",
    "kali-lab-setup",
    "footprinting-scanning-lab",
    "web-security-lab",
    "tools-and-ctf",
    "bca-study",
    "general-chat",
    "study-groups",
    # All-channels update (2026-10-26): user ordered bot in SABHI channels.
    # Study / EH / community / welcome channels from Dinesh server:
    "general-study",
    "dbms",
    "computer-graphics",
    "software-engineering",
    "maths-prob-stats",
    "python",
    "assignments-notes",
    "exam-updates",
    "certifications-free",
    "resources-books",
    "education",
    "resources",
    "cyber-basics",
    "kali-linux-labs",
    "web-security",
    "resources-certifications",
    "general",
    "meeting-plans",
    "introductions",
    "rules",
    "announcements",
]

# Channels the bot must ignore for commands (unless explicitly allowed above).
# NOTE: announcements/rules are now explicitly allowed per user order
# (bot only answers when a user sends a command there, it never auto-posts).
BLOCKED_CHANNEL_SUBSTRINGS = [
    "admin",
    "staff-only",
    "mod-only",
    "moderator",
]


def is_command_allowed(channel_name) -> bool:
    """Return True if the bot should answer commands in this channel.

    - Empty / missing name -> False (e.g. a DM has no server channel name).
    - Exact allow-list match -> True (explicit allow wins over blocks).
    - Any blocked substring (and not explicitly allowed) -> False.
    - Any allow-list entry contained in the name -> True (substring match).
    - Anything else -> False (default deny: bot stays silent elsewhere).
    """
    if not channel_name:
        return False
    name = str(channel_name).strip().lower()
    if not name:
        return False
    if name in ALLOWED_CHANNELS:
        return True
    if any(blocked in name for blocked in BLOCKED_CHANNEL_SUBSTRINGS):
        return False
    if any(allowed in name for allowed in ALLOWED_CHANNELS):
        return True
    return False


def is_welcome_channel(channel_name) -> bool:
    """True for channels the welcome event may post in."""
    if not channel_name:
        return False
    name = str(channel_name).strip().lower()
    return name in ("welcome", "welcome-and-rules") or "welcome" in name
