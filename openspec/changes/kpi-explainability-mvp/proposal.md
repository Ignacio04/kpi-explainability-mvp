# Proposal

## Why

The MVP currently demonstrates KPI explainability using hardcoded response values embedded in the source code. This limits reuse and makes it impossible for a user to explore different datasets without modifying the codebase. Adding a setup screen before the dashboard allows the user to input their own response values and see the KPI computed and explained dynamically, making the prototype more realistic and useful for demonstration purposes.

## What Changes

- Add a setup screen before the KPI dashboard where the user selects a KPI from a dropdown and enters response values in a free-text field.
- Remove the hardcoded response array from the source code; values are now provided at runtime by the user.
- Generate the KPI interpretation text dynamically based on the computed result, using three color-coded threshold bands (red below 60%, yellow between 60% and 80%, green above 80%).
- Apply the threshold color to the KPI value card to give immediate visual feedback on the result.
- Add navigation between the setup screen and the dashboard.

## Capabilities

### New Capabilities
- None.

### Modified Capabilities
- `kpi-explainability`: The capability now accepts user-provided response values instead of relying on static data, adds a setup screen for data entry, and generates threshold-based dynamic interpretation of results.

## Impact

- Changes are limited to the existing frontend-only MVP.
- No backend, database, or authentication added.
- The `App.tsx` component is refactored to manage screen state and receive data from a new `SetupScreen` component.
- The `styles.css` file is extended with styles for the setup screen and color-coded KPI indicators.
