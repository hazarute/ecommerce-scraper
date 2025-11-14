import streamlit as st
from core import engine
from utils.fileops import save_to_csv


st.set_page_config(page_title="E-commerce Product Scraper", layout="wide")
st.title("E-commerce Product Scraper — v2.0")

with st.sidebar:
    st.header("Job config")
    mode = st.selectbox("Mode", ["requests", "selenium", "plugin"], index=0)
    url = st.text_input("Target URL", value="https://example.com/")
    headless = st.checkbox("Selenium headless", value=True)
    plugins = engine.discover_plugins()
    plugin_choice = None
    if mode == "plugin":
        options = [p.get("module") for p in plugins]
        plugin_choice = st.selectbox("Plugin", options)

    run_btn = st.button("Run")

col1, col2 = st.columns([2, 1])

if run_btn:
    st.info("Running job — this may take a while")
    selectors = {}
    results, err = engine.run_job(url, mode, selectors=selectors, plugin_module=plugin_choice, headless=headless)
    if err:
        st.error(f"Job failed: {err}")
    else:
        st.success(f"Job finished — {len(results)} items")
        if results:
            col1.write(results)
            csv_path = save_to_csv(results)
            if csv_path:
                col2.markdown(f"**Exported CSV:** `{csv_path}`")

st.sidebar.markdown("---")
st.sidebar.markdown("Discovered plugins:")
for p in plugins:
    meta = p.get("metadata") or {}
    st.sidebar.markdown(f"- `{p.get('module')}` — {meta.get('description', '')}")
