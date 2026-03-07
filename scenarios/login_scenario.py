import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def login_scenario():
    print("Starting Nova Act login scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Navigate to the login page")
        nova.act("Enter valid email address in the email field")
        nova.act("Enter valid password in the password field")
        nova.act("Click the login button")
        time.sleep(2)
        nova.act("Verify successful login and return the username displayed on the dashboard")
        nova.act("Return the current page URL after login")


if __name__ == "__main__":
    login_scenario()
