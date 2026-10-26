"""Small, honest, rule-based knowledge base for the college study bot.

No AI model, no paid API, no internet call.
Every answer here is a short, written note. If a question does not match
anything in this file, the bot must say "I don't know" instead of guessing.

Cybersecurity / ethical hacking answers are LAB-ONLY by design:
authorised labs only (own system, Kali VM, DVWA, TryHackMe, Metasploitable
lab machines you own / are allowed to use). Never hacking real systems,
real accounts, other people's Wi-Fi, or college networks. Illegal requests
get a short refusal plus a defensive / lab-only alternative — never
instructions for the illegal act.
"""

SUBJECTS = {
    "dbms": (
        "**DBMS (Database Management System)**\n"
        "DBMS data ko organised tarike se store, manage aur retrieve karta hai.\n"
        "- Key: Primary Key har row ko unique pehchanti hai; Foreign Key do tables ko jodti hai.\n"
        "- Normalization: data ki repetition kam karta hai (1NF, 2NF, 3NF).\n"
        "- Basic SQL: `SELECT`, `INSERT`, `UPDATE`, `DELETE` — pehle apne local test "
        "database par practice karo, real data par nahi."
    ),
    "cg": (
        "**Computer Graphics (CG)**\n"
        "Computer Graphics images ko computer se banane aur dikhane ki study hai.\n"
        "- Raster image pixels se banti hai; Vector image maths/shapes se banti hai.\n"
        "- Transformation: Translation (move), Scaling (size badalna), Rotation (ghumana).\n"
        "- Pipeline ka simple idea: Model -> Transform -> Render -> Screen par image."
    ),
    "se": (
        "**Software Engineering (SE)**\n"
        "Software ko plan karke, systematic tarike se banane ki study hai.\n"
        "- SDLC stages: Requirement -> Design -> Coding -> Testing -> Maintenance.\n"
        "- Agile: chhote-chhote parts me kaam karo, baar-baar feedback lo.\n"
        "- Testing ka matlab: software ko use karne se pehle galtiyan dhoondhna aur fix karna."
    ),
    "maths": (
        "**Maths — Probability & Statistics (basic)**\n"
        "- Probability: kisi event ke hone ki chance, 0 se 1 ke beech hoti hai.\n"
        "- Mean = sab values ka average; Median = beech wali value (sorted order me).\n"
        "- Example: coin toss me Head ki probability = 1/2 = 0.5.\n"
        "Detail numerical ke liye apni class notes / teacher se confirm karo."
    ),
    "python": (
        "**Python (basic)**\n"
        "- Variable: value ko naam dena, jaise `x = 10`.\n"
        "- Loop: kaam baar-baar karna — `for` aur `while`.\n"
        "- Function: ek kaam ka reusable block, jaise `def add(a, b): return a + b`.\n"
        "- List: multiple values ek jagah, jaise `[1, 2, 3]`.\n"
        "Practice: chhota code likho, chalao, error padho, phir fix karo."
    ),
}

CYBER_TOPICS = {
    "basics": (
        "**Cybersecurity Basics — CIA Triad**\n"
        "- Confidentiality: data sirf sahi log dekh sakein.\n"
        "- Integrity: data bina permission ke badla na jaye.\n"
        "- Availability: sahi logon ko data/service mile jab zaroorat ho."
    ),
    "phishing": (
        "**Phishing — pehchanna aur bachna (defensive only)**\n"
        "Phishing me nakli link/message se password ya OTP churane ki koshish hoti hai.\n"
        "- Sender, spelling aur link ko dhyan se check karo, jaldi me click mat karo.\n"
        "- OTP/password kabhi kisi ko mat do, kisi bhi link par mat bharo.\n"
        "- Phishing link banana / kisi ko dhoka dena bilkul mana hai — bot sirf "
        "defensive seekhna sikhata hai: pehchanna, report karna, bachna."
    ),
    "password": (
        "**Strong Password**\n"
        "- Lamba password rakho (12+ characters), alag-alag sites par alag password.\n"
        "- Password manager use karna behtar hai, password diary/chat me mat likho.\n"
        "- 2FA (two-factor) on rakho jahan mile — ye extra safety deta hai."
    ),
    "kali": (
        "**Kali Linux (beginner, lab-only)**\n"
        "Kali ek Linux system hai jisme security testing tools hote hain.\n"
        "- Pehle seekho: Linux commands, networking basics, phir tools (jaise Nmap).\n"
        "- Sirf apne laptop / localhost / authorised lab par scan ya test karo.\n"
        "- Real websites, dusron ka Wi-Fi ya college network par kabhi test mat karo."
    ),
    "nmap": (
        "**Nmap (lab-only)**\n"
        "Nmap network par devices/services ke baare me jaankari deta hai.\n"
        "- Basic scan ka idea: `nmap <target>` — target sirf apna system/lab ho.\n"
        "- Bina permission ke kisi aur ke system/network ko scan karna galat aur illegal ho sakta hai."
    ),
    "web": (
        "**Web Security (basic, lab-only)**\n"
        "- Common kamzoriyan: SQL Injection, XSS, weak login — ye sirf lab (DVWA) me seekho.\n"
        "- Fix seekhna utna hi zaroori hai jitna attack samajhna: input check karo, "
        "safe queries use karo, strong login rakho.\n"
        "- Real website par ye try karna mana hai, chahe wo chhoti site hi kyun na ho."
    ),
}

