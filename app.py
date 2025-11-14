import streamlit as st
from core import engine
from utils.fileops import save_to_csv
from utils import exporters
import json
from pathlib import Path

# load site configs
import os
import json as _json
CONFIG_PATH = Path("config") / "sites_config.json"
SITE_CONFIGS = {}
if CONFIG_PATH.exists():
    try:
        SITE_CONFIGS = _json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    except Exception:
        SITE_CONFIGS = {}


st.set_page_config(page_title="E-commerce Product Scraper", layout="wide")
st.title("E-commerce Product Scraper — v2.0")

with st.sidebar:
    st.header("Job config")
    mode = st.selectbox("Mode", ["requests", "selenium", "plugin"], index=0)
    site_keys = list(SITE_CONFIGS.keys())
    site_choice = st.selectbox("Site", ["manual"] + site_keys)
    url = st.text_input("Target URL", value=SITE_CONFIGS.get(site_choice, {}).get('url', "https://example.com/") if site_choice != 'manual' else "https://example.com/")
    headless = st.checkbox("Selenium headless", value=True)
    plugins = engine.discover_plugins()
    plugin_choice = None
    if mode == "plugin":
        options = [p.get("module") for p in plugins]
        plugin_choice = st.selectbox("Plugin", options)

    selectors = {}
    if site_choice != 'manual':
        site_conf = SITE_CONFIGS.get(site_choice, {})
        selectors = site_conf.get('selectors', {})
        # include site name
        selectors['site'] = site_choice

    run_btn = st.button("Run")

col1, col2 = st.columns([2, 1])

if run_btn:
    st.info("Running job — this may take a while")
    results, err = engine.run_job(url, mode, selectors=selectors, plugin_module=plugin_choice, headless=headless)
    if err:
        st.error(f"Job failed: {err}")
    else:
        st.success(f"Job finished — {len(results)} items")
        if results:
            col1.write(results)
            csv_path = exporters.export_csv(results)
            json_path = exporters.export_json(results)
            if csv_path:
                col2.markdown(f"**Exported CSV:** `{csv_path}`")
            if json_path:
                col2.markdown(f"**Exported JSON:** `{json_path}`")

st.sidebar.markdown("---")
st.sidebar.markdown("Discovered plugins:")
for p in plugins:
    meta = p.get("metadata") or {}
    st.sidebar.markdown(f"- `{p.get('module')}` — {meta.get('description', '')}")
