import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def wishlist_profile_scenario():
    print("Starting Nova Act wishlist and profile scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        # LOGIN
        print("\n--- LOGIN ---")
        nova.act("Login with valid credentials")
        time.sleep(1)
        
        # PROFILE TESTS
        print("\n--- PROFILE TESTS ---")
        nova.act("Navigate to user profile section")
        nova.act("Return the user profile information (name, email, phone)")
        nova.act("Edit the user's first name")
        nova.act("Save profile changes")
        nova.act("Verify that changes were saved successfully")
        nova.act("Return the updated profile information")
        
        # ADDRESS MANAGEMENT
        print("\n--- ADDRESS MANAGEMENT ---")
        nova.act("Navigate to addresses section")
        nova.act("Return all saved addresses")
        nova.act("Add a new address with street, city, state, zip, and country")
        nova.act("Set the new address as default")
        nova.act("Edit an existing address")
        nova.act("Delete an address if available")
        
        # WISHLIST TESTS
        print("\n--- WISHLIST TESTS ---")
        nova.act("Search for a product and add it to wishlist")
        nova.act("Search for another product and add it to wishlist")
        nova.act("Navigate to wishlist section")
        nova.act("Return all items in the wishlist with details")
        nova.act("Return the total count of wishlist items")
        
        # WISHLIST OPERATIONS
        print("\n--- WISHLIST OPERATIONS ---")
        nova.act("Remove an item from the wishlist")
        nova.act("Move a wishlist item to cart")
        nova.act("Share the wishlist if feature is available")
        nova.act("Sort wishlist by price or date added")
        
        # ORDER HISTORY
        print("\n--- ORDER HISTORY ---")
        nova.act("Navigate to order history section")
        nova.act("Return all previous orders with order numbers and dates")
        nova.act("Click on a past order to view order details")
        nova.act("Return the complete order details including items, prices, and status")
        nova.act("Check order tracking information if available")
        
        # PREFERENCES
        print("\n--- PREFERENCES ---")
        nova.act("Navigate to account preferences or settings")
        nova.act("Update email notification preferences")
        nova.act("Update newsletter subscription status")
        nova.act("Return current account settings and preferences")
        
        # SECURITY
        print("\n--- SECURITY ---")
        nova.act("Navigate to password change section")
        nova.act("Return to profile without changing password")
        nova.act("Return account security information")


if __name__ == "__main__":
    wishlist_profile_scenario()