# --- Professional ethical hacking learning path (lab-only) ---------------
EH_TOPICS = {
    "eh-path": (
        "**Professional Ethical Hacking — Learning Path**\n"
        "Professional matlab: permission + ethics + report, sirf tools nahi.\n"
        "1. Basics: cybersecurity kya hai, CIA triad, hacker types (white-hat vs black-hat).\n"
        "2. Networking + Linux: IP, port, TCP/UDP, DNS + basic Linux commands.\n"
        "3. Kali lab setup: VirtualBox me apni Kali VM, snapshot lo, lab network alag rakho.\n"
        "4. Footprinting + Scanning — sirf apne lab par.\n"
        "5. Web security — sirf DVWA jaise lab par, saath me fix seekho.\n"
        "6. Tools + CTF: TryHackMe / PicoCTF beginner rooms, apni pace par.\n"
        "7. Free certifications + notes + apna lab portfolio (koi real target nahi).\n"
        "Har step ka rule ek hi hai: pehle permission, phir lab, phir report."
    ),
    "networking": (
        "**Networking Basics (ethical hacking ke liye)**\n"
        "- IP address: device ki pehchan network par; Port: service ka darwaza (jaise 80 = web).\n"
        "- TCP: reliable connection; UDP: fast, bina guarantee ke.\n"
        "- DNS: naam (jaise example.com) ko IP me badalta hai.\n"
        "- Practice: apne lab network par ye concepts dekho — dusre ke network par nahi."
    ),
    "linux": (
        "**Linux Basics (Kali ke liye)**\n"
        "- `pwd` (kahan ho), `ls` (files dekho), `cd` (folder badlo), `cat` (file padho).\n"
        "- `chmod` permission badalta hai — apni hi files par practice karo.\n"
        "- `man <command>` se kisi command ki help padho, bina guess kiye.\n"
        "- Pehle Linux pakka karo, phir security tools asaan lagenge."
    ),
    "kali-lab": (
        "**Kali Lab Setup (professional tareeka)**\n"
        "1. VirtualBox me Kali VM banao — apne laptop par, kisi aur ke system par nahi.\n"
        "2. VM ka snapshot lo, taaki galti ho to wapas aa sako.\n"
        "3. Lab machines (jaise DVWA / Metasploitable) sirf apni VM network me rakho.\n"
        "4. Lab ke bahar — real website, Wi-Fi, college network — par koi scan/test nahi.\n"
        "Lab ready ho, tabhi agle step par jao."
    ),
    "footprinting": (
        "**Footprinting — Lab me info gathering**\n"
        "Footprinting ka matlab: target ke baare me public / allowed jaankari jama karna.\n"
        "- Lab me: apni lab machine ke baare me notes banao — IP, services, version.\n"
        "- Passive tareeka pehle seekho: docs padhna, apne lab ki config samajhna.\n"
        "- Real person / real company ki bina permission jaankari jama karna mana hai."
    ),
    "scanning": (
        "**Scanning — Sirf apne lab par**\n"
        "Scanning me pata chalta hai lab machine par kaunsi services chal rahi hain.\n"
        "- Nmap jaisa tool sirf apni lab machine par chalao, apne lab IP par.\n"
        "- Result ko note karo: kaunsa port khula hai, kaunsi service hai — phir uska fix socho.\n"
        "- Bina permission kisi aur ke system/network ko scan karna illegal ho sakta hai."
    ),
    "web-lab": (
        "**Web Security Lab (DVWA — lab-only)**\n"
        "- Concepts: SQL Injection, XSS, weak login — ye DVWA lab me samjho.\n"
        "- Har kamzori ke saath uska FIX bhi seekho: safe queries, input check, output encoding.\n"
        "- OWASP Top 10 ko list ki tarah padho, ek-ek concept lab me dekhkar.\n"
        "- Real website par ye kabhi try mat karo, chahe site chhoti hi kyun na ho."
    ),
    "tools": (
        "**Tools — Lab me hi, ek-ek karke**\n"
        "- Nmap: apne lab ki services dekhna.\n"
        "- Wireshark: apne hi network traffic ko samajhna.\n"
        "- Burp Suite (Community): apne lab web app ko test karna.\n"
        "- Metasploit: sirf apni lab machine (Metasploitable) par, permission ke saath.\n"
        "Tool seekhne ka sahi tareeka: ek tool, ek lab, ek note — jaldi me sab mat chhedo."
    ),
    "ctf": (
        "**CTF Practice (free, beginner-friendly)**\n"
        "- TryHackMe: beginner rooms, step-by-step, lab environment ke saath.\n"
        "- PicoCTF: beginners ke liye challenges, apni pace par.\n"
        "- HackTheBox Academy: jab basics pakke ho jayein, tab modules try karo.\n"
        "- Har challenge ke baad ye likho: kya seekha, kya fix hota hai — sirf flag nahi."
    ),
    "certifications": (
        "**Free Certifications — Ethical Hacking raasta**\n"
        "- Cisco Ethical Hacker: free, self-paced, ~70 hours, hands-on labs (Cisco Networking Academy).\n"
        "- Fortinet NSE (1/2/3): free chhote modules, security fundamentals + certificate.\n"
        "- Google Cybersecurity (Coursera): video lectures free (audit), certificate financial aid par depend karta hai.\n"
        "- Note: EC-Council CEH alag hai aur paid/mehenga hai — use Cisco se confuse mat karo.\n"
        "- Certificate akela job guarantee nahi karta — degree + practical lab + notes bhi chahiye."
    ),
    "book": (
        "**Book Base — Abhinav Ojha, Beginners Guide to Ethical Hacking**\n"
        "Book se base banao, har chapter ke saath apne lab me 1 practical karo:\n"
        "- Footprinting chapter -> apne lab ki notes + recon practice (lab par).\n"
        "- Scanning chapter -> apne lab par Nmap practice (lab IP par).\n"
        "- Networking chapter -> IP/port/DNS apne lab me dekhkar samjho.\n"
        "- Web chapter -> DVWA lab me concept + fix, real site par kabhi nahi.\n"
        "- Book me theory zyada lage to bhi chapter skip mat karo — theory + lab, dono saath chalenge."
    ),
}

