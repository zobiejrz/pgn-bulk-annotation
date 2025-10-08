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
  
  with open(input, "r", encoding="utf-8") as f:
    games = []
    while True:
      game = chess.pgn.read_game(f)
      if game is None:
        break
      games.append(game)
  
  typer.echo(f"Loaded {len(games)} games")
  annotations: dict[str, str] = {}

  for i, game in enumerate(games, start=1):
    typer.echo(f"\n=== Game {i}/{len(games)} ===")
    board = game.board()
    for node in game.mainline():
      move = node.move
      key = f"{board.fen()}|{move.uci()}"

      if mode == Mode.REPEATED and key in annotations:
          node.comment = annotations[key]
          typer.echo(f"Reusing annotation for {key}")
      else:
        typer.echo(f"\nPosition:\n{board}")
        typer.echo(f"Move: {board.san(move)}")
        note = typer.prompt("Enter annotation")
        annotations[key] = note
        node.comment = note

      board.push(move)
  
  target = output or input
  with open(target, "w", encoding="utf-8") as out:
    for game in games:
      print(game, file=out)
  typer.echo("Processing complete.")