import typer
from typing_extensions import Annotated
import chess
import chess.pgn
from enum import Enum
from pathlib import Path

class Mode(str, Enum):
  REPEATED="REPEATED"
  UNIQUE="UNIQUE"

def annotator(
    input: Path = typer.Argument(..., exists=True, readable=True, help="Input file path"),
    output: Path = typer.Option(
        None, "--output", "-o", writable=True, help="Optional output file path"
    ),
    mode: Mode = typer.Option(
        Mode.UNIQUE, "--mode", help="Processing mode: REPEATED or UNIQUE"
    ),
):
  """
  Entry function called from Typer.
  """
  typer.echo(f"Mode: {mode}")
  typer.echo(f"Input file: {input}")

  if output:
    typer.echo(f"Output file: {output}")
  else:
    typer.echo("No output file given — editing in place.")
  
  try:
    scanner = PGNScanner(starting_moves=moves)
  except typer.BadParameter as e:
    typer.echo(f"{e}", err=True)
    return
  scanner.run()