# Keywords -> topic, so "!doubt phishing kya hai" bhi kaam kare.
DOUBT_KEYWORDS = {
    "dbms": "dbms", "database": "dbms", "sql": "dbms", "normalization": "dbms",
    "graphics": "cg", "cg": "cg", "raster": "cg",
    "software": "se", "sdlc": "se", "agile": "se", "testing": "se",
    "probability": "maths", "maths": "maths", "math": "maths", "statistics": "maths",
    "python": "python", "loop": "python", "function": "python", "list": "python",
    "phishing": "phishing", "otp": "phishing", "fraud": "phishing",
    "password": "password", "2fa": "password",
    "kali": "kali", "linux": "kali",
    "nmap": "nmap", "scan": "nmap",
    "web": "web", "xss": "web", "sqli": "web", "sql injection": "web",
    "cia": "basics", "cyber": "basics", "cybersecurity": "basics", "security": "basics",
}

EH_DOUBT_KEYWORDS = {
    "ethical hacking": "eh-path", "eh path": "eh-path", "roadmap": "eh-path",
    "learning path": "eh-path", "professional": "eh-path",
    "networking": "networking", "network": "networking",
    "ip address": "networking", "port": "networking",
    "linux": "linux", "linux command": "linux",
    "kali lab": "kali-lab", "kali setup": "kali-lab", "virtualbox": "kali-lab",
    "lab setup": "kali-lab",
    "footprinting": "footprinting", "recon": "footprinting",
    "scanning": "scanning",
    "dvwa": "web-lab", "owasp": "web-lab", "web security": "web-lab",
    "burp": "tools", "wireshark": "tools", "metasploit": "tools",
    "ctf": "ctf", "tryhackme": "ctf", "picoctf": "ctf",
    "certification": "certifications", "certificate": "certifications",
    "cisco": "certifications", "fortinet": "certifications",
    "google cybersecurity": "certifications",
    "ojha": "book", "abhinav": "book", "beginners guide": "book",
}

# Specific illegal-request patterns. These are deliberately narrow:
# general learning questions ("ethical hacking kya hai") must NOT match.
ILLEGAL_PATTERNS = [
    "hack instagram", "hack facebook", "hack whatsapp", "hack gmail",
    "hack account", "hack phone", "hack kisi", "kisi ka account hack",
    "wifi password", "wifi hack", "wi-fi hack", "college network hack",
    "college wifi", "real website hack", "hack website", "hack server",
    "phishing link banao", "phishing page banao", "fake login page",
    "password crack", "otp bypass", "bypass login",
    "bina permission ke hack", "bina permission hack",
]

