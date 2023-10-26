import requests
import json
import configparser

def load_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def translate_text(text, config):
    payload = {
        "text": text,
        "target_lang": config['settings']['target_language'],
        "auth_key": config['deepl']['api_key'],
    }
    response = requests.post(config['deepl']['api_url'], data=payload)

    try:
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

    translation = response.json()
    translated_text = translation['translations'][0]['text']
    print(f"Translated '{text}' to '{translated_text}'")

    return translated_text

def read_and_translate(file_path, output_file_path, config):
    try:
        with open(file_path, 'r', encoding='utf-8') as source_file, \
             open(output_file_path, 'w', encoding='utf-8') as translated_file:

            for line in source_file:
                stripped_line = line.strip()

                if not stripped_line or stripped_line.startswith(';') or stripped_line.startswith('#'):
                    translated_file.write(line)
                    continue

                if '=' in stripped_line:
                    key, value = stripped_line.split('=', 1)
                    translated_value = translate_text(value.strip(), config)

                    if translated_value:
                        translated_file.write(f"{key}={translated_value}\n")
                    else:
                        print(f"Error translating key '{key.strip()}'. Keeping original value.")
                        translated_file.write(line)
                else:
                    translated_file.write(line)

            print(f"Translation complete. '{output_file_path}' has been created.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    config = load_config()
    source_file_path = "./global.ini"
    translated_file_path = "./translated_global.ini"
    read_and_translate(source_file_path, translated_file_path, config)