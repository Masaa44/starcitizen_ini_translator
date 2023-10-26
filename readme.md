# Star Citizen INI File Translator

This script is specifically designed for fans and players of Star Citizen! It utilizes the DeepL API to automatically translate the `global.ini` file used in Star Citizen, aiding in the localization of the game's extensive configurations and content.

**Note:** The free version of the DeepL API supports only 500,000 words per month, which may not be sufficient to translate the entire `global.ini` file in one go. Users with higher translation needs might need to consider subscribing to a paid DeepL plan.

## Prerequisites

- Python 3.6 or higher must be installed on your local machine.
- A DeepL account with an API key. You can obtain an API key by signing up on [DeepL's website](https://www.deepl.com/fr/pro-api).

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/sc-translator/starcitizen_ini_translator
    ```


2. Navigate to the cloned project directory:

    ```
    cd starcitizen_ini_translator
    ```

4. Install the necessary dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Copy the provided `config.ini.example` file in the same directory and rename the copy to `config.ini`:

    ```
    cp config.ini.example config.ini  # On Windows, use `copy config.ini.example config.ini`
    ```

6. Open the `config.ini` file and replace the default values with your personal configurations, such as your DeepL API key.

## Usage

After following the installation steps, you can run the script using the following command:
```
python main.py
```
