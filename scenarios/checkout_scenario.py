import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def checkout_scenario():
    print("Starting Nova Act checkout scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Login with valid credentials")
        time.sleep(1)
        nova.act("Search for and add multiple products to the cart")
        time.sleep(1)
        nova.act("Navigate to shopping cart")
        nova.act("Return the cart contents and total price")
        nova.act("Apply a discount code if available")
        nova.act("Proceed to checkout")
        time.sleep(1)
        nova.act("Fill in shipping address with name, street, city, state, and zip code")
        nova.act("Select shipping method and return available options with costs")
        nova.act("Verify shipping cost is correctly added to order total")
        nova.act("Navigate to payment section")
        nova.act("Fill in credit card details (card number, expiry, CVV)")
        nova.act("Fill in billing address")
        nova.act("Review order summary before placing order")
        nova.act("Return the final order total including taxes and shipping")
        nova.act("Submit the order")
        time.sleep(2)
        nova.act("Verify successful order placement and return order confirmation")
        nova.act("Return the order number, total amount, and estimated delivery date")


if __name__ == "__main__":
    checkout_scenario()
