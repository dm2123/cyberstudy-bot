"""Light automatic moderation — warning only.

Rules in this skeleton:
  1. Spam repetition: same message 3+ times in 60 seconds, or
     6+ messages in 10 seconds from one user -> warning.
  2. Bad-word filter: message contains a listed word -> warning.

Deliberately NO automatic kick, ban, timeout, or message deletion.
A human moderator decides any stronger action.

The word list is intentionally small. Server admins can edit BAD_WORDS
in this file for their own community standards. Matching is
case-insensitive and substring-based, so keep the list specific.
"""

import time
from collections import defaultdict, deque

# Admins: edit this list to match your community standards.
BAD_WORDS = [
    "fuck",
    "bitch",
    "chutiya",
    "madarchod",
    "behenchod",
]

SPAM_SAME_MESSAGE_COUNT = 3
SPAM_SAME_MESSAGE_WINDOW_SEC = 60
SPAM_BURST_COUNT = 6
SPAM_BURST_WINDOW_SEC = 10


def contains_bad_word(text: str) -> str | None:
    """Return the first matched bad word, or None. Never returns the message."""
    lowered = text.lower()
    for word in BAD_WORDS:
        if word in lowered:
            return word
    return None


class SpamTracker:
    """In-memory, per-user message history. No database, no persistence."""

    def __init__(self):
        self._history = defaultdict(deque)  # user_id -> deque[(timestamp, text)]

    def record(self, user_id: int, text: str, now: float | None = None) -> str | None:
        """Record a message. Return 'repeat' / 'burst' if spam, else None."""
        now = time.time() if now is None else now
        history = self._history[user_id]
        history.append((now, text))
        # Drop anything older than the longest window we care about.
        while history and now - history[0][0] > SPAM_SAME_MESSAGE_WINDOW_SEC:
            history.popleft()

        recent_same = [t for t, msg in history if msg == text]
        if len(recent_same) >= SPAM_SAME_MESSAGE_COUNT:
            return "repeat"
        recent_burst = [t for t, _ in history if now - t <= SPAM_BURST_WINDOW_SEC]
        if len(recent_burst) >= SPAM_BURST_COUNT:
            return "burst"
        return None


def warning_for(kind: str) -> str:
    if kind == "repeat":
        return (
            "⚠️ Please same message baar-baar mat bhejo (spam). "
            "Ek baar likhna kaafi hai, koi reply karega."
        )
    if kind == "burst":
        return (
            "⚠️ Thoda slow — bahut jaldi-jaldi messages aa rahe hain. "
            "Ek message likhkar reply ka wait karo."
        )
    if kind == "bad_word":
        return (
            "⚠️ Please respectful language use karo. "
            "Gaali / abusive words yahan allowed nahi hain."
        )
    return "⚠️ Please community rules ka dhyan rakho."
