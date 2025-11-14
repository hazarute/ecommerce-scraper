import importlib
import pkgutil
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import json


def _load_plugin_config(plugin_module_name: str) -> dict:
    """Plugin'in .json config dosyasını yükle.
    
    Örnek: 'custom_plugins.example_amazon' ise
    custom_plugins/example_amazon.json dosyasını açar.
    
    Args:
        plugin_module_name: e.g., "custom_plugins.example_amazon"
    
    Returns:
        dict: Yüklenen config veya boş dict
    """
    try:
        # Module adından dosya adını çıkar
        plugin_name = plugin_module_name.split('.')[-1]  # "example_amazon"
        config_path = Path("custom_plugins") / f"{plugin_name}.json"
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"[Engine] Plugin config yüklendi: {config_path.name}")
            return config
    except Exception as e:
        print(f"[Engine] Plugin config yüklenirken hata ({plugin_module_name}): {e}")
    
    return {}


def discover_plugins() -> List[Dict]:
    """Discover python modules under `custom_plugins` and return metadata list.

    Returns:
        List of dicts: {"module": "custom_plugins.myplugin", "metadata": {...}}
    """
    plugins = []
    try:
        import custom_plugins
        package = custom_plugins
        prefix = package.__name__ + "."
        for finder, name, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            # skip template
            short = name.split('.')[-1]
            if short.startswith("_"):
                continue
            try:
                mod = importlib.import_module(name)
                meta = getattr(mod, "metadata", None)
                plugins.append({"module": name, "metadata": meta})
            except Exception:
                # ignore bad plugins
                continue
    except Exception:
        return []
    return plugins


def run_job(url: str, mode: str, selectors: dict = None, plugin_module: Optional[str] = None, plugin_config: dict = None, headless: bool = True) -> Tuple[List[Dict], Optional[str]]:
    """Run a scraping job.

    Args:
        url: target URL
        mode: 'requests' | 'selenium' | 'plugin'
        selectors: site selectors/config
        plugin_module: full module name for plugin (when mode=='plugin')
        plugin_config: extra config passed to plugin
        headless: for selenium

    Returns:
        (results_list, error_message)
    """
    selectors = selectors or {}
    try:
        if mode == "requests":
            from core.scrapers.requests_scraper import RequestsScraper
            scraper = RequestsScraper(url, selectors)
            html = scraper.fetch()
            results = scraper.parse(html)
            return results, None

        if mode == "selenium":
            from core.scrapers.selenium_scraper import SeleniumScraper
            scraper = SeleniumScraper(url, selectors, headless=headless)
            html = scraper.fetch()
            results = scraper.parse(html)
            return results, None

        if mode == "plugin":
            if not plugin_module:
                return [], "No plugin selected"
            mod = importlib.import_module(plugin_module)
            run_fn = getattr(mod, "run", None)
            if not callable(run_fn):
                return [], "Plugin has no run()"
            
            # Plugin config dosyasını yükle
            plugin_cfg = _load_plugin_config(plugin_module)
            # Mergelenmiş config: plugin config + user config
            merged_cfg = {**plugin_cfg, **(plugin_config or {})}
            
            results = run_fn(url, merged_cfg)
            return results, None

        return [], f"Unknown mode: {mode}"
    except Exception as e:
        return [], str(e)


if __name__ == "__main__":
    print("core.engine module — use discover_plugins() and run_job() from app")
