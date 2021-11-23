import json
from brownie import MockSuperfluid, accounts


HOST_ADDRESS = "0x3E14dC1b13c488a8d5D310918780c983bD5982E7"


def main():

    mock_superfluid = MockSuperfluid.deploy(
        {'from': accounts[0]}
    )
    print("Deployed MockSuperfluid at: ", mock_superfluid.address)
