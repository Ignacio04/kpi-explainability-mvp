# Spec Delta

## Purpose

This capability provides a simple and understandable view of how an aggregated KPI is computed from questionnaire answers, helping users interpret the final result without needing technical or statistical expertise.

## ADDED Requirements

### Requirement: Setup screen for data entry
The system SHALL present a setup screen before the dashboard where the user selects a KPI and enters response values.

#### Scenario: Setup screen is the initial view
- **WHEN** the application loads
- **THEN** the system displays the setup screen with a KPI dropdown and a text field for response values

#### Scenario: KPI selection via dropdown
- **WHEN** the user views the setup screen
- **THEN** the system displays a dropdown with at least one KPI option pre-selected

#### Scenario: Free-text value entry
- **WHEN** the user enters response values in the text field
- **THEN** the system accepts comma-separated or space-separated numeric values between 1 and 5

#### Scenario: Navigation to dashboard
- **WHEN** the user has entered at least one valid response value and clicks the calculate button
- **THEN** the system navigates to the dashboard and displays the KPI computed from the entered values

### Requirement: Dynamic KPI interpretation with color-coded thresholds
The system SHALL generate an interpretation of the KPI result based on threshold bands and apply a corresponding color to the KPI value display.

#### Scenario: Red threshold below 60 percent
- **WHEN** the computed KPI value is below 60 percent
- **THEN** the system displays a red indicator and an interpretation text indicating the result needs urgent attention

#### Scenario: Yellow threshold between 60 and 80 percent
- **WHEN** the computed KPI value is between 60 and 80 percent inclusive
- **THEN** the system displays a yellow indicator and an interpretation text indicating the result needs attention

#### Scenario: Green threshold above 80 percent
- **WHEN** the computed KPI value is above 80 percent
- **THEN** the system displays a green indicator and an interpretation text indicating the result is good

### Requirement: Return to setup from dashboard
The system SHALL allow the user to navigate back from the dashboard to the setup screen.

#### Scenario: Back navigation preserves entered data
- **WHEN** the user clicks the back button on the dashboard
- **THEN** the system returns to the setup screen with the previously entered values preserved

## MODIFIED Requirements

### Requirement: Compute KPI from static response data
The system SHALL calculate the KPI from user-provided responses using a deterministic formula based on the average score and the scale range.

#### Scenario: Calculation is performed
- **WHEN** the user submits response values from the setup screen
- **THEN** the system calculates the result from the provided response set and displays the numeric output

### Requirement: Display KPI summary
The system SHALL display a KPI summary for the selected metric based on user-provided questionnaire responses collected on a 1-to-5 scale.

#### Scenario: KPI summary is visible
- **WHEN** the user navigates to the dashboard from the setup screen
- **THEN** the system shows the KPI name, final value, total response count, and formula used in the calculation

### Requirement: Provide human-readable explanation
The system SHALL provide a short textual explanation that interprets the KPI result in plain language, generated dynamically based on the computed value and threshold band.

#### Scenario: Explanation is readable
- **WHEN** the KPI result is shown
- **THEN** the system presents a brief explanation describing whether the result needs urgent attention, needs attention, or is good, based on the threshold the value falls into

### Requirement: Maintain isolated prototype scope
The system SHALL remain independent from the Gen_Connect platform and SHALL not rely on authentication, backend APIs, or persistent storage. Response data is ephemeral and exists only during the current session.

#### Scenario: Ephemeral data behavior
- **WHEN** the MVP is loaded
- **THEN** all data is provided by the user at runtime and all content is rendered locally in the frontend without external services
