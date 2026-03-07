import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def search_filter_scenario():
    print("Starting Nova Act search and filter scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Navigate to the products page")
        nova.act("Return all available product categories")
        
        # SEARCH TESTS
        print("\n--- SEARCH TESTS ---")
        nova.act("Search for 'Samsung' in the search bar")
        nova.act("Return all search results for Samsung products")
        nova.act("Search for 'laptop' and return the results")
        nova.act("Perform a search with empty or special characters")
        nova.act("Return suggestions or autocomplete results")
        
        # FILTER BY CATEGORY
        print("\n--- FILTER BY CATEGORY ---")
        nova.act("Filter products by category 'Phones'")
        nova.act("Return the count and list of phone products")
        nova.act("Filter by category 'Tablets'")
        nova.act("Return the count and list of tablet products")
        
        # FILTER BY PRICE
        print("\n--- FILTER BY PRICE ---")
        nova.act("Apply price filter: $0 - $500")
        nova.act("Return products in the $0-$500 price range")
        nova.act("Apply price filter: $500 - $1000")
        nova.act("Return products in the $500-$1000 price range")
        
        # FILTER BY RATING
        print("\n--- FILTER BY RATING ---")
        nova.act("Filter products with 5-star ratings")
        nova.act("Return all 5-star rated products")
        nova.act("Filter products with 4 stars and above")
        nova.act("Return the count of high-rated products")
        
        # COMBINED FILTERS
        print("\n--- COMBINED FILTERS ---")
        nova.act("Apply multiple filters: Electronics category, $300-$800 price, 4+ stars rating")
        nova.act("Return filtered results with 'Samsung' in the name")
        nova.act("Sort results by price (low to high)")
        nova.act("Sort results by rating (high to low)")
        nova.act("Sort results by newest first")
        
        # FILTER VERIFICATION
        print("\n--- FILTER VERIFICATION ---")
        nova.act("Clear all filters and return to full product list")
        nova.act("Verify that clearing filters shows all products again")
        nova.act("Return the total product count after clearing filters")


if __name__ == "__main__":
    search_filter_scenario()
