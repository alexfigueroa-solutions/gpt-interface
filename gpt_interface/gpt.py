import argparse
import shutil
from scripts.prompt import run_prompt

def write_text_files(dir_translations):
    for translation in dir_translations:
        shutil.copyfile(translation["script_dir"], translation["output_dir"])

def create_command_list_text(commands):
    command_list_text = ''
    for command in commands:
        if command == commands[-1]:
            command_list_text += f" or '{command}'."
        else:
            command_list_text += f" '{command},'"
    return command_list_text

def default_function(args):
    print(f"No command provided. Please use {create_command_list_text(['prompt-code'])}")

def set_prompt_cli_parser(parser, subparsers):
    prompt_cli_parser = subparsers.add_parser(
        "prompt-code", help="Prompt chatgpt with any given prompt"
    )
    prompt_cli_parser.add_argument("input", type=str, help="The file containing the code to be modified by GPT")
    prompt_cli_parser.set_defaults(func=run_prompt)    

def main():
    parser = argparse.ArgumentParser(prog="gpt")
    subparsers = parser.add_subparsers()
    
    set_prompt_cli_parser(parser, subparsers)
    
    args = parser.parse_args()
    if 'func' in args:
        args.func(args.input)
    else:
        default_function(args)

if __name__ == "__main__":
    main()
