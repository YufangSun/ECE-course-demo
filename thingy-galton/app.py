"""Galton Board - an interactive thingy for The Thingy Repository."""

import html
import pathlib

import gradio as gr

AUTHOR = "Yufang Sun"

TITLE = "Galton Board"
BLURB = (
    "Every peg is one coin flip. The bin a ball lands in counts its right turns, "
    "so the pile that builds up is a binomial distribution - and for many rows, a bell curve. "
    "Watch the exact pmf appear underneath the measured histogram, and set the fall speed to "
    "**slow** to follow a single ball and read off its left/right sequence."
)

# The demo is a self-contained HTML/canvas animation with no dependencies. It is
# served inside an iframe via srcdoc so its <script> is guaranteed to execute and
# its styling cannot leak into (or be overridden by) the surrounding Gradio theme.
_DEMO = (pathlib.Path(__file__).parent / "galton.html").read_text(encoding="utf-8")
_IFRAME = (
    '<iframe srcdoc="{doc}" '
    'style="width:100%;height:1180px;border:1px solid #30363d;border-radius:12px;'
    'background:#0d1117" '
    'sandbox="allow-scripts"></iframe>'
).format(doc=html.escape(_DEMO, quote=True))

with gr.Blocks(title=TITLE, theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {TITLE}\nBy **{AUTHOR}**\n\n{BLURB}")
    gr.HTML(_IFRAME)

if __name__ == "__main__":
    demo.launch()
