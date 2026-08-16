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
- separate public-facing material from internal creator/approval notes;
- apply specialist document-design and creative-direction logic so that dashboards, decks, reports, social graphics and other designed outputs do not stop at generic defaults.

## Package structure

- `SKILL.md` — front-door instruction set and decision logic.
- `references/` — distilled identity, voice, visual, imagery, patient-communication, governance, contractor, asset and design-specialist guidance.
- `playbooks/` — task-specific workflows for staff, Communications/design, contractors and common SJH applications.
- `templates/` — intake, review, approval and verified-information templates.
- `scripts/` — optional mechanical linting utility for text and HTML/CSS.

## Design-specialist stack

The skill includes a dedicated design-specialist layer for higher-quality designed output:
- `references/document_design.md`
- `references/creative_design.md`
- `references/design_interrogation_checklist.md`
- `references/design_technique_catalog.md`
- `references/design_reference_library.md`
- `references/design_elevation_protocol.md`
- `references/design_philosophy.md`
- `playbooks/document_design.md`
- `playbooks/creative_design.md`

The creation workflow automatically activates this layer for designed artifacts such as presentation decks, dashboards, reports, guides, brochures, patient handouts, posters, social graphics, campaign assets, event visuals and polished digital pages.

The design specialist is instructed to:
- start with a functional version, then elevate it;
- question typography, colour, layout, spacing, imagery and data treatment;
- draw principle-level guidance from professional references such as Stripe, Linear, Apple, Bauhaus and Swiss/International Typographic Style;
- apply specific visual techniques rather than generic defaults;
- balance bold choices with tasteful restraint;
- keep refining until the result feels authored rather than template-generated;
- show the polished result by default rather than exposing internal design reasoning.

## Source authority

The **current approved St. Jude Hospital Brand Bible** is the highest authority. The Visual Brand Guide and Staff Brand Guide are implementation references and must not override it.

The institutional source documents themselves are **not committed to this public repository**. Deployments should attach or connect the current approved Brand Bible, Visual Brand Guide, Staff Brand Guide, current templates/assets and any specialist standards as controlled knowledge sources.

## Deployment

1. Install/copy this repository into the AI system's skill directory or knowledge package.
2. Make the current approved Brand Bible available to the AI as the highest-authority source.
3. Attach/connect current approved master templates and brand assets relevant to the deployment.
4. Maintain a current verified-information register for changing operational facts.
5. Preserve the relative paths because `SKILL.md` and the playbooks reference the supporting files directly.

For an environment that accepts only one instruction file, use `SKILL.md` and make the `references/` and `playbooks/` documents available as attached knowledge.

## Ongoing maintenance

Maintain at minimum:
1. `references/verified_information.md` plus the live verified-information register — current contacts, domains, hours, service status, names, addresses and other changing facts.
2. `references/approved_assets.md` plus the live central asset register — current templates and master assets.
3. `references/governance_approvals.md` — update when SJH confirms or changes approval roles.

When the Brand Bible changes, review the distilled references and playbooks before redeployment.

## Important

This skill helps create and review material. It **does not grant institutional approval** and should never claim that SJH approval has been obtained unless an authorised workflow or user-provided evidence confirms it.