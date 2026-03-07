import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def error_handling_scenario():
    print("Starting Nova Act error handling and edge cases scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        # INVALID LOGIN TESTS
        print("\n--- INVALID LOGIN TESTS ---")
        nova.act("Navigate to login page")
        nova.act("Try logging in with invalid email format")
        nova.act("Return any error message displayed")
        nova.act("Try logging in with empty password field")
        nova.act("Return validation error messages")
        nova.act("Try logging in with non-existent account")
        nova.act("Return 'Invalid credentials' or similar error message")
        
        # REGISTRATION EDGE CASES
        print("\n--- REGISTRATION EDGE CASES ---")
        nova.act("Try registering with an email that already exists")
        nova.act("Return the error message indicating email already registered")
        nova.act("Try registering with a weak password")
        nova.act("Return password strength warning if applicable")
        nova.act("Try registering with mismatched passwords")
        nova.act("Return confirmation mismatch error")
        
        # SEARCH EDGE CASES
        print("\n--- SEARCH EDGE CASES ---")
        nova.act("Search for a product that doesn't exist")
        nova.act("Return 'No results found' or similar message")
        nova.act("Search with special characters or SQL injection attempts")
        nova.act("Return safe search results or error handling")
        nova.act("Search with very long query string")
        
        # CART EDGE CASES
        print("\n--- CART EDGE CASES ---")
        nova.act("Try adding more items to cart than available inventory")
        nova.act("Return inventory warning or maximum quantity message")
        nova.act("Try proceeding to checkout with an empty cart")
        nova.act("Return appropriate error or redirect message")
        
        # PAYMENT EDGE CASES
        print("\n--- PAYMENT EDGE CASES ---")
        nova.act("Login and add item to cart")
        nova.act("Proceed to checkout and try entering invalid card number")
        nova.act("Return card validation error")
        nova.act("Try entering expired credit card")
        nova.act("Return expiry date error message")
        nova.act("Try entering invalid CVV")
        nova.act("Return CVV validation error")
        
        # NETWORK/TIMEOUT SCENARIOS
        print("\n--- TIMEOUT SCENARIOS ---")
        nova.act("Return current page load time")
        nova.act("Navigate through multiple pages and return average load time")
        
        # DATA VALIDATION
        print("\n--- DATA VALIDATION ---")
        nova.act("Try entering special characters in name field")
        nova.act("Try entering numbers in email field")
        nova.act("Try entering text in phone number field")
        nova.act("Return validation results for each field")
        
        # CONCURRENT ACCESS
        print("\n--- EDGE CASES ---")
        nova.act("Try accessing user account after logout")
        nova.act("Return redirect to login page or unauthorized access message")
        nova.act("Try accessing admin section with regular user account")
        nova.act("Return access denied message if applicable")
        nova.act("Return a comprehensive error handling test summary")


if __name__ == "__main__":
    error_handling_scenario()
