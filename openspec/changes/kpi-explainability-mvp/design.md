# Design

## Context

The MVP already has a working KPI dashboard that renders a single metric from hardcoded response values. See proposal.md for motivation. The evolution adds a data-entry step before the dashboard so the user controls the input, and makes the result interpretation respond to the actual computed value.

## Goals / Non-Goals

**Goals:**
- Allow the user to enter response values at runtime instead of changing source code.
- Generate interpretation text and visual feedback dynamically based on threshold bands.
- Keep the interface simple enough for quick demonstration and evaluation.

**Non-Goals:**
- Authentication, backend APIs, or database persistence.
- AI-generated explanations or advanced explainability methods.
- Integration with the Gen_Connect application or production infrastructure.
- Persisting entered data across sessions or browser reloads.

## Decisions

### 1. Two-step single-page app
The application stays as a single React page but manages two views via component state: a setup screen and the existing dashboard. This avoids adding a router while still giving the user a clear data-entry step before seeing results. A `screen` state variable controls which view renders.

### 2. User-provided data model
Response values come from the user via a free-text input field that accepts comma-separated or space-separated numbers. The values are parsed, validated (must be integers between 1 and 5), and stored in component state. This replaces the previous static constant and makes the prototype usable with any dataset the user provides, including large sets of 40-50+ values.

### 3. KPI selection via dropdown
A dropdown presents the available KPIs. For now there is a single option ("Clareza de metas e objetivos"), but using a dropdown makes the interface extensible for future KPIs without structural changes.

### 4. Three-band threshold interpretation
The KPI result is classified into one of three bands, each with a color and interpretation text:
- Below 60%: red — needs urgent attention
- 60% to 80%: yellow — needs attention
- Above 80%: green — good performance

The color is applied to the KPI value summary card and the interpretation text is generated dynamically from the band. This replaces the previous hardcoded explanation string.

### 5. Preserved navigation state
When the user returns from the dashboard to the setup screen, the previously entered values and selected KPI are preserved in state. This avoids forcing re-entry when the user wants to adjust values and recalculate.

## Risks / Trade-offs

- [Free-text parsing vs structured input] → Free text is faster for bulk entry but requires validation and clear error feedback for invalid values.
- [Ephemeral data vs persistence] → Data is lost on page reload. This is acceptable for a prototype but limits reuse across sessions.
- [Single KPI option] → The dropdown has one item for now, which may look odd. The design choice prioritizes future extensibility over current appearance.
- [Fixed threshold bands] → The 60/80 boundaries are hardcoded in the frontend. Changing them requires a code edit.
