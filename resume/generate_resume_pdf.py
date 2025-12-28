#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parent
SOURCE_MD = ROOT / "resume.md"
OUTPUT_PDF = ROOT / "resume.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Heading1Center", parent=styles["Heading1"], alignment=1, spaceAfter=12))
styles.add(ParagraphStyle(name="Heading2Tight", parent=styles["Heading2"], spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], leading=14))


def markdown_to_story(lines: list[str]):
    story = []
    bullet_buffer: list[str] = []

    def flush_bullets():
        if not bullet_buffer:
            return
        items = [ListItem(Paragraph(item, styles["Body"]), leftIndent=12) for item in bullet_buffer]
        story.append(ListFlowable(items, bulletType="bullet", start="-"))
        story.append(Spacer(1, 6))
        bullet_buffer.clear()

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line:
            flush_bullets()
            story.append(Spacer(1, 6))
            continue

        if line.startswith("- "):
            text = line[2:].strip()
            text = convert_inline_markdown(text)
            bullet_buffer.append(text)
            continue

        flush_bullets()

        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["Heading1Center"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["Heading2Tight"]))
        else:
            story.append(Paragraph(convert_inline_markdown(line), styles["Body"]))
        story.append(Spacer(1, 6))

    flush_bullets()
    return story


def convert_inline_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    return text


def build_pdf():
    lines = SOURCE_MD.read_text(encoding="utf-8").splitlines()
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=LETTER,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
    )
    story = markdown_to_story(lines)
    doc.build(story)
    print(f"Created {OUTPUT_PDF.relative_to(Path.cwd())}")


if __name__ == "__main__":
    build_pdf()
