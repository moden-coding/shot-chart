# Exercise 33: Shot Chart

Use `groupby` to compare players in a table of every shot from the 2014–15 NBA regular season (`data/shot_logs.csv`).

## Research questions

| # | Research question | Function | Returns | Look back at |
|---|---|---|---|---|
| 1 | How many points did each player score on these shots? Biggest first. | `points_by_player(df)` | a Series | Part 4 |
| 2 | Which player made the highest share of his shots? (`FGM` is 1 for a make and 0 for a miss.) | `best_shooter(df)` | a name | Part 4 |
| 3 | Which player's average shot came from the farthest away? | `longest_shooter(df)` | a name | Part 4 |

## How to run

- See your findings: run `src/shot_chart.py` (or `python src/shot_chart.py` in the terminal).
- Run the tests from the Testing panel (beaker icon), or with `python -m unittest discover` in the terminal.

## If tests won't run

- Select the Anaconda (conda) interpreter: Ctrl/Cmd+Shift+P → "Python: Select Interpreter".
- If you have the old **Python Test Explorer** extension, uninstall it (`code --uninstall-extension littlefoxteam.vscode-python-test-adapter`). It ignores your interpreter.
- `pip install -r requirements.txt` if pandas is missing.
