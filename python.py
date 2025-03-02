import os
import subprocess
import sys
import urllib.request

def download_roblox_installer():
    url = 'https://setup.roblox.com/RobloxPlayerLauncher.exe'
    installer_path = 'RobloxPlayerLauncher.exe'
    urllib.request.urlretrieve(url, installer_path)
    return installer_path

def install_roblox(installer_path):
    subprocess.run([installer_path, '/silent', '/install'], check=True)

def main():
    try:
        installer_path = download_roblox_installer()
        install_roblox(installer_path)
        print("Roblox installation successful.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(installer_path):
            os.remove(installer_path)

if __name__ == '__main__':
    main()
