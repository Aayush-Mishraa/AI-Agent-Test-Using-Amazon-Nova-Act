import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def add_product_scenario():
    print("Starting Nova Act add product scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Login with valid credentials")
        time.sleep(1)
        nova.act("Navigate to the admin or product management section")
        nova.act("Click on 'Add New Product' button")
        nova.act("Fill in the product name field with a test product name")
        nova.act("Fill in the product description with product details")
        nova.act("Set the product price to $99.99")
        nova.act("Upload a product image")
        nova.act("Select product category as 'Electronics'")
        nova.act("Set product quantity to 50 units")
        nova.act("Click the 'Save Product' button")
        time.sleep(2)
        nova.act("Verify that the product was successfully added and return the product ID")
        nova.act("Return the confirmation message and new product details")


if __name__ == "__main__":
    add_product_scenario()
