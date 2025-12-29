import typer
import json
import os

app = typer.Typer()

@app.command()
def add_data_to_file(data: str):
    """
    Append a JSON argument to a local file.
    """
    try:
        parsed = json.loads(data)

    except json.JSONDecodeError:
        typer.echo("Invalid JSON")
        raise typer.Exit(code = 1)
    
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(json.dumps(parsed))
        file.write("\n")

    typer.echo("Data added successfully")

@app.command()
def return_last_ten_lines():
    """
    Return the last 10 stored JSON arguments.
    """

    if not os.path.exists("data.txt"):
        typer.echo("No data found")
        raise typer.Exit()
    
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    last_lines = lines[-10:]

    for line in last_lines:
        typer.echo(line.strip())

if __name__ == "__main__":
    app()
    
