
# Atlan Submission Project

## Basic Flow

1. Form Management:

Users create forms with questions and configure action components.
Forms are stored in the database with associated questions and metadata.
2. Response Submission:

Users submit responses to forms, providing answers to questions.
Responses are stored in the database with associated form and submitter details.

3. Action-specific Processing:

Google Sheets export action component formats and exports response data to a Google Sheet.
SMS notification action component generates and sends SMS notifications to users.
Other action components perform their designated tasks based on their logic.
4. Monitoring and Error Handling:

System health metrics like queue backlog and worker performance are monitored.
Alerts are triggered for critical events and errors.
Retries and error handling mechanisms ensure data consistency and action completion.

5. User Interface:
Users manage forms, configure actions, and view response data.
Dashboards visualize system health and action execution logs.
Additional Flows
System administrators manage action components and configure settings.
Access control mechanisms ensure data security and user permissions.
Scheduled tasks can be implemented for periodic actions or data processing.

## Database Schematic
- Form:

    - ID: Unique identifier for the form (e.g., UUID)
    - Name: Form title
    - Description: Optional description of the form's purpose
    - Created by: User who created the form
    - Created at: Timestamp of form creation
    - Metadata: Additional relevant information (e.g., organization, category)
    - ID: Unique identifier for the question (within a form)
    - Form ID: Reference to the form the question belongs to
    - Text: Question text
    - Type: Question type (e.g., single-choice, multiple-choice, text)
    - Options: List of available options for choice-based questions
    - Metadata: Additional information (e.g., required, scoring)

- Response:

    - ID: Unique identifier for the response (e.g., UUID)
    - Form ID: Reference to the form the response belongs to
    - Submitted at: Timestamp of response submission
    - Submitted by: User who submitted the response (optional)
    - Metadata: Additional information (e.g., IP address, device)

- Answer:

    - ID: Unique identifier for the answer (within a response)
    - Response ID: Reference to the response the answer belongs to
    - Question ID: Reference to the question the answer corresponds to
    - Value: The actual answer provided by the user (e.g., selected option, text input)
    - Metadata: Additional information (e.g., scoring, validation)


### Relationships:

- One Form has many Questions.
- One Question has many Answers in a Response.
- One Response belongs to one Form and has one Answer per Question.