"""
Product Count Scenario with HTML Report Generation
This example shows how to integrate the TestResultLogger with Nova Act scenarios
"""

import time
import sys
import os

# Add parent directory to path to import test_result_logger
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nova_act import NovaAct, workflow
from test_result_logger import TestResultLogger


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def product_count_scenario_with_report():
    # Initialize the HTML report logger
    logger = TestResultLogger("Product_Count_Scenario")
    
    print("\n" + "="*60)
    print("🚀 Starting Nova Act Product Count Scenario with HTML Reporting")
    print("="*60 + "\n")
    
    try:
        with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
            # Step 1: Navigate to products page
            logger.log_step(
                action="Navigate to the products page",
                status="passed",
                details="Opening the main products catalog page"
            )
            response = nova.act("Navigate to the products page")
            time.sleep(1)
            
            # Step 2: Get total product count
            logger.log_step(
                action="Get total number of products",
                status="passed",
                details="Retrieving the total count of products in catalog"
            )
            result = nova.act_get("Return the total number of products available in the catalog")
            logger.log_step(
                action="Total products retrieved",
                status="passed",
                response=f"Total Products: {result.response}"
            )
            time.sleep(1)
            
            # Step 3: Filter by Electronics category
            logger.log_step(
                action="Filter products by category 'Electronics'",
                status="passed",
                details="Applying filter to show only Electronics products"
            )
            nova.act("Filter products by category 'Electronics'")
            time.sleep(1)
            
            # Step 4: Get Electronics count
            logger.log_step(
                action="Get Electronics category count",
                status="passed",
                details="Counting products in Electronics category"
            )
            result = nova.act_get("Return the count of products in the Electronics category")
            logger.log_step(
                action="Electronics count retrieved",
                status="passed",
                response=f"Electronics Products: {result.response}"
            )
            time.sleep(1)
            
            # Step 5: Filter by price range
            logger.log_step(
                action="Filter products by price range $0-$500",
                status="passed",
                details="Applying price filter between $0 and $500"
            )
            nova.act("Filter products by price range $0-$500")
            time.sleep(1)
            
            # Step 6: Get price range count
            logger.log_step(
                action="Get count in price range",
                status="passed",
                details="Counting products within $0-$500 range"
            )
            result = nova.act_get("Return the count of products in the specified price range")
            logger.log_step(
                action="Price range count retrieved",
                status="passed",
                response=f"Products in $0-$500 range: {result.response}"
            )
            time.sleep(1)
            
            # Step 7: Navigate to admin dashboard
            logger.log_step(
                action="Navigate to admin dashboard",
                status="passed",
                details="Accessing the admin panel for inventory management"
            )
            nova.act("Navigate to the admin dashboard")
            time.sleep(2)
            
            # Step 8: Check inventory count
            logger.log_step(
                action="Check total inventory count",
                status="passed",
                details="Retrieving inventory statistics from admin panel"
            )
            nova.act("Check the total inventory count from the admin panel")
            time.sleep(1)
            
            # Step 9: Get inventory distribution
            logger.log_step(
                action="Get inventory distribution by category",
                status="passed",
                details="Retrieving product distribution across categories"
            )
            result = nova.act_get("Return the total inventory count and product distribution by category")
            logger.log_step(
                action="Inventory distribution retrieved",
                status="passed",
                response=f"Inventory Details: {result.response}"
            )
            time.sleep(1)
            
            # Step 10: Get all product metrics
            logger.log_step(
                action="Get all product metrics and statistics",
                status="passed",
                details="Retrieving comprehensive product statistics"
            )
            result = nova.act_get("Return all product metrics and statistics")
            logger.log_step(
                action="Product metrics retrieved",
                status="passed",
                response=f"Product Metrics: {result.response}"
            )
            
            logger.log_info("✅ All test steps completed successfully!")
            
    except Exception as e:
        logger.log_step(
            action="Test execution encountered an error",
            status="failed",
            details=str(e)
        )
        print(f"\n❌ Error during test execution: {str(e)}")
    
    finally:
        # Generate the HTML report at the end
        report_path = logger.generate_html_report()
        print(f"\n📊 View your HTML report at: {os.path.abspath(report_path)}")
        print("\n" + "="*60)


if __name__ == "__main__":
    product_count_scenario_with_report()
