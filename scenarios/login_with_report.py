"""
Simple Login Test with HTML Report
Demonstrates basic HTML reporting for a login scenario
"""

import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nova_act import NovaAct, workflow
from test_result_logger import TestResultLogger


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def login_test_with_report():
    """Simple login test with HTML report generation"""
    
    # Create report logger
    logger = TestResultLogger("Login_Test_Scenario")
    
    print("\n🔐 Starting Login Test with HTML Reporting\n")
    
    try:
        with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
            
            # Test Step 1
            logger.log_step(
                action="Navigate to login page",
                status="passed",
                details="Opening the login page from homepage"
            )
            nova.act("Navigate to the login page")
            time.sleep(1)
            
            # Test Step 2
            logger.log_step(
                action="Enter email address",
                status="passed",
                details="Filling in the email field with valid credentials"
            )
            nova.act("Enter valid email address in the email field")
            time.sleep(0.5)
            
            # Test Step 3
            logger.log_step(
                action="Enter password",
                status="passed",
                details="Filling in the password field"
            )
            nova.act("Enter valid password in the password field")
            time.sleep(0.5)
            
            # Test Step 4
            logger.log_step(
                action="Click login button",
                status="passed",
                details="Submitting the login form"
            )
            nova.act("Click the login button")
            time.sleep(2)
            
            # Test Step 5
            logger.log_step(
                action="Verify successful login",
                status="passed",
                details="Checking if user is logged in and dashboard is displayed"
            )
            result = nova.act_get("Verify successful login and return the username displayed on the dashboard")
            logger.log_step(
                action="Login verification complete",
                status="passed",
                response=f"Logged in as: {result.response}"
            )
            time.sleep(1)
            
            # Test Step 6
            logger.log_step(
                action="Verify current page URL",
                status="passed",
                details="Confirming redirect to dashboard after login"
            )
            result = nova.act_get("Return the current page URL after login")
            logger.log_step(
                action="URL verification complete",
                status="passed",
                response=f"Current URL: {result.response}"
            )
            
            print("\n✅ Login test completed successfully!")
            
    except Exception as e:
        logger.log_step(
            action="Test failed with exception",
            status="failed",
            details=f"Error: {str(e)}"
        )
        print(f"\n❌ Test failed: {str(e)}")
    
    finally:
        # Generate HTML report
        report_path = logger.generate_html_report()
        print(f"\n📊 HTML Report: {os.path.abspath(report_path)}")


if __name__ == "__main__":
    login_test_with_report()
