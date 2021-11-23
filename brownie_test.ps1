Write-Host "Run tests"

Write-Host "Create copied_contracts folder"
Invoke-Expression -Command "mkdir .\\ricochet-hardhat\\copied_contracts"

Write-Host "Copying contracts"
Invoke-Expression -Command "xcopy .\\contracts\\* .\\ricochet-hardhat\\copied_contracts\\ /s /e"
Invoke-Expression -Command "cd .\\ricochet-hardhat\\"

Write-Host "Run hardhat test"
Invoke-Expression -Command "yarn hardhat test"

Invoke-Expression -Command "cd .."

Write-Host "Removew copied_contracts"
Invoke-Expression -Command "rmdir .\\ricochet-hardhat\\copied_contracts\\"