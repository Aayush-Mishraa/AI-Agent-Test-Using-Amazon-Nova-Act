import time
from nova_act import NovaAct, workflow


@workflow(
    workflow_definition_name="nova-act-automation-aayush",
    model_id="nova-act-latest",
    boto_session_kwargs={"region_name": "us-east-1"},
)
def forgot_password_scenario():
    print("Starting Nova Act forgot password scenario...")
    with NovaAct(starting_page="https://aayushmishra.tech/ecommerceautomation/") as nova:
        nova.act("Navigate to the login page")
        nova.act("Click on the 'Forgot Password' link")
        time.sleep(1)
        nova.act("Enter the registered email address in the recovery email field")
        nova.act("Click the 'Send Recovery Link' button")
        time.sleep(2)
        nova.act("Verify that a recovery email has been sent and return the confirmation message")
        nova.act("Return the page content showing password reset instructions")


if __name__ == "__main__":
    forgot_password_scenario()
