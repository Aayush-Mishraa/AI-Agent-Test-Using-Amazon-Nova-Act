# Nova Act Test Automation with HTML Reporting

## 📊 HTML Test Reports

This project includes a comprehensive HTML report generator for Nova Act test scenarios. The reports provide detailed insights into test execution with a beautiful, professional interface.

## ✨ Features

- **Comprehensive Test Reports**: Detailed HTML reports with step-by-step execution logs
- **Visual Dashboard**: Summary cards showing pass/fail statistics and execution time
- **Step-by-Step Tracking**: Each test step is logged with status, timestamp, and response data
- **Professional Design**: Modern, responsive UI with gradient themes and smooth animations
- **Automatic Report Generation**: Reports are automatically saved to the `results/` folder

## 🚀 Quick Start

### 1. Import the Logger

```python
from test_result_logger import TestResultLogger
```

### 2. Initialize in Your Test

```python
logger = TestResultLogger("Your_Test_Name")
```

### 3. Log Test Steps

```python
# Log a simple step
logger.log_step(
    action="Navigate to login page",
    status="passed",
    details="Opening the login page from homepage"
)

# Log a step with response data
logger.log_step(
    action="Get product count",
    status="passed",
    response=f"Total Products: {result.response}"
)

# Log a failed step
logger.log_step(
    action="Submit form",
    status="failed",
    details="Form validation error occurred"
)
```

### 4. Generate the Report

```python
# At the end of your test
report_path = logger.generate_html_report()
print(f"Report saved to: {report_path}")
```

## 📝 Complete Example

```python
import time
from nova_act import NovaAct, workflow
from test_result_logger import TestResultLogger

@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def my_test_with_report():
    logger = TestResultLogger("My_Test_Scenario")
    
    try:
        with NovaAct(starting_page="https://example.com") as nova:
            # Step 1
            logger.log_step(
                action="Navigate to homepage",
                status="passed"
            )
            nova.act("Go to homepage")
            
            # Step 2
            logger.log_step(
                action="Click search button",
                status="passed"
            )
            result = nova.act_get("Search for products")
            
            # Step 3
            logger.log_step(
                action="Get search results",
                status="passed",
                response=f"Found: {result.response}"
            )
            
    except Exception as e:
        logger.log_step(
            action="Test failed",
            status="failed",
            details=str(e)
        )
    
    finally:
        # Always generate report
        report_path = logger.generate_html_report()
        print(f"📊 Report: {report_path}")

if __name__ == "__main__":
    my_test_with_report()
```

## 📂 Report Structure

Reports are saved in the `results/` folder with the following naming convention:

```
results/
├── Login_Test_Scenario_20260307_143025.html
├── Product_Count_Scenario_20260307_144532.html
└── Checkout_Scenario_20260307_145123.html
```

## 🎨 Report Features

### Summary Dashboard
- **Total Steps**: Total number of test steps executed
- **Passed**: Number of successful steps
- **Failed**: Number of failed steps
- **Pass Rate**: Percentage of successful steps
- **Duration**: Total execution time in seconds

### Step Details
Each step includes:
- **Step Number**: Sequential order of execution
- **Action**: Description of what was tested
- **Status**: Passed/Failed/Skipped indicator
- **Timestamp**: When the step was executed
- **Details**: Additional context about the step
- **Response**: Data returned from Nova Act (if any)

### Visual Indicators
- ✅ Green checkmarks for passed steps
- ❌ Red X marks for failed steps
- 🔵 Blue info boxes for responses
- 📊 Progress bar showing pass rate

## 🎯 Example Scenarios with Reports

### Run Login Test
```bash
python scenarios/login_with_report.py
```

### Run Product Count Test
```bash
python scenarios/product_count_with_report.py
```

## 💡 Best Practices

1. **Always use try-finally**: Ensure the report is generated even if tests fail
2. **Log meaningful details**: Include context in the `details` parameter
3. **Capture responses**: Log important data returned from Nova Act
4. **Use descriptive names**: Choose clear scenario names for easy identification
5. **Review reports**: Check HTML reports after each test run

## 🔧 Customization

### Custom Report Location
```python
# Save to a specific location
logger.generate_html_report(save_path="custom/path/report.html")
```

### Log Informational Messages
```python
logger.log_info("Starting checkout flow...")
```

### Log Errors
```python
logger.log_error("Connection timeout occurred")
```

## 📱 Report Viewing

Simply open any HTML report in your web browser:

```bash
# Windows
start results/Login_Test_Scenario_20260307_143025.html

# macOS
open results/Login_Test_Scenario_20260307_143025.html

# Linux
xdg-open results/Login_Test_Scenario_20260307_143025.html
```

Or double-click the HTML file in your file explorer.

## 🎓 Learning Resources

- Check `scenarios/login_with_report.py` for a simple example
- See `scenarios/product_count_with_report.py` for a comprehensive example
- Review `test_result_logger.py` for the full API documentation

## 🐛 Troubleshooting

**Reports not generating?**
- Ensure the `results/` folder exists (it's created automatically)
- Check file permissions in the results directory
- Verify you're calling `generate_html_report()` at the end

**Steps not showing in report?**
- Make sure you're calling `logger.log_step()` for each action
- Verify the logger is initialized before logging steps

**Report looks broken?**
- Open in a modern browser (Chrome, Firefox, Safari, Edge)
- Check that the HTML file is not corrupted

## 📊 Sample Report Screenshot

The generated HTML reports include:
- Professional gradient header
- Summary cards with key metrics
- Visual progress bar
- Detailed step-by-step logs
- Timestamps and status indicators
- Response data display
- Test metadata footer

---

**Happy Testing! 🚀**
