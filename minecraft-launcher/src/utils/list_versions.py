def list_versions(game_dir):
    import os
    versions = []
    versions_dir = os.path.join(game_dir, "versions")
    
    if os.path.exists(versions_dir):
        for version in os.listdir(versions_dir):
            if os.path.isdir(os.path.join(versions_dir, version)):
                versions.append(version)
    
    return versions