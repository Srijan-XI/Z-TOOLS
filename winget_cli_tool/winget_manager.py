import subprocess
from datetime import datetime

def log_action(action, package_name, status):
    """Logs install/uninstall actions with timestamp."""
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} | {action} | {package_name} | {status}\n")

def run_command(command):
    """Executes the shell command and returns output and error."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def list_upgradable_packages():
    output, _ = run_command("winget upgrade")
    print(output)

def upgrade_all_packages():
    output, _ = run_command("winget upgrade --all")
    print(output)

def install_package(package_name):
    print(f"Installing {package_name}...")
    output, error = run_command(f"winget install {package_name} --silent")
    print(output)
    if error:
        print("Error:", error)
        log_action("INSTALL", package_name, "FAILED")
    else:
        log_action("INSTALL", package_name, "SUCCESS")

def uninstall_package(package_name):
    print(f"Uninstalling {package_name}...")
    output, error = run_command(f"winget uninstall {package_name}")
    print(output)
    if error:
        print("Error:", error)
        log_action("UNINSTALL", package_name, "FAILED")
    else:
        log_action("UNINSTALL", package_name, "SUCCESS")

def list_sources():
    output, _ = run_command("winget source list")
    print(output)

def add_source(name, url):
    output, error = run_command(f"winget source add -n {name} {url}")
    print(output)
    if error:
        print("Error:", error)

def remove_source(name):
    output, error = run_command(f"winget source remove {name}")
    print(output)
    if error:
        print("Error:", error)
