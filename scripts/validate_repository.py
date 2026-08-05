from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "crafty-carousels"
SKILL = PLUGIN / "skills" / "crafty-carousels"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/client-intake.md",
    "references/production-system.md",
    "references/platform-delivery.md",
    "references/governance-measurement.md",
    "references/sources.md",
    "scripts/new_carousel_project.py",
    "assets/client-workspace/_templates/carousel-run/run.json",
    "assets/client-workspace/_templates/carousel-run/visual-brief.md",
    "assets/client-workspace/_templates/carousel-run/qa.md",
    "assets/client-workspace/setup/client-intake.md",
    "assets/client-workspace/_shared/brand.md",
    "assets/client-workspace/_shared/voice.md",
    "assets/client-workspace/_shared/people-and-likeness.md",
    "assets/client-workspace/_shared/asset-register.csv",
    "assets/client-workspace/_shared/claim-register.csv",
)


def main() -> int:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["name"] == "crafty-carousels"
    assert manifest["version"] == version
    assert manifest["skills"] == "./skills/"

    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    assert marketplace["name"] == "crafty-carousels-skill"
    entry = marketplace["plugins"][0]
    assert entry["name"] == manifest["name"]
    assert entry["source"]["path"] == "./plugins/crafty-carousels"

    missing = [relative for relative in REQUIRED if not (SKILL / relative).is_file()]
    assert not missing, f"Missing skill files: {missing}"

    urls = []
    for path in SKILL.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".json", ".yaml", ".csv"}:
            if "http://" in path.read_text(encoding="utf-8") or "https://" in path.read_text(encoding="utf-8"):
                urls.append(path.relative_to(SKILL).as_posix())
    assert urls == ["references/sources.md"], f"Runtime knowledge depends on unexpected URLs: {urls}"

    script = SKILL / "scripts" / "new_carousel_project.py"
    result = subprocess.run(
        [sys.executable, str(script), "self-test"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "self_test=PASS" in result.stdout

    with tempfile.TemporaryDirectory() as folder:
        workspace = Path(folder) / "workspace"
        subprocess.run(
            [
                sys.executable,
                str(script),
                "init",
                "--client-name",
                "Example Co",
                "--owner",
                "Content Lead",
                "--output",
                str(workspace),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        assert (workspace / "setup" / "client-intake.md").is_file()
        assert (workspace / "_shared" / "media").is_dir()
        assert (workspace / "_shared" / "asset-register.csv").is_file()
        assert not list((workspace / "_shared" / "media").iterdir())

    print(f"validation=PASS version={version} offline_runtime=PASS cold_walk=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
