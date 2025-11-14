
# Custom Plugins — Development Guide

Place user-provided scrapers in the `custom_plugins/` folder. Each plugin is a
Python module that follows a small contract so the core engine can discover
and run it safely.

Required contract
- `metadata` (dict) — fields: `name`, `version`, `description`, `supported_sites`.
- `def run(url: str, config: dict) -> list` — returns a `List[Dict]` where each
	dict represents a product (e.g. `{"title": ..., "price": ..., "url": ...}`).

Optional fields
- `metadata['requirements']` — list of pip package names required by the plugin.

How to add a plugin
1. Copy `_template.py` to `custom_plugins/my_plugin.py`.
2. Edit `metadata` and implement `run()` with site-specific parsing.
3. (Optional) List any extra dependencies in `metadata['requirements']`.
4. Restart Streamlit UI — the engine will auto-discover new plugins.

Security notes
- Plugins execute arbitrary Python code. For production deployments:
	- Validate plugin metadata before enabling.
	- Run plugins inside sandboxed containers when possible.
	- Require code review for new plugins.

Testing locally
- You can run a plugin directly for quick testing:

```powershell
python custom_plugins\my_plugin.py
```

Example
- See `_template.py` for a minimal working example using `requests` + `BeautifulSoup`.

Best practices
- Keep plugin logic small and focused on parsing.
- Prefer configuration-driven selectors (pass `config` from UI) rather than hardcoding selectors.
- Return consistent product dicts across plugins to make exporting simple.
