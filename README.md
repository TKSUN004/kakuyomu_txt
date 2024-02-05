# Kakuyomu Text Downloader

The `kakuyomu_txt` script allows you to download content from [Kakuyomu](https://kakuyomu.jp/) as `.txt` files using the Firefox browser. It leverages Selenium for web scraping, navigating through pages and dynamically loading content before saving it as text.

## Installation Requirements

Before running the script, ensure you have the following installed:

- **Python 3**: The script is written for Python 3. Ensure it's installed on your system.
- **Selenium**: A powerful tool for controlling web browsers through programs and performing browser automation.
- **Geckodriver**: A proxy for using W3C WebDriver-compatible clients to interact with Gecko-based browsers (e.g., Firefox).
- **Firefox**: The web browser used by the script for scraping content.

### Installing Dependencies

1. **Selenium**: Install Selenium using pip:

```pip install selenium```


Then, install Geckodriver. On macOS, you can use Homebrew:

```brew install geckodriver```


### Running the Script

To run the script, navigate to the directory containing it and execute the following command:

```python3 kakuyomu_txt.py https://kakuyomu.jp/works/XXXXXXXXXXXXXXXXXX```

Replace `XXXXXXXXXXXXXXXXXX` with the actual work ID from Kakuyomu.

