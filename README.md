# Aryn Sparks Consulting Site

This repository powers the static GitHub Pages site at:

https://asparks1987.github.io/

The site is positioned as an independent software consulting website for operational software services. It is intended to generate qualified conversations with businesses that depend on networks, data, and repeatable workflows.

## Positioning

Aryn Sparks designs and builds operational software for businesses that depend on networks, data, and repeatable workflows.

The primary audience includes:

- MSPs
- WISPs
- IT departments
- Network operators
- Infrastructure-heavy small and midsize businesses
- Businesses with spreadsheet-driven or manual operational workflows
- Companies needing custom internal software, automation, monitoring, or reporting

## Primary Services

- Network monitoring and automation: device and service monitoring, alerts, network-health dashboards, inventory, topology visibility, reporting, and operational automation.
- Custom internal business applications: staff portals, customer portals, tracking systems, approval workflows, scheduling tools, role-based administration, and API integrations.
- Business dashboards and reporting: executive dashboards, service-health views, recurring reports, KPI trends, exportable reports, and data cleanup.

## Selected Proof Projects

- LAN Scanner Pro: publicly released Android network-scanning application with local-first discovery, device history, topology-related workflows, reporting, and operator-focused tooling.
- NOCWALL-CE: private alpha network-operations platform work around wallboards, telemetry, topology, edge-agent concepts, alerts, APIs, and deployment tooling.
- AlphaRunner: anonymized commissioned analytics web application with FastAPI, scheduled workers, data pipelines, authentication, dashboards, databases, and deployment automation.

## Site Structure

- `index.html` - main static homepage.
- `SITE_POSITIONING.md` - source of truth for future positioning, proof claims, and prohibited claims.
- `privacypolicy.html` - privacy policy page.
- `resume/` - resume source and PDF.
- `LanScannerPro.png`, `nocwall.png`, `alpharunner.png` - selected-work visuals.

## Local Preview

From the repository root:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Then open:

http://127.0.0.1:8765/index.html

The page can also be opened directly as a static HTML file, but the local server is closer to how GitHub Pages serves assets.

## Updating Content

- Use `SITE_POSITIONING.md` before changing service, audience, or proof-project claims.
- Keep the primary CTA focused on booking a discovery call.
- Do not add pricing unless it has been explicitly approved by the site owner.
- Do not add client names, revenue, testimonials, download counts, uptime, performance claims, ratings, or production-maturity claims without evidence and approval.
- Keep open-source and R&D work secondary to the consulting message.
- Keep private alpha and commissioned work clearly labeled.

## Design Direction

The site should remain dark, technical, and developer-focused while reading as a serious independent consultancy. Prefer clear operational language, credible proof, and concise service descriptions over generic agency language.
