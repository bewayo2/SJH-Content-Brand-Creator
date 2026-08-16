# SJH Content & Brand Creator

A deployable AI skill package for people creating material on behalf of **St. Jude Hospital**.

## What it does

The skill can:
- create new communication;
- adapt approved content across channels;
- review material for Brand Bible compliance;
- route staff toward approved templates;
- support Communications and designers with controlled visual development;
- handle contractors differently depending on whether they are designing or producing approved artwork;
- flag privacy, clinical, operational-readiness, naming, logo, colour, typography, and approval issues;
- separate public-facing material from internal creator/approval notes.

## Package structure

- `SKILL.md` — the front-door instruction set and decision logic.
- `references/` — distilled brand, visual, naming, imagery, information-design, governance, contractor, and asset guidance.
- `playbooks/` — task-specific workflows.
- `templates/` — intake, review, approval, and verified-information templates.
- `scripts/` — optional linting utility for text and HTML/CSS.
- `sources/` — the source documents used to build the skill.

## Source authority

The current Brand Bible in `sources/` is the highest authority in this package. The visual guide and staff guide are implementation references and must not override the Brand Bible.

## Deployment

Install/copy the entire `SJH_Content_Brand_Creator_Skill` folder into the AI system's skill directory or knowledge package. Preserve the relative paths because `SKILL.md` references the files directly.

For an environment that only accepts one instruction file, use `SKILL.md` and make the `references/` and `playbooks/` documents available as attached knowledge.

## Ongoing maintenance

At minimum, maintain three operational resources outside or alongside the Brand Bible:
1. `verified_information.md` — current contacts, domains, hours, service status, names, addresses and other changing facts.
2. `approved_assets.md` — the actual current template/asset register.
3. `governance_approvals.md` — update once SJH confirms its final approval matrix.

When a new Brand Bible version is issued, replace the source and review all distilled references before deployment.
