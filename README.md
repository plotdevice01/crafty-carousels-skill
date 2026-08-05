# Crafty Carousels Skill

Crafty Carousels Skill is a skills-only plugin for ChatGPT and Codex. It turns one approved idea into a governed Instagram or LinkedIn carousel package. It does not promise virality.

## What it contains

- guided client intake for brand look, voice, claims, people, likeness permissions, and private image libraries;
- a copy-first carousel system with explicit human approval;
- a reference-first cover workflow with three cover candidates;
- enforced copy hashes, production-rules hashes, and frozen anchor rules;
- locked mobile type floors plus no-glow, text-safe, and CTA-safe gates;
- one-slide-at-a-time GPT Image production records;
- accessibility, rights, platform, release, and measurement checks;
- a local workspace generator and run validator.

Client records and media are not bundled. The plugin stamps a separate workspace for each client and keeps image-library files ignored by default.

## Install for a team

### ChatGPT desktop app

1. Clone this repository and open it as a workspace in the ChatGPT desktop app.
2. Restart the app.
3. Open the Plugins Directory, select the `Crafty Carousels Skill` marketplace, and install the plugin.
4. Start a new chat and invoke `@crafty-carousels`.

### Codex CLI

```powershell
codex plugin marketplace add plotdevice01/crafty-carousels-skill --ref v0.3.0
```

Then refresh the plugin list, install `crafty-carousels`, and start a new task. Pinning the release tag keeps every teammate on the same package.

This public GitHub repository is a team-distribution source. It is not automatically a listing in OpenAI's universal plugin directory.

## Required companion

Final copy and release require the AI Sloppy Copy plugin. If it is missing, Crafty Carousels may prepare drafts, but it must record the dependency as a blocker before final copy approval.

Chief of Staff is optional. When installed, Chief may coordinate status and approvals. Crafty Carousels also works by itself through its saved workspace contracts.

## Start a client

```powershell
python plugins/crafty-carousels/skills/crafty-carousels/scripts/new_carousel_project.py init `
  --client-name "Example Co" `
  --owner "Content Lead" `
  --output "C:\work\example-carousel"
```

The skill then asks one unanswered blocking question at a time and saves the answers to the client workspace. Actual photos belong in the private `_shared/media/` folder, never in this repository.

## Validate and build

```powershell
python scripts/validate_repository.py
python scripts/build_release.py
```

The release builder creates a deterministic plugin ZIP and SHA-256 receipt in `dist/`.

## Versioning

- Release tag: the package teammates install or cite, such as `v0.3.0`.
- Plugin manifest: host-facing compatibility metadata, such as `0.3.0`.
- Skill workflow: the instructions and bundled workspace contracts inside that release.

For this initial release, all three move together. Later releases may change workflow behavior without changing the client data schema, or may change the schema when migration instructions are included.

## Offline source of truth

The operational workflow is fully written into the plugin. Production does not fetch Novitckii or any other instructional page at runtime. `references/sources.md` retains links for provenance and future review. Current platform facts still need release-time verification because platform limits change.

The workflow summarizes methods from Novitckii resources and user-supplied production guides. It does not redistribute the source pages or creator assets. It also does not redistribute client files.
