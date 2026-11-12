"""Generates the animated SVGs used by the profile README.

Run:  py -3 tools/build_svgs.py
All animation is SMIL/CSS inside the SVG, so it works when GitHub shows it as an <img>.
"""
import random
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"

PURPLE, CYAN, PINK, GREEN, AMBER, BLUE, RED, ORANGE = (
    "#a78bfa", "#22d3ee", "#f472b6", "#4ade80", "#fbbf24", "#60a5fa", "#f87171", "#fb923c")


# ---------------------------------------------------------------- header
def header():
    rnd = random.Random(7)
    W, H = 1000, 270
    stars = []
    for _ in range(46):
        x, y = rnd.uniform(10, W - 10), rnd.uniform(10, H - 10)
        r = rnd.choice([0.8, 1.1, 1.5, 2])
        d = rnd.uniform(2, 5)
        b = rnd.uniform(0, 4)
        stars.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff">'
            f'<animate attributeName="opacity" values="0.15;1;0.15" dur="{d:.1f}s" begin="{b:.1f}s" repeatCount="indefinite"/></circle>')

    phrases = [
        "automating the boring stuff so humans don't have to",
        "building apps that secretly live inside Power Apps",
        "teaching AI agents to behave (mostly)",
        "writing Java for school, TypeScript for fun",
    ]
    cyc = 3.5 * len(phrases)
    taglines = []
    for i, p in enumerate(phrases):
        taglines.append(
            f'<text x="60" y="196" class="mono" font-size="19" fill="#e2e8f0" opacity="0">'
            f'<tspan fill="{GREEN}">&gt; </tspan>{escape(p)}'
            f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.03;0.22;0.25;1" '
            f'dur="{cyc}s" begin="{i * 3.5}s" repeatCount="indefinite"/></text>')

    robot = f'''
  <g transform="translate(800 70)">
    <g>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -9;0 0" dur="3s" repeatCount="indefinite"/>
      <!-- antenna -->
      <line x1="60" y1="8" x2="60" y2="-14" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round"/>
      <circle cx="60" cy="-18" r="7" fill="{PINK}">
        <animate attributeName="fill" values="{PINK};{AMBER};{CYAN};{PINK}" dur="2.4s" repeatCount="indefinite"/>
      </circle>
      <!-- head -->
      <rect x="10" y="8" width="100" height="76" rx="18" fill="#1e293b" stroke="{PURPLE}" stroke-width="4"/>
      <rect x="22" y="22" width="76" height="46" rx="10" fill="#0b1020"/>
      <rect x="36" y="32" width="14" height="16" rx="3" fill="{CYAN}">
        <animate attributeName="height" values="16;16;2;16;16" keyTimes="0;0.9;0.94;0.98;1" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="y" values="32;32;39;32;32" keyTimes="0;0.9;0.94;0.98;1" dur="4s" repeatCount="indefinite"/>
      </rect>
      <rect x="70" y="32" width="14" height="16" rx="3" fill="{CYAN}">
        <animate attributeName="height" values="16;16;2;16;16" keyTimes="0;0.9;0.94;0.98;1" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="y" values="32;32;39;32;32" keyTimes="0;0.9;0.94;0.98;1" dur="4s" repeatCount="indefinite"/>
      </rect>
      <path d="M46 56 Q60 64 74 56" stroke="{CYAN}" stroke-width="3" fill="none" stroke-linecap="round"/>
      <circle cx="26" cy="62" r="4" fill="{PINK}" opacity=".55"/>
      <circle cx="94" cy="62" r="4" fill="{PINK}" opacity=".55"/>
      <!-- body -->
      <rect x="24" y="90" width="72" height="56" rx="12" fill="#1e293b" stroke="{PURPLE}" stroke-width="4"/>
      <text x="60" y="126" text-anchor="middle" class="mono" font-size="20" font-weight="700" fill="{GREEN}">{{ }}</text>
      <!-- left arm -->
      <rect x="2" y="96" width="16" height="40" rx="8" fill="#334155"/>
      <!-- waving right arm -->
      <g>
        <animateTransform attributeName="transform" type="rotate" values="0 104 98;-38 104 98;0 104 98;-38 104 98;0 104 98;0 104 98" keyTimes="0;0.12;0.24;0.36;0.48;1" dur="4s" repeatCount="indefinite"/>
        <rect x="100" y="60" width="16" height="44" rx="8" fill="#334155"/>
        <circle cx="108" cy="58" r="10" fill="#475569"/>
      </g>
    </g>
    <ellipse cx="60" cy="178" rx="46" ry="7" fill="#000" opacity=".35">
      <animate attributeName="rx" values="46;38;46" dur="3s" repeatCount="indefinite"/>
    </ellipse>
  </g>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="vusallmammad — animated banner">
  <style>.mono{{font-family:{MONO}}} .sans{{font-family:{SANS}}}</style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f0c29"/><stop offset=".55" stop-color="#302b63"/><stop offset="1" stop-color="#1a1a3a"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{PURPLE}"/><stop offset="1" stop-color="{PINK}"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-0.4 0;0.4 0;-0.4 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath>
  </defs>
  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <circle cx="180" cy="60" r="120" fill="{PURPLE}" opacity=".35" filter="url(#blur)">
      <animate attributeName="cx" values="180;320;180" dur="14s" repeatCount="indefinite"/>
    </circle>
    <circle cx="760" cy="230" r="130" fill="{CYAN}" opacity=".22" filter="url(#blur)">
      <animate attributeName="cy" values="230;150;230" dur="11s" repeatCount="indefinite"/>
    </circle>
    <circle cx="520" cy="250" r="90" fill="{PINK}" opacity=".22" filter="url(#blur)">
      <animate attributeName="cx" values="520;420;520" dur="9s" repeatCount="indefinite"/>
    </circle>
    {''.join(stars)}
    <text x="60" y="82" class="mono" font-size="17" fill="#94a3b8">~/github $ ./say-hi --loud</text>
    <text x="58" y="150" class="sans" font-size="64" font-weight="800" fill="url(#name)" letter-spacing="-1">vusallmammad</text>
    {''.join(taglines)}
    <text x="60" y="238" class="mono" font-size="14" fill="#64748b">power platform · azure · react/ts · ai agents · java</text>
    {robot}
  </g>
</svg>'''
    (OUT / "header.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- terminal
def terminal():
    CW = 9.0          # forced char width (textLength) so typing lines up in any mono font
    FS = 15
    LH = 25
    X0 = 28
    TOP = 66
    TYPE = 0.055      # seconds per typed char
    user = "vusallmammad"
    prompt = [(user, GREEN), ("@", "#94a3b8"), ("github", PURPLE), (":", "#94a3b8"), ("~", BLUE), ("$", "#94a3b8")]
    plen_draw = sum(len(t) for t, _ in prompt)
    plen = plen_draw + 1  # one blank cell after "$" (SVG would collapse a trailing space)

    script = [
        ("whoami", [
            [("automation engineer", CYAN), (" · ", "#64748b"), ("student dev", PINK), (" · ", "#64748b"), ("professional button-presser", AMBER)],
        ]),
        ("cat currently.txt", [
            [("→ ", GREEN), ("shipping React apps that secretly live inside Power Apps", "#e2e8f0")],
            [("→ ", GREEN), ("plugging AI agents into ERPs older than some interns", "#e2e8f0")],
            [("→ ", GREEN), ("finishing my senior design project (the farm one 🐄)", "#e2e8f0")],
        ]),
        ("git log --all --oneline | wc -l", [
            [("too many to count. ", "#e2e8f0"), ("most of them live in private repos 🤫", "#94a3b8")],
        ]),
        ("sudo make coffee", [
            [("[sudo] password for vusallmammad: ", "#94a3b8"), ("********", "#94a3b8")],
            [("☕ brewing... ", AMBER), ("done.", GREEN), (" productivity +40%", "#e2e8f0")],
        ]),
    ]

    body = []
    cursor_anims = []
    t = 0.6
    y = TOP
    for cmd, outputs in script:
        # prompt appears
        spans = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in prompt)
        body.append(f'<text x="{X0}" y="{y}" textLength="{plen_draw * CW}" lengthAdjust="spacing" opacity="0">{spans}'
                    f'<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/></text>')
        cx0 = X0 + plen * CW
        cursor_anims.append(f'<set attributeName="y" to="{y - FS + 2}" begin="{t:.2f}s" fill="freeze"/>')
        cursor_anims.append(f'<set attributeName="x" to="{cx0}" begin="{t:.2f}s" fill="freeze"/>')
        t += 0.45
        # command typed
        n = len(cmd)
        cid = f"c{len(body)}"
        widths = ";".join(f"{k * CW:.1f}" for k in range(n + 1))
        xs = ";".join(f"{cx0 + k * CW:.1f}" for k in range(n + 1))
        dur = TYPE * (n + 1)
        body.append(
            f'<clipPath id="{cid}"><rect x="{cx0}" y="{y - FS - 4}" width="0" height="{LH}">'
            f'<animate attributeName="width" values="{widths}" calcMode="discrete" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"/>'
            f'</rect></clipPath>'
            f'<text x="{cx0}" y="{y}" fill="#f8fafc" textLength="{n * CW}" lengthAdjust="spacing" clip-path="url(#{cid})">{escape(cmd)}</text>')
        cursor_anims.append(f'<animate attributeName="x" values="{xs}" calcMode="discrete" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"/>')
        t += dur + 0.35
        y += LH
        # outputs
        for line in outputs:
            spans = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in line)
            body.append(f'<text x="{X0}" y="{y}" opacity="0">{spans}'
                        f'<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/></text>')
            t += 0.18
            y += LH
        t += 0.5
        y += 6
    # final prompt with resting cursor
    spans = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in prompt)
    body.append(f'<text x="{X0}" y="{y}" textLength="{plen_draw * CW}" lengthAdjust="spacing" opacity="0">{spans}'
                f'<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/></text>')
    cursor_anims.append(f'<set attributeName="y" to="{y - FS + 2}" begin="{t:.2f}s" fill="freeze"/>')
    cursor_anims.append(f'<set attributeName="x" to="{X0 + plen * CW}" begin="{t:.2f}s" fill="freeze"/>')

    W = 1000
    H = y + 30
    cursor = (f'<rect x="{X0 + plen * CW}" y="{TOP - FS + 2}" width="{CW}" height="{FS + 3}" fill="{GREEN}" opacity=".9">'
              + "".join(cursor_anims)
              + '<animate attributeName="opacity" values=".9;.9;0;0" keyTimes="0;.5;.5;1" dur="1s" repeatCount="indefinite"/></rect>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Terminal: whoami — automation engineer, student dev, professional button-presser">
  <style>text{{font-family:{MONO};font-size:{FS}px}}</style>
  <rect width="{W}" height="{H}" rx="16" fill="#0b1020"/>
  <rect width="{W}" height="{H}" rx="16" fill="none" stroke="#1f2a44" stroke-width="2"/>
  <path d="M0 16 a16 16 0 0 1 16 -16 h{W - 32} a16 16 0 0 1 16 16 v20 h-{W} z" fill="#151c33"/>
  <circle cx="26" cy="18" r="6.5" fill="#ff5f57"/><circle cx="48" cy="18" r="6.5" fill="#febc2e"/><circle cx="70" cy="18" r="6.5" fill="#28c840"/>
  <text x="{W / 2}" y="23" text-anchor="middle" fill="#64748b" style="font-size:13px">vusallmammad — zsh — 100×{len(body)}</text>
  {''.join(body)}
  {cursor}
</svg>'''
    (OUT / "terminal.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- character sheet
def stats():
    W, H = 1000, 380
    px = 12  # pixel size for the wizard sprite
    sprite = [
        "......YY......",
        ".....PPPP.....",
        "....PPPPPP....",
        "...PPPYPPPP...",
        "..PPPPPPPPPP..",
        ".BBBBBBBBBBBB.",
        "....SSSSSS....",
        "....SKSSKS....",
        "....SSSSSS....",
        "....WWWWWW....",
        "...RRWWWWRR...",
        "..RRRRRRRRRR.G",
        "..RRRRRRRRRR.G",
        "..RRRRAARRRR.G",
        "..RRRRRRRRRR.G",
        "...RR....RR..G",
    ]
    cols = {"Y": AMBER, "P": "#7c3aed", "B": "#4c1d95", "S": "#fcd9b6", "K": "#0f172a",
            "W": "#e5e7eb", "R": "#6d28d9", "A": AMBER, "G": "#a16207"}
    pix = []
    for r, row in enumerate(sprite):
        for c, ch in enumerate(row):
            if ch in cols:
                pix.append(f'<rect x="{c * px}" y="{r * px}" width="{px}" height="{px}" fill="{cols[ch]}"/>')
    # sparkle on the staff
    pix.append(f'<circle cx="{13 * px + 6}" cy="{10 * px}" r="7" fill="{CYAN}">'
               f'<animate attributeName="r" values="4;9;4" dur="1.6s" repeatCount="indefinite"/>'
               f'<animate attributeName="opacity" values="1;.4;1" dur="1.6s" repeatCount="indefinite"/></circle>')

    bars = [
        ("Power Platform", 92, PURPLE),
        ("AI agents / MCP", 88, PINK),
        ("Azure", 80, CYAN),
        ("React + TypeScript", 78, BLUE),
        ("PowerShell sorcery", 75, GREEN),
        ("Java (homework-powered)", 70, ORANGE),
        ("Sleep schedule", 12, RED),
    ]
    BX, BW, BY0, BGAP = 610, 320, 92, 36
    rows = []
    for i, (name, val, col) in enumerate(bars):
        y = BY0 + i * BGAP
        begin = 0.4 + i * 0.18
        w = BW * val / 100
        rows.append(
            f'<text x="{BX - 192}" y="{y + 12}" class="sans" font-size="14" fill="#cbd5e1">{escape(name)}</text>'
            f'<rect x="{BX}" y="{y}" width="{BW}" height="14" rx="7" fill="#1e293b"/>'
            f'<rect x="{BX}" y="{y}" width="0" height="14" rx="7" fill="{col}">'
            f'<animate attributeName="width" from="0" to="{w:.1f}" begin="{begin:.2f}s" dur="1.1s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1" keyTimes="0;1"/></rect>'
            f'<text x="{BX + BW + 12}" y="{y + 12}" class="mono" font-size="13" fill="{col}" opacity="0">{val}'
            f'<set attributeName="opacity" to="1" begin="{begin + 1.0:.2f}s" fill="freeze"/></text>')
    # blinking LOW warning on sleep
    ly = BY0 + (len(bars) - 1) * BGAP
    rows.append(f'<text x="{BX + 60}" y="{ly + 12}" class="mono" font-size="11" font-weight="700" fill="{RED}" opacity="0">⚠ LOW'
                f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.6;1" dur="1.2s" begin="2.6s" repeatCount="indefinite"/></text>')

    info = [("CLASS", "Automation Wizard", PURPLE), ("LEVEL", "99 (self-reported)", AMBER),
            ("ALIGNMENT", "Chaotic Productive", PINK), ("FUEL", "coffee, deadlines", CYAN)]
    info_svg = []
    for i, (k, v, c) in enumerate(info):
        y = 92 + i * 52
        info_svg.append(f'<text x="222" y="{y}" class="mono" font-size="11" fill="#64748b" letter-spacing="2">{k}</text>'
                        f'<text x="222" y="{y + 22}" class="sans" font-size="17" font-weight="700" fill="{c}">{escape(v)}</text>')

    perks = "✦ speaks fluent Dataverse   ✦ tames legacy ERPs   ✦ turns spreadsheets into apps   ✦ +10 vs. Monday bugs"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Character sheet: Automation Wizard, skill bars">
  <style>.mono{{font-family:{MONO}}} .sans{{font-family:{SANS}}}</style>
  <defs>
    <linearGradient id="sbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#111827"/><stop offset="1" stop-color="#1e1b4b"/></linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#ffffff" stroke-opacity=".035"/></pattern>
  </defs>
  <rect width="{W}" height="{H}" rx="18" fill="url(#sbg)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="17" fill="none" stroke="{PURPLE}" stroke-opacity=".45" stroke-width="2" stroke-dasharray="10 6">
    <animate attributeName="stroke-dashoffset" values="0;-32" dur="2s" repeatCount="indefinite"/>
  </rect>
  <text x="34" y="46" class="mono" font-size="15" font-weight="700" fill="#e2e8f0" letter-spacing="4">⚔ CHARACTER SHEET</text>
  <text x="{W - 34}" y="46" text-anchor="end" class="mono" font-size="12" fill="#64748b">player: vusallmammad · save slot 1</text>
  <g transform="translate(26 76)">
    <animateTransform attributeName="transform" type="translate" values="26 76;26 70;26 76" dur="2.2s" repeatCount="indefinite"/>
    {''.join(pix)}
  </g>
  {''.join(info_svg)}
  <text x="{BX - 192}" y="72" class="mono" font-size="11" fill="#64748b" letter-spacing="2">SKILLS</text>
  {''.join(rows)}
  <line x1="34" y1="{H - 56}" x2="{W - 34}" y2="{H - 56}" stroke="#334155"/>
  <text x="34" y="{H - 26}" class="mono" font-size="13" fill="#94a3b8"><tspan fill="{AMBER}">PERKS </tspan>{escape(perks)}</text>
</svg>'''
    (OUT / "stats.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- footer
def footer():
    W, H = 1000, 150

    def wave(amp, length, y, phase):
        pts = [f"M{-length * 2} {y}"]
        x = -length * 2
        while x < W + length * 2:
            pts.append(f"q{length / 4} {-amp} {length / 2} 0 t{length / 2} 0")
            x += length
        pts.append(f"V{H} H{-length * 2} Z")
        return "".join(pts)

    layers = [(PURPLE, .35, 14, 240, 70, 7), (CYAN, .3, 10, 200, 84, 5), (PINK, .45, 8, 160, 100, 4)]
    g = []
    for col, op, amp, ln, y, dur in layers:
        g.append(f'<path d="{wave(amp, ln, y, 0)}" fill="{col}" opacity="{op}">'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;{ln} 0" dur="{dur}s" repeatCount="indefinite"/></path>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Thanks for scrolling — here is a cookie">
  <defs><clipPath id="fc"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>
  <g clip-path="url(#fc)">
    <rect width="{W}" height="{H}" fill="#0f0c29"/>
    {''.join(g)}
    <text x="{W / 2}" y="52" text-anchor="middle" font-family="{SANS}" font-size="20" font-weight="700" fill="#f8fafc">thanks for scrolling this far — here's a cookie 🍪</text>
  </g>
</svg>'''
    (OUT / "footer.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    header(); terminal(); stats(); footer()
    for f in sorted(OUT.glob("*.svg")):
        print(f.name, f.stat().st_size, "bytes")
