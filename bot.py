"""College Ethical Hacking / Study Discord bot — AI-agent skeleton.

Free route only: discord.py + a small local rule-based knowledge base.
No paid API, no LLM call, no external service.

Channel-aware behaviour (see channels.py for the full documented list):
  - ALLOWED_CHANNELS — the bot answers commands / Q&A only in these
    channels (matched by channel-name substring, so exact Discord names
    do not have to match perfectly). Everywhere else it stays silent.
  - It IGNORES commands in announcements / rules-only / admin-only
    channels — except the welcome *event* (on_member_join), which still
    posts to the welcome channel.
  - ALLOWED_CHANNELS (re-exported here for visibility):
    welcome, welcome-and-rules, doubts-help, eh-basics, networking-linux,
    kali-lab-setup, footprinting-scanning-lab, web-security-lab,
    tools-and-ctf, bca-study, general-chat, study-groups.

Features:
  - Automatic welcome message for new members.
  - !help, !doubt <question>, !cyber <topic>, !eh <topic>, !subject <subject>
  - Light automatic moderation: warning only (no kick / ban / timeout).

Token safety (important):
  - Token ONLY comes from the environment variable DISCORD_BOT_TOKEN.
  - It is never hardcoded, never printed, and never written to any file.
  - If the variable is missing, the bot exits with an error message
    that does NOT contain the token (because there is none to show).

Run (after setup in README.md):
    pip install -r requirements.txt
    # Linux/macOS:
    export DISCORD_BOT_TOKEN="your-token-here"
    python bot.py
    # Windows (PowerShell):
    #   $env:DISCORD_BOT_TOKEN="your-token-here"; python bot.py
"""

import os
import sys

import discord
from discord.ext import commands

from channels import ALLOWED_CHANNELS, is_command_allowed
from knowledge import cyber_answer, doubt_answer, eh_answer, subject_answer
from moderation import SpamTracker, contains_bad_word, warning_for

# Re-exported so `from bot import ALLOWED_CHANNELS` works and the list is
# visible in this file too; the single source of truth is channels.py.
__all__ = ["ALLOWED_CHANNELS", "is_command_allowed"]

# Optional: load a local .env file if python-dotenv is installed.
# .env itself is NEVER committed (see .gitignore). The token still only
# lives in the environment; this just makes local runs easier.
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# --- Bot setup -----------------------------------------------------------
# message_content intent is needed to read commands like !doubt.
# It must also be enabled for the bot in the Discord Developer Portal
# (Bot -> Privileged Gateway Intents -> MESSAGE CONTENT INTENT).
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
spam_tracker = SpamTracker()

WELCOME_CHANNEL_NAMES = ("welcome", "welcome-and-rules", "general")


def find_welcome_channel(guild):
    """Prefer a welcome channel, else fall back to the first text channel."""
    for name in WELCOME_CHANNEL_NAMES:
        channel = discord.utils.get(guild.text_channels, name=name)
        if channel is not None:
            return channel
    return guild.text_channels[0] if guild.text_channels else None


def _channel_name(message_or_ctx) -> str:
    """Best-effort channel name; empty string for DMs / unknown channels."""
    channel = getattr(message_or_ctx, "channel", None)
    return getattr(channel, "name", "") or ""


# --- Automatic welcome (exception to command gating) ---------------------
@bot.event
async def on_member_join(member):
    channel = find_welcome_channel(member.guild)
    if channel is None:
        return
    await channel.send(
        f"👋 Welcome {member.mention} to **{member.guild.name}**!\n"
        "Ye college Professional Ethical Hacking learning community hai.\n"
        "• Rules padhne ke liye #welcome-and-rules dekho — lab-only rule sabse zaroori hai\n"
        "• Learning path ke liye `!eh eh-path` likho (allowed channels me)\n"
        "• Doubt ke liye `!doubt <sawal>` likho, ya #doubts-help me likho\n"
        "• Subject notes ke liye `!subject dbms` jaise command use karo\n"
        "• Ethical hacking sirf apne lab me seekho — real system / account / Wi-Fi par kabhi nahi."
    )


# --- Automatic moderation (warning only) + channel gating ---------------
# NOTE (2026-10-26): @ai activation was added, then user ordered to
# forget it and go back to the earlier way — so @ai handling is REMOVED.
# Bot works only via ! commands as before.
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    # Channel gating: outside allowed channels the bot stays silent —
    # no moderation warning and no command processing. This keeps
    # admin-only channels clean.
    if not is_command_allowed(_channel_name(message)):
        return
    # Commands must still work, so check moderation first, then process.
    bad = contains_bad_word(message.content)
    if bad:
        await message.channel.send(
            f"{message.author.mention} {warning_for('bad_word')}"
        )
    else:
        spam = spam_tracker.record(message.author.id, message.content)
        if spam:
            await message.channel.send(
                f"{message.author.mention} {warning_for(spam)}"
            )
    await bot.process_commands(message)


