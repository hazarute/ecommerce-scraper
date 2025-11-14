from pathlib import Path
import os
from datetime import datetime
from typing import List, Dict, Optional

import pandas as pd


EXPORT_DIR = Path("data") / "exports"
PAGE_SOURCES_DIR = Path("data") / "page_sources"


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def save_to_csv(data: List[Dict], filename_prefix: str = "products") -> Optional[str]:
    """Convert a list of dicts to a pandas DataFrame and save as CSV.

    Args:
        data: List[Dict] — list of product dictionaries.
        filename_prefix: prefix for the generated filename.

    Returns:
        Full path to the saved CSV file as str, or None if data is empty.
    """
    if not data:
        return None

    _ensure_dir(EXPORT_DIR)

    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.csv"
    file_path = EXPORT_DIR / filename

    # Use utf-8-sig for Excel compatibility with Turkish characters
    df.to_csv(file_path, index=False, encoding="utf-8-sig")

    return str(file_path.resolve())


def save_html_debug(html_content: str, filename: str = "last_page_source.html") -> str:
    """Save raw HTML for debugging purposes.

    Args:
        html_content: raw HTML string to save.
        filename: filename to use under `data/page_sources/`.

    Returns:
        Full path to the saved HTML file as str.
    """
    _ensure_dir(PAGE_SOURCES_DIR)
    file_path = PAGE_SOURCES_DIR / filename
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content or "")

    return str(file_path.resolve())


__all__ = ["save_to_csv", "save_html_debug"]
