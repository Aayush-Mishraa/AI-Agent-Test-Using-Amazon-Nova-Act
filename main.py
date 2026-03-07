"""
Nova Act - Quick Start Sample (IAM Authentication)
Docs: https://pypi.org/project/nova-act/

Uses AWS IAM credentials configured via: aws configure
Region must be us-east-1 (Nova Act is only available there).
"""

import boto3
from nova_act import NovaAct, Workflow


def main():
    print("Starting Nova Act session with IAM credentials...")

    # Uses credentials from ~/.aws/credentials (set via `aws configure`)
    boto_session = boto3.Session(region_name="us-east-1")

    with Workflow(
        workflow_definition_name="nova-act-automation-aayush",
        model_id="nova-act-latest",
        boto_session_kwargs={"region_name": "us-east-1"},
    ) as workflow:
        with NovaAct(
            starting_page="https://www.google.com",
            workflow=workflow,
        ) as nova:
            # Example: perform a Google search
            result = nova.act_get("Search for 'AWS Nova Act' and return the title of the first result.")
            print(f"\nResult: {result.response}")


if __name__ == "__main__":
    main()
