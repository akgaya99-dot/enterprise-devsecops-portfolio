from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"
DATA_FILE = BASE_DIR / "data" / "profile.json"
TEMPLATE_NAME = "portfolio.html"

CONTROL_CHARS_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")
SHORT_TEXT_LIMIT = 200
LONG_TEXT_LIMIT = 2500


def strip_control_chars(value: str) -> str:
    return CONTROL_CHARS_RE.sub("", value).strip()


def clean_text(value: Any, *, max_length: int = LONG_TEXT_LIMIT) -> str:
    text = strip_control_chars(str(value))
    return text[:max_length]


def clean_url(value: Any) -> str:
    url = clean_text(value, max_length=500)
    parsed = urlparse(url)

    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return url
    if parsed.scheme == "mailto" and "@" in parsed.path:
        return url

    raise ValueError(f"Unsupported or unsafe URL: {url!r}")


def require_dict(data: Any, key: str) -> dict[str, Any]:
    value = data.get(key)
    if not isinstance(value, dict):
        raise TypeError(f"{key!r} must be a JSON object.")
    return value


def require_list(data: Any, key: str) -> list[Any]:
    value = data.get(key)
    if not isinstance(value, list):
        raise TypeError(f"{key!r} must be a JSON array.")
    return value


def clean_list(items: list[Any], *, max_length: int = SHORT_TEXT_LIMIT) -> list[str]:
    result: list[str] = []
    for item in items:
        text = clean_text(item, max_length=max_length)
        if text:
            result.append(text)
    return result


def load_profile() -> dict[str, Any]:
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    site = require_dict(raw, "site")
    profile = require_dict(raw, "profile")
    links = require_dict(raw, "links")
    metrics = require_list(raw, "metrics")
    capabilities = require_list(raw, "capabilities")
    projects = require_list(raw, "projects")
    skills = require_dict(raw, "skills")

    cleaned: dict[str, Any] = {
        "schema_version": clean_text(raw.get("schema_version", "2.0"), max_length=20),
        "site": {
            "title": clean_text(site.get("title", "Aakash Kumar | Portfolio"), max_length=120),
            "description": clean_text(site.get("description", ""), max_length=300),
            "hero_badge": clean_text(site.get("hero_badge", "Public Portfolio"), max_length=60),
            "eyebrow": clean_text(site.get("eyebrow", "Enterprise Automation Command Center"), max_length=90),
            "focus": clean_list(site.get("focus", []), max_length=70),
            "overview_intro": clean_text(site.get("overview_intro", ""), max_length=500),
            "identity_points": clean_list(site.get("identity_points", []), max_length=180),
            "current_focus_title": clean_text(site.get("current_focus_title", ""), max_length=90),
            "current_focus_body": clean_text(site.get("current_focus_body", ""), max_length=500),
            "workflow_tools": clean_list(site.get("workflow_tools", []), max_length=40),
            "section_narrative": clean_text(site.get("section_narrative", ""), max_length=650),
            "footer_motto": clean_text(site.get("footer_motto", ""), max_length=120),
            "footer_note": clean_text(site.get("footer_note", ""), max_length=200),
        },
        "profile": {
            "name": clean_text(profile.get("name", "Aakash Kumar"), max_length=80),
            "initials": clean_text(profile.get("initials", "AK"), max_length=4),
            "role": clean_text(profile.get("role", "Lead Platform & DevSecOps Engineer"), max_length=120),
            "summary": clean_text(profile.get("summary", ""), max_length=900),
            "location": clean_text(profile.get("location", ""), max_length=80),
            "availability": clean_text(profile.get("availability", ""), max_length=140),
            "email": clean_text(profile.get("email", ""), max_length=120),
        },
        "links": {
            "linkedin": clean_url(links.get("linkedin", "https://www.linkedin.com/")),
            "github": clean_url(links.get("github", "https://github.com/")),
            "email": clean_url(links.get("email", "mailto:example@example.com")),
        },
        "metrics": [],
        "capabilities": [],
        "projects": [],
        "skills": {},
    }

    for item in metrics:
        if not isinstance(item, dict):
            raise TypeError("Each metric must be an object.")
        cleaned["metrics"].append(
            {
                "icon": clean_text(item.get("icon", "•"), max_length=8),
                "value": clean_text(item.get("value", ""), max_length=40),
                "label": clean_text(item.get("label", ""), max_length=60),
                "subtext": clean_text(item.get("subtext", ""), max_length=140),
            }
        )

    for item in capabilities:
        if not isinstance(item, dict):
            raise TypeError("Each capability must be an object.")
        cleaned["capabilities"].append(
            {
                "icon": clean_text(item.get("icon", "•"), max_length=8),
                "title": clean_text(item.get("title", ""), max_length=80),
                "description": clean_text(item.get("description", ""), max_length=340),
                "highlights": clean_list(item.get("highlights", []), max_length=120),
            }
        )

    for item in projects:
        if not isinstance(item, dict):
            raise TypeError("Each project must be an object.")
        cleaned["projects"].append(
            {
                "icon": clean_text(item.get("icon", "•"), max_length=8),
                "title": clean_text(item.get("title", ""), max_length=80),
                "description": clean_text(item.get("description", ""), max_length=260),
                "impact": clean_text(item.get("impact", ""), max_length=260),
                "stack": clean_list(item.get("stack", []), max_length=40),
            }
        )

    for category, items in skills.items():
        if not isinstance(items, list):
            raise TypeError(f"skills[{category!r}] must be a list.")
        cleaned["skills"][clean_text(category, max_length=40)] = clean_list(items, max_length=50)

    if not cleaned["profile"]["summary"]:
        raise ValueError("profile.summary cannot be empty.")
    if not cleaned["metrics"]:
        raise ValueError("metrics cannot be empty.")
    if not cleaned["projects"]:
        raise ValueError("projects cannot be empty.")
    if not cleaned["skills"]:
        raise ValueError("skills cannot be empty.")

    return cleaned


