# SJH Content & Brand Creator

A deployable AI skill for people creating material on behalf of **St. Jude Hospital**.

## What it does

The skill can:
- create new communication;
- adapt approved content across channels;
- review material for Brand Bible compliance;
- route staff toward approved templates;
- support Communications and designers with controlled visual development;
- handle contractors differently depending on whether they are designing or producing approved artwork;
- flag privacy, clinical, operational-readiness, naming, logo, colour, typography and approval issues;
- separate public-facing material from internal creator/approval notes.

## Package structure

- `SKILL.md` — front-door instruction set and decision logic.
- `references/` — distilled identity, voice, visual, imagery, patient-communication, governance, contractor and asset guidance.
- `playbooks/` — task-specific workflows for staff, Communications/design, contractors and common SJH applications.
- `templates/` — intake, review, approval and verified-information templates.
- `scripts/` — optional mechanical linting utility for text and HTML/CSS.

## Source authority

The **current approved St. Jude Hospital Brand Bible** is the highest authority. The Visual Brand Guide and Staff Brand Guide are implementation references and must not override it.

The institutional source documents themselves are **not committed to this public repository**. Deployments should attach or connect the current approved Brand Bible, Visual Brand Guide, Staff Brand Guide, current templates/assets and any specialist standards as controlled knowledge sources.

## Deployment

1. Install/copy this repository into the AI system's skill directory or knowledge package.
2. Make the current approved Brand Bible available to the AI as the highest-authority source.
3. Attach/connect current approved master templates and brand assets relevant to the deployment.
4. Maintain a current verified-information register for changing operational facts.
5. Preserve the relative paths because `SKILL.md` references the supporting files directly.

For an environment that accepts only one instruction file, use `SKILL.md` and make the `references/` and `playbooks/` documents available as attached knowledge.

## Ongoing maintenance

Maintain at minimum:
1. `references/verified_information.md` plus the live verified-information register — current contacts, domains, hours, service status, names, addresses and other changing facts.
2. `references/approved_assets.md` plus the live central asset register — current templates and master assets.
3. `references/governance_approvals.md` — update when SJH confirms or changes approval roles.

When the Brand Bible changes, review the distilled references and playbooks before redeployment.

## Important

This skill helps create and review material. It **does not grant institutional approval** and should never claim that SJH approval has been obtained unless an authorised workflow or user-provided evidence confirms it.
