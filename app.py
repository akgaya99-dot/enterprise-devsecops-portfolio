import json
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Aakash Kumar | Platform Engineering Portfolio",
    page_icon="⚡",
    layout="wide",
)

BASE_DIR = Path(__file__).parent

def load_json(path: str) -> dict:
    with open(BASE_DIR / path, "r", encoding="utf-8") as file:
        return json.load(file)

def load_html(path: str) -> str:
    with open(BASE_DIR / path, "r", encoding="utf-8") as file:
        return file.read()

data = load_json("data/profile.json")
template = load_html("templates/portfolio.html")

html = template

for key, value in data["profile"].items():
    html = html.replace(f"{{{{ profile.{key} }}}}", str(value))

for key, value in data["links"].items():
    html = html.replace(f"{{{{ links.{key} }}}}", str(value))

def render_cards(section_name: str) -> str:
    cards = ""
    for item in data[section_name]:
        cards += f"""
        <div class="card">
            <div class="card-icon">{item.get("icon", "")}</div>
            <div>
                <h3>{item["title"]}</h3>
                <p>{item["description"]}</p>
            </div>
        </div>
        """
    return cards

def render_metrics() -> str:
    html_cards = ""
    for item in data["metrics"]:
        html_cards += f"""
        <div class="metric-card">
            <div class="metric-icon">{item["icon"]}</div>
            <div class="metric-value">{item["value"]}</div>
            <div class="metric-label">{item["label"]}</div>
            <div class="metric-sub">{item["subtext"]}</div>
        </div>
        """
    return html_cards

def render_tags() -> str:
    return "".join([f"<span class='tag'>{skill}</span>" for skill in data["skills"]])

html = html.replace("{{ capabilities }}", render_cards("capabilities"))
html = html.replace("{{ metrics }}", render_metrics())
html = html.replace("{{ projects }}", render_cards("projects"))
html = html.replace("{{ skills }}", render_tags())

components.html(html, height=1800, scrolling=True)
