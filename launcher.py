import subprocess
import os

def launch_minecraft(version, username, uuid, game_dir, ram):
    version_dir = os.path.join(game_dir, "versions", version)
    jar_path = os.path.join(version_dir, f"{version}.jar")

    classpath = f"{version_dir}/{version}.jar"
    main_class = "net.minecraft.client.main.Main"

    print("\nLaunching Minecraft...")
    cmd = [
        "java", f"-Xmx{ram}",
        "-cp", classpath,
        main_class,
        "--username", username,
        "--version", version,
        "--gameDir", game_dir,
        "--assetsDir", os.path.join(game_dir, "assets"),
        "--assetIndex", version.split('.')[0],
        "--uuid", uuid,
        "--accessToken", "0",
        "--userType", "legacy"
    ]

    subprocess.run(cmd)
