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
