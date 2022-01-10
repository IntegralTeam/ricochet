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
