# RICOCHET Python - Brownie port Contracts

This directory contains the contracts for Ricochet's `StreamExchange`.

Here's commands for deploying and setting up the contracts.

## Deployment

* MockSuperfluid: brownie run ./scripts/DeployMockSuperfluid.py
* Multiple Mock Tokens (MockERC20): brownie run ./scripts/DeployMockTokens.py
* StreamExchange (on Polygon): brownie run ./scripts/DeployPolygon.py
* StreamExchange (on Rinkeby): brownie run ./scripts/DeployRinkeby.py

## Setting up

* Transact distribution: brownie run ./scripts/Distribute.py --network <choose your network>
* Set up Tellor oracle address: brownie run ./scripts/setOracle.py --network <choose your network>
* Set up rate tolerance in StreamExchange: brownie run ./scripts/SetRateTolerance.py --network <choose your network>
* Set up subsidy rate in StreamExchange: brownie run ./scripts/SetSubsidyRate.py --network <choose your network>
* Transact ownership transfer: brownie run ./scripts/TransferOwnership.py --network <choose your network>

## Issues

### Searching for address of CFA contract

File: StreamExchange_test.py
Need to be found to instantiate User class at line 90. The instance of the class must be included in the User class constructor when instantiating it.

### Searching for address of superfluid contract

File: StreamExchange_test.py
Need to be found to instantiate User class.

### updateFlow of User class functional translation from Superfluid JS SDK

File: StreamExchange_test.py, line 124
Source file: "https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/js-sdk/src/User.js", line 78


### createFlow of User class functional translation from Superfluid JS SDK

File: StreamExchange_test.py, line 128
Source file: "https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/js-sdk/src/User.js", line 85


### Raw transaction execution translation (implementation of)

File: StreamExchange_test.py, line 150
Source file: https://github.com/decentral-ee/web3-helpers/blob/master/src/web3tx.js

### Initialize IDA contract in approveSubscriprions method

File: StreamExchange_test.py, line 163
Requirements: Need to find in SuperFluid contract sources an IDA contract, then it is required to get ABI or at least either create or search for the interface, then it needs to be imported in brownie test at file StreamExchange_test.py at line 6. Or the Contract class at line 7 of the file could be of use, if the address of the contract is found.
