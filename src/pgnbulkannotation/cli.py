import typer

from .pgnbulkannotation import annotator


app = typer.Typer()
app.command()(annotator)


if __name__ == "__main__":
  app()