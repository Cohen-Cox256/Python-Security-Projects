# Security Policy
Please report any possiable vulnerability to the email given below on "Reporting a Vulnerability".

## Supported Versions

All current projects are being supported.
### Reminder this is for Python so it will be pip.

| Version | Supported          |
| ------- | ------------------ |
| 25.0.1  | :white_check_mark: |
| 5.0.x   | :white_check_mark: |
| 4.0.x   | <Unknown>          |
| < 4.0   | :x:                |

## Reporting a Vulnerability

To report a vulnerability, please email me at [Email].
Reporting vulnerabilites will be greatly asked of. Each time there is a possiable error, that means the code could have errors.
I greatly apprciate your help. 


## Perfered format
Title:
[Short, clear title summarizing the vulnerability]
Example: "Cross-Site Scripting (XSS) vulnerability in the user profile page"

1. Summary of the Vulnerability
[A brief, concise description of the vulnerability]
Example: "This vulnerability allows an attacker to inject malicious JavaScript code into the user profile page, which is executed when another user views the profile."

2. Affected Components
[List the affected components, modules, or endpoints]
Example: "User Profile Page, Edit Profile Form"

3. Steps to Reproduce
[Step-by-step instructions on how to reproduce the vulnerability]

Step 1: Open the web application and log in.
Step 2: Navigate to the "Edit Profile" page.
Step 3: In the "Description" field, input the following payload: <script>alert('XSS');</script>
Step 4: Save the profile and view the updated profile.
4. Expected Behavior
[Describe how the system should behave in the absence of the vulnerability]
Example: "The input should be sanitized or escaped to prevent the execution of injected JavaScript code."

5. Actual Behavior
[Describe the system behavior that indicates the presence of the vulnerability]
Example: "The malicious JavaScript code is executed when the profile is viewed, triggering an alert with the message 'XSS'."

6. Impact
[Explain the potential security consequences of the vulnerability]
Example: "An attacker can inject malicious scripts that can steal session cookies, perform unauthorized actions, or deface the profile page. This could lead to unauthorized access or data theft."

7. Environment Information
[List relevant environment details such as software version, operating system, and browser used]
Example:

Web Application Version: 1.2.0
Browser: Google Chrome 95.0
Operating System: Windows 10
8. Proof of Concept (PoC)
[Provide a PoC, if possible, demonstrating the vulnerability]
Example: Attach a screenshot or a link to a public page showing the vulnerability in action.

9. Recommended Mitigation / Fix
[Provide suggestions or steps to mitigate the vulnerability, if known]
Example: "Sanitize user inputs by escaping special characters and applying Content Security Policies (CSP) to prevent script execution."

10. Additional Information
[Any other details that might help the team understand or fix the issue]
Example: "The issue appears to exist in all environments (production, staging), and the vulnerability is not mitigated by current input validation."

11. Contact Information (Optional)
[Your name and contact information, if you want to be contacted for follow-up]
Example:

Name: John Doe
Email: johndoe@example.com
12. Disclosure Timeline (Optional)
[If applicable, include the expected timeline for disclosure, or the urgency of fixing the vulnerability]
Example:

Date Reported: 2025-02-26
Expected Fix Date: 2025-03-10 (2 weeks)
Public Disclosure Date: 2025-03-30 (if no response is received)

Thank you for taking the time to address this issue. I look forward to hearing back from you.

