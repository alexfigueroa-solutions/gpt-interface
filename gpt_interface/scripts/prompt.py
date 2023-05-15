import typer
import openai
from rich.console import Console
from rich.syntax import Syntax
from rich.progress import track
from time import sleep

app = typer.Typer()

def prompt_gpt(code):
    console = Console()

    prompt = "Write your response in markdown. Explain ways that I can extend the functionality of this system and what I can do to improve the ux and developer experience. Rewrite the file. Dont use a progress bar:  " + code

    openai.api_key = "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"

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=messages
    )

    # We'll use the rich library to print the response with syntax highlighting
    syntax = Syntax(response['choices'][0]['message']['content'], "python", theme="monokai", line_numbers=True)
    console.print(syntax)

@app.command()
def run_prompt(input_file: str):
    with open(input_file, 'r') as file:
        code = file.read()

    # Indicate the code generation process
    with Console().status("[bold green] Fetching responses from GPT API ...") as status:
        prompt_gpt(code)
        status.update("[bold green]Template generation complete!")


if __name__ == "__main__":
    app()
