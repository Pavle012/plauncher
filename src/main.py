from utils import list_versions, get_uuid, install_fabric
from launcher import launch_minecraft
import os

DEFAULT_GAME_DIR = os.path.expanduser("~/.minecraft")

def main():
    print("== Minecraft Launcher ==")
    print("1. Launch Minecraft")
    print("2. Install Fabric Modloader")
    choice = input("Choose an option (1 or 2): ")

    if choice == "2":
        mc_version = input("Enter Minecraft version to install Fabric for (e.g. 1.20.1): ")
        install_fabric(mc_version, DEFAULT_GAME_DIR)
        return

    versions = list_versions(DEFAULT_GAME_DIR)
    print("\nAvailable versions:")
    for i, v in enumerate(versions):
        print(f"[{i}] {v}")

    version_idx = int(input("\nSelect version index: "))
    version = versions[version_idx]

    username = input("Enter username: ")
    ram = input("Max RAM (e.g. 2G): ").upper()
    custom_dir = input(f"Game directory (default: {DEFAULT_GAME_DIR}): ").strip()
    game_dir = custom_dir if custom_dir else DEFAULT_GAME_DIR

    uuid = get_uuid(username)
    launch_minecraft(version, username, uuid, game_dir, ram)

if __name__ == "__main__":
    main()