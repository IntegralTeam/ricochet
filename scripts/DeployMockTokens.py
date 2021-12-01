import json
from brownie import MockSuperToken, MockERC20, accounts


HOST_ADDRESS = "0x3E14dC1b13c488a8d5D310918780c983bD5982E7"
decimals = 8
name = "SuperInput"
symbol = "SI"

def main():

    mock_input_ERC20 = MockERC20.deploy(
        {'from': accounts[0]}
    )
    print("Deployed MockInputSuperToken at: ", mock_input_ERC20.address)

    mock_output_ERC20 = MockERC20.deploy(
        {'from': accounts[0]}
    )
    print("Deployed MockInputSuperToken at: ", mock_output_ERC20.address)

    mock_input_super_token = MockSuperToken.deploy(
        {'from': accounts[0]}
    )
    print("Deployed MockInputSuperToken at: ", mock_input_super_token.address)

    mock_input_super_token.setInputToken(mock_input_ERC20.address)

    mock_output_super_token = MockSuperToken.deploy(
        {'from': accounts[0]}
    )
    print("Deployed MockOutputSuperToken at: ", mock_output_super_token.address)

    mock_output_super_token.setOutputToken(mock_output_ERC20.address)