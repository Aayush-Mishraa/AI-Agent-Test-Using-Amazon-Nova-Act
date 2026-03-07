import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def product_count_scenario():
    print("Starting Nova Act product count scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Navigate to the products page")
        nova.act("Return the total number of products available in the catalog")
        nova.act("Filter products by category 'Electronics'")
        nova.act("Return the count of products in the Electronics category")
        nova.act("Filter products by price range $0-$500")
        nova.act("Return the count of products in the specified price range")
        nova.act("Navigate to the admin dashboard")
        nova.act("Check the total inventory count from the admin panel")
        nova.act("Return the total inventory count and product distribution by category")
        nova.act("Return all product metrics and statistics")


if __name__ == "__main__":
    product_count_scenario()
