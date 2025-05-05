def install_fabric(mc_version, game_dir):
    import os
    import requests
    import json

    fabric_url = f"https://meta.fabricmc.net/v2/versions/loader/{mc_version}/latest"
    response = requests.get(fabric_url)

    if response.status_code != 200:
        print(f"Failed to fetch Fabric version for Minecraft {mc_version}.")
        return

    fabric_info = response.json()
    loader_version = fabric_info['loader']['version']
    installer_url = fabric_info['loader']['downloads']['installer']['url']

    print(f"Installing Fabric Modloader {loader_version} for Minecraft {mc_version}...")

    installer_response = requests.get(installer_url)

    if installer_response.status_code == 200:
        installer_path = os.path.join(game_dir, "fabric-installer.jar")
        with open(installer_path, 'wb') as installer_file:
            installer_file.write(installer_response.content)
        print(f"Fabric installer downloaded to {installer_path}.")
    else:
        print("Failed to download the Fabric installer.")