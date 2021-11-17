import subprocess


def deploy_hardhat_test():
    copy_contracts_process = subprocess.Popen([
        "cp", "-a", "./contracts", "./ricochet-hardhat/copied_contracts"
    ], stdout=subprocess.STDOUT)

    deploy_hardhat_tests = subprocess.Popen([
        "cd", "./ricochet-hardhat",
        "&&",
        "npx", "hardhat", "test",
        "&&",
        "cd", ".."
    ], stdout=subprocess.STDOUT)

    remove_contracts_process = subprocess.Popen([
        "rm", "-rf", "./ricochet-hardhat/copied_contracts"
    ], stdout=subprocess.STDOUT)
