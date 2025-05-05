import os
import uuid

def list_versions(game_dir):
    versions_path = os.path.join(game_dir, "versions")
    if not os.path.exists(versions_path):
        return []
    return sorted([f for f in os.listdir(versions_path) if os.path.isdir(os.path.join(versions_path, f))])

def get_uuid(username):
    # You can generate a consistent UUID from username
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, username))
import os
import uuid
import urllib.request
import subprocess

def list_versions(game_dir):
    versions_path = os.path.join(game_dir, "versions")
    if not os.path.exists(versions_path):
        return []
    return sorted([f for f in os.listdir(versions_path) if os.path.isdir(os.path.join(versions_path, f))])

def get_uuid(username):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, username))

def install_fabric(minecraft_version, game_dir):
    print("Downloading Fabric installer...")
    installer_url = "https://meta.fabricmc.net/v2/versions/installer"
    latest_installer = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.0/fabric-installer-1.0.0.jar"

    # Save location
    installer_path = os.path.join(game_dir, "fabric-installer.jar")

    # Download installer
    urllib.request.urlretrieve(latest_installer, installer_path)
    print("Installer downloaded!")

    # Run installer via Java
    cmd = [
        "java", "-jar", installer_path,
        "client",
        "-dir", game_dir,
        "-mcversion", minecraft_version
    ]

    print("Running Fabric installer...")
    subprocess.run(cmd)
    print("Fabric installed!")
