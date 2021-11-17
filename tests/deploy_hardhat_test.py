import subprocess
import os


def deploy_hardhat_test():
    if not os.path.isdir("./ricochet-hardhat/copied_contracts"):
        subprocess.run([
            "mkdir", "./ricochet-hardhat/copied_contracts"
        ], stdout=subprocess.STDOUT, capture_output=True)

    subprocess.run([
        "cp", "-a", "./contracts", "./ricochet-hardhat/copied_contracts"
    ], stdout=subprocess.STDOUT, capture_output=True)

    subprocess.run([
        "cd", "./ricochet-hardhat",
        "&&",
        "npx", "hardhat", "test",
        "&&",
        "cd", ".."
    ], stdout=subprocess.STDOUT, capture_output=True)

    subprocess.run([
        "rm", "-rf", "./ricochet-hardhat/copied_contracts"
    ], stdout=subprocess.STDOUT, capture_output=True)
