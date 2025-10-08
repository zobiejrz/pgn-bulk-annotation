# pgn-bulk-annotation

This is a CLI tool that assists with annotating PGN databases quickly. It loops through each move and allows for an annotation to be applied, or can automatically apply previous annotations to the same move from different games.

## Installation

**1. Clone the repository**

**2. Install dependencies (inside a virtual environment is recommended):**

```bash
pip install -r requirements.txt
```

- Requires Python 3.12+

## Usage

Run the CLI:

```bash
python -m pgnscanner.cli /path/to/file [--output path] [--mode <REPEATED/UNIQUE>]
```

This starts an interactive REPL loop for the specied input file.

Optionally, an output file may be given using `--output` or `-o`. If no output file is specified, the input file is overwritten.

Additionally, the mode may be set with `--mode REPEATED` or `--mode UNIQUE` (or using `-m`). In `REPEATED` mode, annotations will be automatically applied for the same moves across games. In `UNIQUE` mode you will be prompted for every annotation.

Commands available during the prompt loop are prefixed using a `!`.

## REPL Commands

|        Command         |  Description  |
| :--------------------: | :------------ |
|         `!skip`        | Will skip prompting for the rest of the moves in the current game. |
