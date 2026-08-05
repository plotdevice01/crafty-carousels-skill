from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "crafty-carousels"
DIST = ROOT / "dist"


def main() -> int:
    manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    archive = DIST / f"crafty-carousels-skill-v{version}.zip"
    DIST.mkdir(exist_ok=True)
    if archive.exists():
        archive.unlink()

    files = [path for path in PLUGIN.rglob("*") if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"]
    files.extend([ROOT / "README.md", ROOT / "LICENSE", ROOT / "VERSION"])
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(files, key=lambda item: item.as_posix().lower()):
            relative = path.relative_to(PLUGIN) if path.is_relative_to(PLUGIN) else Path(path.name)
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, path.read_bytes())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    receipt = DIST / f"crafty-carousels-skill-v{version}.sha256"
    receipt.write_text(f"{digest}  {archive.name}\n", encoding="utf-8", newline="\n")

    with zipfile.ZipFile(archive) as bundle:
        assert ".codex-plugin/plugin.json" in bundle.namelist()
        assert "skills/crafty-carousels/SKILL.md" in bundle.namelist()
        assert not any("__pycache__" in name or name.endswith(".pyc") for name in bundle.namelist())
    print(f"archive={archive}")
    print(f"sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