def build_environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(
            enabled_extensions=("html", "htm", "xml"),
            default_for_string=True,
        ),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_template(context: dict[str, Any]) -> str:
    env = build_environment()
    template = env.get_template(TEMPLATE_NAME)
    return template.render(**context)


def estimate_component_height(context: dict[str, Any]) -> int:
    metric_rows = max(1, math.ceil(len(context["metrics"]) / 4))
    capability_rows = max(1, math.ceil(len(context["capabilities"]) / 2))
    project_rows = max(1, math.ceil(len(context["projects"]) / 2))
    skill_rows = max(1, len(context["skills"]))

    base_height = 1180
    estimated = (
        base_height
        + (metric_rows * 145)
        + (capability_rows * 260)
        + (project_rows * 250)
        + (skill_rows * 118)
    )
    return max(estimated, 2200)


def render_html(rendered_html: str, context: dict[str, Any]) -> None:
    # Streamlit 1.56+ recommends st.html over st.components.v1.html.
    if hasattr(st, "html"):
        st.html(rendered_html, unsafe_allow_javascript=True)
    else:
        components.html(
            rendered_html,
            height=estimate_component_height(context),
            scrolling=True,
            tab_index=0,
        )


def apply_streamlit_chrome_overrides() -> None:
    st.markdown(
        """
        <style>
            .stApp {
                background: #020617;
            }
            .block-container {
                padding: 0 !important;
                max-width: none !important;
            }
            header[data-testid="stHeader"],
            [data-testid="stDecoration"],
            [data-testid="stToolbar"] {
                visibility: hidden;
                height: 0;
                position: fixed;
            }
            #MainMenu, footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    context = load_profile()

    st.set_page_config(
        page_title=context["site"]["title"],
        page_icon="🌐",
        layout="wide",
    )

    apply_streamlit_chrome_overrides()

    rendered_html = render_template(context)
    render_html(rendered_html, context)


if __name__ == "__main__":
    main()
