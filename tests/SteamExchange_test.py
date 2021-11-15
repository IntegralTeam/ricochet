from brownie import web3

const { time } = require('@openzeppelin/test-helpers') """заменить своим"""
const axios = require('axios').default """замена"""
const SuperfluidSDK = require('@superfluid-finance/js-sdk')

const SuperfluidGovernanceBase = require('./artifacts/superfluid/SuperfluidGovernanceII.json')"""читает сам или парсить?"""

TEST_TRAVEL_TIME = 3600 * 2