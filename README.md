# Minecraft Launcher

This project is a simple command-line interface for launching Minecraft and installing the Fabric Modloader. It is designed to provide an easy way for users to manage their Minecraft installations.

## Features

- Launch Minecraft with a specified version and username.
- Install the Fabric Modloader for different Minecraft versions.
- List available Minecraft versions from the specified game directory.

## Project Structure

```
minecraft-launcher
├── src
│   ├── main.py               # Entry point for the launcher application
│   ├── launcher
│   │   └── __init__.py       # Initialization for the launcher module
│   ├── utils
│   │   ├── __init__.py       # Initialization for the utils module
│   │   ├── list_versions.py   # Function to list available Minecraft versions
│   │   ├── get_uuid.py       # Function to get UUID for a Minecraft username
│   │   └── install_fabric.py  # Function to install Fabric Modloader
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd minecraft-launcher
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the launcher, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to either launch Minecraft or install the Fabric Modloader.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.