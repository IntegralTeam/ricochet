Write-Host "Cloning required dependences:"

Write-Host "Cloning OpenZeppelin/openzeppelin-test-helpers to .brownie/packages"
Invoke-Expression -Command "git clone https://github.com/OpenZeppelin/openzeppelin-test-helpers.git C:\Users\$env:UserName\.brownie\packages\OpenZeppelin\openzeppelin-test-helpers@0.5.13"

Write-Host "Cloning OpenZeppelin/openzeppelin-contracts to .brownie/packages"
Invoke-Expression -Command "git clone https://github.com/OpenZeppelin/openzeppelin-contracts.git C:\Users\$env:UserName\.brownie\packages\OpenZeppelin\openzeppelin-contracts@4.0.0"

Write-Host "Cloning superfluid-finance/protocol-monorepo to .brownie/packages"
Invoke-Expression -Command "git clone https://github.com/superfluid-finance/protocol-monorepo.git C:\Users\$env:UserName\.brownie\packages\superfluid-finance\protocol-monorepo@0.1.2"

Write-Host "Cloning Uniswap/v2-periphery to .brownie/packages"
Invoke-Expression -Command "git clone https://github.com/Uniswap/v2-periphery.git C:\Users\$env:UserName\.brownie\packages\Uniswap\v2-periphery@1.1.0-beta.0"

Write-Host "Cloning Uniswap/v2-core to .brownie/packages"
Invoke-Expression -Command "git clone https://github.com/Uniswap/v2-core.git C:\Users\$env:UserName\.brownie\packages\Uniswap\v2-core@1.0.1"