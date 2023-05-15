# file_writer.py
import shutil

def write_text_files(dir_translations):
    for translation in dir_translations:
        shutil.copyfile(translation["script_dir"], translation["output_dir"])

def main():
    prompt_translation = {
        "prompt": {
            "script_dir": "scripts/prompt.py",
            "output_dir": "text_files/prompt.txt"
        },
    }

    code_reader_translation = {
        "code_reader": {
            "script_dir": "scripts/code_reader.py",
            "output_dir": "text_files/code_reader.txt"
        },
    }

    gpt_translation = {
        "gpt": {
            "script_dir": "gpt.py",
            "output_dir": "text_files/gpt.txt"
        }
    }

    directory_translations = [
        prompt_translation,
        code_reader_translation,
        gpt_translation
    ]

    write_text_files(directory_translations)

if __name__ == "__main__":
    main()
