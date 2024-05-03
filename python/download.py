import urllib.request
import os

def download_chrome():
    # URL of the Google Chrome RPM file for Fedora
    chrome_rpm_url = 'https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm'

    # Destination directory where the RPM file will be saved (current directory)
    destination_directory = os.path.dirname(os.path.abspath(__file__))

    # Full path to the destination RPM file to be downloaded
    destination_path = os.path.join(destination_directory, 'google-chrome.rpm')

    try:
        # Download the Google Chrome RPM file
        print(f"Downloading Google Chrome to {destination_path}...")
        urllib.request.urlretrieve(chrome_rpm_url, destination_path)
        print("Download completed.")

        return destination_path  # Return the full path of the downloaded file
    except Exception as e:
        print(f"Error downloading Google Chrome: {e}")
        return None

# Main function to download and install Google Chrome
def main():
    # Perform the download of Google Chrome
    rpm_file = download_chrome()

    if rpm_file:
        # Install Google Chrome using dnf package manager (replace with your package manager if different)
        try:
            print("Installing Google Chrome...")
            os.system(f"sudo dnf install -y {rpm_file}")
            print("Google Chrome installed successfully.")
        except Exception as e:
            print(f"Error installing Google Chrome: {e}")
    else:
        print("Failed to download Google Chrome. Check logs for details.")

if __name__ == "__main__":
    main()
