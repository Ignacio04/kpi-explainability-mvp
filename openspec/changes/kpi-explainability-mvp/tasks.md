# Tasks

## 1. Setup screen component

- [x] 1.1 Create the SetupScreen component with a KPI dropdown (one option: "Clareza de metas e objetivos") and a free-text input field for response values, and verify the component renders without errors
- [x] 1.2 Implement value parsing from the text field (comma-separated or space-separated), validate that each value is an integer between 1 and 5, display parsed values as visual pills below the input, and verify valid and invalid inputs are handled correctly
- [x] 1.3 Add a remove button on each parsed value pill and verify individual values can be removed
- [x] 1.4 Add a "Calcular e Visualizar" button that is disabled when no valid values are present and verify the button state changes correctly

## 2. App state management and navigation

- [x] 2.1 Refactor App.tsx to manage screen state (setup vs dashboard) and store response values and KPI name in component state, removing the hardcoded responseValues constant, and verify the setup screen appears as the initial view
- [x] 2.2 Wire the SetupScreen calculate button to transition to the dashboard view with the entered data, and verify the dashboard displays the correct KPI computed from user-provided values
- [x] 2.3 Add a back button on the dashboard that returns to the setup screen with previously entered values preserved, and verify round-trip navigation maintains state

## 3. Dynamic threshold interpretation

- [x] 3.1 Implement the three-band threshold logic (below 60% red, 60-80% yellow, above 80% green) to generate interpretation text dynamically and verify each band produces the correct text
- [x] 3.2 Apply the threshold color to the KPI value summary card and verify the card color changes for values in each of the three bands
- [x] 3.3 Update the explanation panel to use the dynamically generated interpretation instead of the hardcoded explanation string and verify the explanation matches the computed result

## 4. Styling

- [x] 4.1 Add CSS styles for the setup screen (card layout, dropdown, text input, value pills, calculate button) matching the existing design language, and verify the setup screen looks consistent with the dashboard
- [x] 4.2 Add CSS for the color-coded KPI card variants (red, yellow, green gradients) and the back button, and verify colors render correctly across all three thresholds

## 5. Validation

- [x] 5.1 Verify the prototype remains independent from Gen_Connect, backend, and database layers
- [x] 5.2 Confirm the full flow works end-to-end: setup screen loads first, user enters values, dashboard shows correct results with dynamic interpretation, and back navigation preserves data
