# AI-Test-Automation-Using-Amazon-Nova-Act

## 1. Introduction
This project shows how to build AI-driven web test automation using Amazon Nova Act. Instead of writing rigid locator-heavy scripts for every UI action, we describe test intent in natural language and let Nova Act execute those steps in the browser.

The goal of this repository is practical: demonstrate real scenario-based functional testing for an ecommerce flow using AI agents, while still keeping the project structured like an engineering test suite.

## 2. Problem with Traditional Automation
Traditional UI automation frameworks like Selenium, Playwright, and Cypress are powerful, but they come with known pain points in large test suites:

- Tests are tightly coupled to CSS/XPath selectors.
- Minor UI changes can break many scripts.
- Authoring test cases takes time and strong framework knowledge.
- Maintenance cost grows quickly as product surfaces expand.
- Non-technical stakeholders cannot easily contribute to test authoring.

In short, traditional tools are deterministic and robust, but often expensive to maintain over time for fast-moving UI products.

<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.5.0/lottie.js"></script>
## 3. Why AI Driven Automation
AI-driven automation shifts from selector-first scripts to intent-first instructions.

Instead of writing low-level code for every click and input, we provide high-level instructions such as:

`"Login with valid credentials and verify username on dashboard"`

An AI agent can then:

- Interpret the instruction in context.
- Plan browser actions dynamically.
- Adapt when UI structure changes slightly.
- Return meaningful execution output.

This approach can reduce authoring effort and improve adaptability for exploratory and regression-style flows.

## 4. Amazon Nova Act Overview
Amazon Nova Act is an AI agent capability from AWS for browser task automation. It combines LLM reasoning with an action execution layer to perform tasks on real web pages.

At a high level, Nova Act:

- Accepts natural-language goals.
- Understands page context.
- Plans and performs browser actions.
- Produces execution logs and outcomes.

In this project, Nova Act is used through the Python SDK with workflow-based scenario execution.

## 5. Architecture
The implementation follows an agentic test architecture where test intent is translated into executable browser actions.

Core building blocks:

- LLM model: interprets test intent and page context.
- Agent planner: decomposes intent into ordered actions.
- Tool execution: performs actions like click/type/navigate/assert.
- Browser automation layer: drives browser interactions.
- AWS integration: handles auth, model access, and workflow execution.

Architecture flow:

```text
User Prompt
  |
  v
Nova LLM
  |
  v
Agent Planner
  |
  v
Browser Automation
  |
  v
Execution Logs
```

## 6. How Nova Act Works Internally
In simple terms, each `nova.act(...)` instruction goes through this cycle:

1. Parse intent from natural language.
2. Observe current browser/page state.
3. Decide the next best action.
4. Execute the action.
5. Re-evaluate whether the goal is complete.
6. Continue until the instruction is satisfied or fails.

This loop is why AI automation can handle small UI differences better than hardcoded scripts.

## 7. Browser Interaction
Nova Act uses a browser automation layer compatible with Playwright-style interaction patterns under the hood. This enables stable low-level control (click, type, navigate, wait, evaluate) while exposing a high-level natural-language interface to the test author.

In practice, you write intent, and the framework handles granular browser operations.

## 8. Nova Act Playground
The Nova Act Playground is a browser-based environment for quickly trying prompts and observing agent behavior without writing much code.

What it gives you:

- Fast experimentation with prompts.
- Quick feedback loop while learning agent behavior.
- Visual understanding of action traces.

Regional availability note:

- Service and playground availability can vary by AWS region and account setup.
- Some users may not see the same access experience in regions like India.

If playground access is limited, use the SDK directly from local scripts, which is the approach used in this repository.

## 9. Nova Act SDK Setup
Follow these steps to run locally.

### 9.1 Prerequisites
- Python 3.10+
- AWS account
- AWS CLI installed

### 9.2 Install Dependencies
```bash
pip install -r requirements.txt
pip install playwright
playwright install
```

### 9.3 Install Nova Act SDK Explicitly (if needed)
```bash
pip install nova-act
```

### 9.4 Create IAM User for Programmatic Access
1. Open AWS Console -> IAM -> Users -> Create user.
2. Enable programmatic access.
3. Attach required permissions.

Recommended minimum approach:
- Start with least-privilege policies required for Nova Act usage.
- Add S3 permissions if you plan to store artifacts/logs in a bucket.

### 9.5 Create Access Keys
1. IAM -> User -> Security credentials.
2. Create access key.
3. Save `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` securely.

### 9.6 Configure AWS CLI
```bash
aws configure
```

Set:
- Access key ID
- Secret access key
- Default region: `us-east-1`
- Output format: `json`

### 9.7 Optional: Connect to S3 for Artifacts
If you want to upload logs/reports:

```python
import boto3

s3 = boto3.client("s3", region_name="us-east-1")
s3.upload_file("results/sample_report.html", "your-bucket-name", "reports/sample_report.html")
```

### 9.8 Run Scripts Locally
```bash
python main.py
python demo.py
python scenarios/login_scenario.py
python scenarios/checkout_scenario.py
```

## 10. Example SDK Usage
```python
from nova_act import NovaAct

with NovaAct(starting_page="https://example.com") as nova:
    nova.act("Login with valid credentials")
```

## 11. My Implementation
I implemented this project as scenario-based automation to mirror realistic ecommerce testing flows. Each scenario is isolated for focused validation, and there is also a comprehensive scenario for end-to-end coverage.

Implemented scenarios:

- Login scenario
- Registration scenario
- Forgot password scenario
- Search product scenario
- Filter products scenario
- Add to cart / product management flow
- Product count validation
- Checkout scenario
- Wishlist and profile scenario
- Error handling scenarios
- Comprehensive end-to-end scenario

This layout makes it easier to run individual suites or combine them for broader regression execution.

## 12. Project Structure
```text
AI-Test-Automation-Using-Amazon-Nova-Act/
  scenarios/
    add_product_scenario.py
    checkout_scenario.py
    comprehensive_scenario.py
    error_handling_scenario.py
    forgot_password_scenario.py
    login_scenario.py
    login_with_report.py
    product_count_scenario.py
    product_count_with_report.py
    registration_scenario.py
    search_filter_scenario.py
    wishlist_profile_scenario.py
  results/
  demo.py
  main.py
  test_result_logger.py
  HTML_REPORTING_GUIDE.md
  README.md
```

## 13. Test Reporting
The project includes HTML reporting for execution tracking.

- `test_result_logger.py` captures step-level results.
- Report scenarios (for example `login_with_report.py`) generate timestamped HTML files.
- Reports are written to the `results/` directory.

Typical report data includes:

- Test step name
- Status (pass/fail)
- Timestamp
- Response/output details
- Overall summary metrics

## 14. Benefits of AI Automation
From an SDET perspective, key benefits are:

- Faster test creation through natural-language steps.
- Easier collaboration between QA, dev, and product teams.
- Lower maintenance burden compared to selector-heavy tests.
- Better fit for exploratory and dynamic UI paths.
- Foundation for autonomous testing agents.

## 15. Future Improvements
Planned evolution areas:

- Self-healing tests for higher resilience.
- AI-generated test cases from user stories/requirements.
- CI/CD integration for scheduled and gated execution.
- Autonomous regression agents for nightly validation.
- Centralized artifact storage and trend dashboards.

## 16. Author
Aayush Mishra  
SDET | Automation Engineer | AI Testing Enthusiast

GitHub: https://github.com/Aayush-Mishraa  
LinkedIn: https://www.linkedin.com/in/aayushmishra33/  
Portfolio: https://aayushmishra.tech
