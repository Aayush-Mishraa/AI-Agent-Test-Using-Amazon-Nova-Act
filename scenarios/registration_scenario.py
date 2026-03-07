import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def registration_scenario():
    print("Starting Nova Act registration scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Navigate to the registration page")
        nova.act("Click on 'Sign Up' or 'Create Account' button")
        nova.act("Fill in the first name field with test data")
        nova.act("Fill in the last name field with test data")
        nova.act("Fill in the email address field with a unique email")
        nova.act("Fill in the password field with a strong password")
        nova.act("Fill in the confirm password field")
        nova.act("Accept terms and conditions checkbox")
        nova.act("Click the 'Sign Up' button")
        time.sleep(2)
        nova.act("Verify successful account creation and return the confirmation message")
        nova.act("Verify that a confirmation email was sent")
        nova.act("Return the new account details and user ID")


if __name__ == "__main__":
    registration_scenario()
