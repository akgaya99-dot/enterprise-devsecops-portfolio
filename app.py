from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "profile.json"
TEMPLATE_DIR = BASE_DIR / "templates"
TEMPLATE_NAME = "portfolio.html"

REQUIRED_TOP_LEVEL_KEYS = {
    "theme",
    "profile",
    "links",
    "metrics",
    "capabilities",
    "product",
    "workflow_steps",
    "integrations",
    "projects",
    "principles",
    "roadmap",
    "skills",
}

# NOTE:
# Streamlit documents that st.components.v1.html is deprecated as of 1.56.0.
# It is still used here because you explicitly asked for safe components.html usage
# and because an iframe is useful for isolating custom CSS/JS/Three.js.
# Long-term, the cleaner path is a dedicated Streamlit custom component.

st.set_page_config(
    page_title="Aakash Kumar | Enterprise Vulnerability Remediation",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def apply_streamlit_shell() -> None:
    """Tighten Streamlit chrome so the portfolio can be more full-bleed."""
    st.markdown(
        """
        <style>
          [data-testid="stAppViewContainer"]{
            background:#020617;
          }
          .block-container{
            max-width:100%;
            padding-top:.35rem;
            padding-bottom:.35rem;
            padding-left:.35rem;
            padding-right:.35rem;
          }
          header[data-testid="stHeader"]{
            background:transparent;
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Profile JSON not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    validate_payload(payload)
    return normalize_links(payload)


def validate_payload(payload: dict) -> None:
    missing = REQUIRED_TOP_LEVEL_KEYS.difference(payload.keys())
    if missing:
        raise ValueError(f"Missing required top-level keys: {sorted(missing)}")

    if not isinstance(payload["profile"], dict):
        raise TypeError("'profile' must be an object")

    required_profile_fields = {"name", "headline", "subheadline", "summary", "email"}
    missing_profile_fields = required_profile_fields.difference(payload["profile"].keys())
    if missing_profile_fields:
        raise ValueError(
            f"Missing required profile fields: {sorted(missing_profile_fields)}"
        )

    for key in ("metrics", "capabilities", "workflow_steps", "integrations", "projects", "roadmap", "skills", "principles"):
        if not isinstance(payload[key], list):
            raise TypeError(f"'{key}' must be a list")

    if not isinstance(payload["product"], dict):
        raise TypeError("'product' must be an object")


def safe_url(value: str | None, *, allow_mailto: bool = False) -> str:
    if not value:
        return "#"

    value = value.strip()
    if value == "#":
        return "#"

    parsed = urlparse(value)
    allowed_schemes = {"https"}
    if allow_mailto:
      allowed_schemes.add("mailto")

    if parsed.scheme in allowed_schemes:
        return value

    return "#"


def normalize_links(payload: dict) -> dict:
    payload = dict(payload)
    links = dict(payload.get("links", {}))

    links["linkedin"] = safe_url(links.get("linkedin"))
    links["github"] = safe_url(links.get("github"))

    email_link = links.get("email") or f"mailto:{payload['profile']['email']}"
    links["email"] = safe_url(email_link, allow_mailto=True)

    payload["links"] = links
    return payload


def build_environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_portfolio(payload: dict) -> str:
    env = build_environment()
    template = env.get_template(TEMPLATE_NAME)
    generated_at = datetime.now(timezone.utc).strftime("%d %b %Y")

    return template.render(**payload, generated_at=generated_at)


def estimate_initial_height(payload: dict) -> int:
    """
    Best-effort initial iframe height.
    The template also posts dynamic height updates to Streamlit.
    If dynamic resizing is unavailable, scrolling=True remains a safe fallback.
    """
    metrics_rows = math.ceil(len(payload["metrics"]) / 4) or 1
    card_rows = math.ceil(len(payload["capabilities"]) / 2) or 1
    integration_rows = math.ceil(len(payload["integrations"]) / 3) or 1
    project_rows = math.ceil(len(payload["projects"]) / 3) or 1
    roadmap_rows = math.ceil(len(payload["roadmap"]) / 3) or 1
    workflow_rows = math.ceil(len(payload["workflow_steps"]) / 5) or 1
    skill_rows = math.ceil(len(payload["skills"]) / 6) or 1

    height = (
        1180
        + metrics_rows * 180
        + card_rows * 240
        + integration_rows * 220
        + project_rows * 210
        + roadmap_rows * 210
        + workflow_rows * 220
        + skill_rows * 60
    )

    return min(max(height, 1800), 4200)


def main() -> None:
    apply_streamlit_shell()

    try:
        payload = load_json(DATA_FILE)
        html = render_portfolio(payload)
        initial_height = estimate_initial_height(payload)
    except Exception as exc:
        st.error("Portfolio failed to render.")
        st.exception(exc)
        st.stop()

    components.html(
        html,
        height=initial_height,
        scrolling=True,
        tab_index=-1,
    )


if __name__ == "__main__":
    main()