REFUSAL_ILLEGAL = (
    "Main isme madad nahi kar sakta — ye real system / account / network ko "
    "bina permission target karta hai, jo galat aur illegal ho sakta hai. 🙏\n"
    "Defensive / lab-only alternative: apne lab me ye concept seekho — "
    "apni Kali VM / DVWA / TryHackMe par, permission ke saath — aur agar "
    "kisi real system me kamzori dikhe to use responsible tareeke se report karo, "
    "khud exploit mat karo.\n"
    "Safe shuruaat: `!eh eh-path` ya `!eh kali-lab`"
)

FALLBACK = (
    "Sorry, is sawal ka jawab mere paas nahi hai — I don't know, aur main guess nahi karunga. 🙏\n"
    "Apna doubt #doubts-help channel me likho, ya teacher / senior se poochho.\n"
    "Tip: sawal ke saath topic bhi likho, jaise `!cyber phishing`, `!eh kali-lab` ya `!subject dbms`."
)

LAB_ONLY_NOTE = (
    "\n\n⚠️ Lab-only: sirf apne system / authorised lab (apni Kali VM, DVWA, TryHackMe) "
    "par practice karo. Real system, account, Wi-Fi ya college network par kabhi try mat karo."
)


def is_illegal_request(question: str) -> bool:
    """True for narrow, specific illegal-target requests (see ILLEGAL_PATTERNS).

    Also catches hack + a real target in any word order, e.g.
    "kisi ka instagram account hack kaise kare?" — where the words are
    not in "hack instagram" order. General learning questions such as
    "ethical hacking kya hai?" contain "hack" but no real target, so
    they do NOT match.
    """
    q = question.strip().lower()
    if any(pattern in q for pattern in ILLEGAL_PATTERNS):
        return True
    if "hack" in q:
        targets = (
            "instagram", "facebook", "whatsapp", "gmail", "account",
            "phone", "kisi ka", "kisi ke", "dusre ka", "dusron ka",
        )
        if any(target in q for target in targets):
            return True
    return False


def subject_answer(subject: str) -> str:
    """Return the note for a subject, or the honest fallback."""
    key = subject.strip().lower()
    if key in SUBJECTS:
        return SUBJECTS[key]
    return (
        FALLBACK
        + "\nAvailable subjects: dbms, cg, se, maths, python.\n"
        + "Example: `!subject dbms`"
    )


def cyber_answer(topic: str) -> str:
    """Return the note for a cyber/EH topic, or the honest fallback."""
    key = topic.strip().lower()
    if key in CYBER_TOPICS:
        return CYBER_TOPICS[key] + LAB_ONLY_NOTE
    if key in EH_TOPICS:
        return EH_TOPICS[key] + LAB_ONLY_NOTE
    return (
        FALLBACK
        + "\nAvailable cyber topics: basics, phishing, password, kali, nmap, web.\n"
        + "Available ethical hacking topics: eh-path, networking, linux, kali-lab, "
        "footprinting, scanning, web-lab, tools, ctf, certifications, book.\n"
        + "Example: `!cyber phishing` ya `!eh kali-lab`"
    )


def eh_answer(topic: str) -> str:
    """Return the note for a professional ethical hacking topic, else fallback."""
    key = topic.strip().lower()
    if key in EH_TOPICS:
        return EH_TOPICS[key] + LAB_ONLY_NOTE
    if key in CYBER_TOPICS:
        return CYBER_TOPICS[key] + LAB_ONLY_NOTE
    return (
        FALLBACK
        + "\nAvailable ethical hacking topics: eh-path, networking, linux, kali-lab, "
        "footprinting, scanning, web-lab, tools, ctf, certifications, book.\n"
        + "Example: `!eh eh-path`"
    )


def doubt_answer(question: str) -> str:
    """Keyword-match a free question to the knowledge base, else fallback.

    Illegal-target requests are refused first, with a defensive alternative.
    """
    q = question.strip().lower()
    if not q:
        return FALLBACK + "\nExample: `!doubt dbms me primary key kya hai?`"
    if is_illegal_request(q):
        return REFUSAL_ILLEGAL
    # Ethical hacking topics first (more specific than the generic map).
    for keyword, topic in EH_DOUBT_KEYWORDS.items():
        if keyword in q:
            return EH_TOPICS[topic] + LAB_ONLY_NOTE
    for keyword, topic in DOUBT_KEYWORDS.items():
        if keyword in q:
            if topic in SUBJECTS:
                return SUBJECTS[topic]
            if topic in CYBER_TOPICS:
                return CYBER_TOPICS[topic] + LAB_ONLY_NOTE
    return FALLBACK
