import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def comprehensive_scenario():
    print("Starting Nova Act comprehensive scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        # LOGIN FLOW
        print("\n--- LOGIN FLOW ---")
        nova.act("Navigate to the login page")
        nova.act("Enter valid credentials and login")
        time.sleep(2)
        nova.act("Verify successful login and return the username")
        
        # BROWSE PRODUCTS
        print("\n--- BROWSE PRODUCTS ---")
        nova.act("Navigate to the products catalog")
        nova.act("Return the total number of available products")
        nova.act("Filter products by category 'Electronics'")
        nova.act("Sort products by price (low to high)")
        nova.act("Return the first 5 products with their prices")
        
        # SHOPPING FLOW
        print("\n--- SHOPPING FLOW ---")
        nova.act("Search for Samsung phone or tablet")
        nova.act("Select the first product from search results")
        nova.act("Return product details including name, price, and specifications")
        nova.act("Add the product to the shopping cart")
        time.sleep(1)
        nova.act("Verify product is in cart and return cart total")
        
        # ADVANCED SHOPPING
        print("\n--- ADVANCED SHOPPING ---")
        nova.act("Continue shopping and search for another product")
        nova.act("Add a second product to the cart")
        nova.act("Return the total number of items in cart")
        nova.act("Return the complete cart summary with all items and total price")
        
        # CHECKOUT FLOW
        print("\n--- CHECKOUT FLOW ---")
        nova.act("Proceed to checkout")
        nova.act("Return the current checkout page and available payment methods")
        nova.act("Fill in shipping address with dummy data")
        nova.act("Select a shipping method")
        nova.act("Fill in billing information")
        nova.act("Select payment method as Credit Card")
        nova.act("Enter payment credentials and submit order")
        time.sleep(2)
        nova.act("Verify successful order placement")
        
        # ORDER CONFIRMATION
        print("\n--- ORDER CONFIRMATION ---")
        nova.act("Return the order confirmation message")
        nova.act("Return the order number and order details")
        nova.act("Return the estimated delivery date")
        
        # ACCOUNT MANAGEMENT
        print("\n--- ACCOUNT MANAGEMENT ---")
        nova.act("Navigate to my account/profile section")
        nova.act("Return the user profile information")
        nova.act("Navigate to order history")
        nova.act("Return the list of all previous orders")
        
        # ADMIN/INVENTORY CHECK
        print("\n--- ADMIN SECTION ---")
        nova.act("Navigate to admin dashboard if accessible")
        nova.act("Return total product count and inventory statistics")
        nova.act("Return sales metrics and order statistics")
        
        # SEARCH AND FILTER
        print("\n--- SEARCH AND FILTER ---")
        nova.act("Perform advanced search with multiple filters")
        nova.act("Filter by price range $100-$1000")
        nova.act("Filter by ratings 4 stars and above")
        nova.act("Return filtered product results")
        
        # WISHLIST
        print("\n--- WISHLIST ---")
        nova.act("Add a product to wishlist")
        nova.act("Navigate to wishlist section")
        nova.act("Return all items in the wishlist")
        
        # LOGOUT
        print("\n--- LOGOUT ---")
        nova.act("Logout from the account")
        nova.act("Verify successful logout and return to home page")
        
        # FINAL SUMMARY
        print("\n--- COMPREHENSIVE TEST COMPLETE ---")
        nova.act("Return a final summary of all test cases executed and their status")


if __name__ == "__main__":
    comprehensive_scenario()
