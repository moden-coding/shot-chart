import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "shot_logs.csv"


def points_by_player(df):
    """Return the total PTS for each player, biggest first."""
    return None


def best_shooter(df):
    """Return the player who made the highest share of his shots."""
    return None


def longest_shooter(df):
    """Return the player whose average shot came from the farthest away."""
    return None


def main():
    df = pd.read_csv(DATA_PATH)
    print("Points by player:")
    print(points_by_player(df))
    print()
    print("Best shooter:", best_shooter(df))
    print("Farthest average shot:", longest_shooter(df))


if __name__ == "__main__":
    main()
