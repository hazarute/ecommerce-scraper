from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import json
import os
import pandas as pd

EXPORT_DIR = Path("data") / "exports"


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def export_json(data: List[Dict], filename_prefix: str = "products") -> Optional[str]:
    if not data:
        return None
    _ensure_dir(EXPORT_DIR)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.json"
    path = EXPORT_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return str(path.resolve())


def export_csv(data: List[Dict], filename_prefix: str = "products") -> Optional[str]:
    if not data:
        return None
    _ensure_dir(EXPORT_DIR)
    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.csv"
    path = EXPORT_DIR / filename
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return str(path.resolve())


__all__ = ["export_json", "export_csv"]