# --- Study / ethical hacking Q&A commands --------------------------------
# POWERFUL update (2026-10-26): more commands, same free rule-based bot,
# no paid LLM/API. !quiz, !plan, !lab, !resources added.
@bot.command(name="help")
async def help_command(ctx):
    await ctx.send(
        "**College Ethical Hacking Bot — Commands (allowed channels me hi)**\n"
        "• `!help` — ye list dikhata hai\n"
        "• `!doubt <sawal>` — apna doubt likho, jaise `!doubt phishing kya hai?`\n"
        "• `!cyber <topic>` — topics: basics, phishing, password, kali, nmap, web\n"
        "• `!eh <topic>` — ethical hacking path: eh-path, networking, linux, kali-lab, "
        "footprinting, scanning, web-lab, tools, ctf, certifications, book\n"
        "• `!subject <subject>` — subjects: dbms, cg, se, maths, python\n"
        "• `!quiz <subject>` — us subject ka 1 practice question\n"
        "• `!plan` — Dec 2026 exams ka simple study plan\n"
        "• `!lab` — lab safety checklist (Kali/DVWA/TryHackMe)\n"
        "• `!resources` — free resources ki list\n"
        "\nAgar jawab na mile to bot seedha bolega 'I don't know' — guess nahi karega.\n"
        "Ethical hacking: sirf authorised lab (apni Kali VM, DVWA, TryHackMe) par practice karo. "
        "Real system / account / Wi-Fi / college network par kabhi nahi."
    )


@bot.command(name="quiz")
async def quiz_command(ctx, *, subject: str = ""):
    quizzes = {
        "dbms": "Q: Primary Key aur Foreign Key me kya farak hai? Socho, phir `!subject dbms` se check karo.",
        "cg": "Q: Raster aur Vector image me kya farak hai? Socho, phir `!subject cg` se check karo.",
        "se": "Q: SDLC ke 5 stages kya hain? Socho, phir `!subject se` se check karo.",
        "maths": "Q: Coin toss me Head ki probability kitni hai? Socho, phir `!subject maths` se check karo.",
        "python": "Q: `for` loop aur `while` loop me kya farak hai? Socho, phir `!subject python` se check karo.",
    }
    key = subject.strip().lower()
    await ctx.send(quizzes.get(key, "Quiz subjects: dbms, cg, se, maths, python. Example: `!quiz dbms`"))


@bot.command(name="plan")
async def plan_command(ctx):
    await ctx.send(
        "**Dec 2026 Exams — Simple Study Plan**\n"
        "• Roz 2 subjects: 1 BCA subject + 1 EH/lab topic\n"
        "• Har subject: notes padho -> 10 practice Q&A -> 1 lab task\n"
        "• Maths backlog (1st sem) ke liye roz 30 min alag rakho\n"
        "• Exam se 1 hafta pehle: sirf revision + past questions, naya topic mat chhedo\n"
        "• Lab rule: sirf apni Kali VM / DVWA / TryHackMe par practice"
    )


@bot.command(name="lab")
async def lab_command(ctx):
    await ctx.send(
        "**Lab Safety Checklist**\n"
        "1. Sirf apni Kali VM / DVWA / TryHackMe par kaam karo\n"
        "2. Lab ka snapshot lo, galti ho to wapas aa sako\n"
        "3. Real website, account, Wi-Fi ya college network par kabhi test mat karo\n"
        "4. Har lab ke baad notes likho: kya seekha, kya fix hota hai\n"
        "5. Bina permission kisi system ko scan/test mat karo"
    )


@bot.command(name="resources")
async def resources_command(ctx):
    await ctx.send(
        "**Free Resources**\n"
        "• Cisco Ethical Hacker (free, ~70h) — Networking Academy\n"
        "• Fortinet NSE free modules\n"
        "• TryHackMe beginner rooms, PicoCTF\n"
        "• Book: Abhinav Ojha — Beginners Guide to Ethical Hacking (chapter + lab)\n"
        "• Class notes: apne study channels me posted material dekho"
    )


@bot.command(name="doubt")
async def doubt_command(ctx, *, question: str = ""):
    await ctx.send(doubt_answer(question))


@bot.command(name="cyber")
async def cyber_command(ctx, *, topic: str = ""):
    await ctx.send(cyber_answer(topic))


@bot.command(name="eh")
async def eh_command(ctx, *, topic: str = ""):
    await ctx.send(eh_answer(topic))


@bot.command(name="subject")
async def subject_command(ctx, *, subject: str = ""):
    await ctx.send(subject_answer(subject))


@bot.event
async def on_ready():
    # Only the bot's display name is logged. The token is never logged.
    print(f"Bot online as {bot.user} — ready for commands (!help).")


def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print(
            "ERROR: DISCORD_BOT_TOKEN environment variable set nahi hai.\n"
            "README.md me setup steps dekho, phir dobara chalao.",
            file=sys.stderr,
        )
        sys.exit(1)
    bot.run(token)


if __name__ == "__main__":
    main()
