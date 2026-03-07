import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def run_automation():
    print("Starting Nova Act session with IAM credentials...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Search for any Samsung phone or tablet")
        nova.act("Add the first product to the cart")
        time.sleep(2)
        nova.act("Verify that the product is added to the cart and return the product name and price")
        nova.act("Proceed to checkout and return the total price")
        nova.act("Fill in the checkout form with dummy data and submit the order")
        nova.act("Return the order confirmation message and order number")




if __name__ == "__main__":
    run_automation()

