def get_uuid(username):
    import requests

    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("id")
    else:
        raise ValueError("Username not found or invalid")