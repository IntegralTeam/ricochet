import subprocess
import os


def test_deploy_hardhat():
    if not os.path.isdir(".\\ricochet-hardhat\\copied_contracts"):
        subprocess.run([
            "mkdir", ".\\ricochet-hardhat\\copied_contracts"
        ])
    print('1')
    subprocess.run([
        "xcopy", ".\\contracts\\*", ".\\ricochet-hardhat\\copied_contracts\\", "/s", "/e",
    ])
    print('2')
    subprocess.run(["cd", ".\\ricochet-hardhat\\"])
    print('3')
    subprocess.run(["yarn", "hardhat", "test"])
    print('4')
    subprocess.run(["cd", ".."])
    print('5')
    subprocess.run([
        "rd", "/s", "/q", ".\\ricochet-hardhat\\copied_contracts\\"
    ])
    assert True