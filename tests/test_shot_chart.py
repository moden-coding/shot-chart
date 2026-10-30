import numbers
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except ImportError:
    raise ImportError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the Anaconda (conda) interpreter in VS Code: Ctrl/Cmd+Shift+P → "
        "'Python: Select Interpreter' → pick the one that says 'anaconda3'."
    ) from None

from src.shot_chart import points_by_player, best_shooter, longest_shooter

DATA_PATH = REPO_ROOT / "data" / "shot_logs.csv"

COLUMNS = ["player_name", "FGM", "PTS", "SHOT_DIST"]

practice = pd.DataFrame([
    ["amy", 1, 2, 10], ["amy", 1, 2, 12], ["amy", 1, 3, 24], ["amy", 0, 0, 25], ["amy", 0, 0, 8],
    ["ben", 1, 3, 23], ["ben", 1, 3, 24], ["ben", 0, 0, 23],
    ["cal", 1, 2, 2],  ["cal", 1, 2, 3],
    ["dee", 1, 2, 5],  ["dee", 1, 2, 6],  ["dee", 1, 2, 4],  ["dee", 1, 2, 7], ["dee", 0, 0, 30], ["dee", 0, 0, 9],
], columns=COLUMNS)

RETURNED_NONE = "Function returned None. Did you replace `return None`?"
POINTS_ORDER = ("Should be the total (.sum()) PTS for each player, biggest first. "
                "Did you sort with ascending=False? Did you use .sum(), not .mean()?")
PLAYER_COUNT = "There should be one entry for each player."
BEST_SHOOTER = "That's the most shots made. The question asks for the highest share of shots made."
LONGEST = "The question asks for the farthest average shot."


def run(function, df):
    """Call a student function. If it crashes, return the error as text so the test fails with a message."""
    try:
        return function(df)
    except Exception as error:
        return type(error).__name__ + ": " + str(error)


class ShotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(DATA_PATH)

    def check_not_none(self, result):
        if result is None:
            self.fail(RETURNED_NONE)

    def check_series(self, result):
        self.check_not_none(result)
        if not isinstance(result, pd.Series):
            self.fail("Should return a Series. Got: " + repr(result)[:200])

    def check_number(self, result, expected, msg):
        if not isinstance(result, numbers.Real):
            self.fail(repr(result) + " is not a number : " + msg)
        self.assertAlmostEqual(result, expected, places=2, msg=msg)


class TestPointsByPlayer(ShotTestCase):
    def test_real_data(self):
        result = run(points_by_player, self.df.copy())
        self.check_series(result)
        self.assertEqual(len(result), 281, msg=PLAYER_COUNT)
        self.assertEqual(list(result.index[:3]), ["stephen curry", "james harden", "klay thompson"],
                         msg=POINTS_ORDER)
        for value, expected in zip(result.iloc[:3], [1130, 1103, 1075]):
            self.check_number(value, expected, POINTS_ORDER)

    def test_practice_table(self):
        result = run(points_by_player, practice.copy())
        self.check_series(result)
        self.assertEqual(list(result.index), ["dee", "amy", "ben", "cal"], msg=POINTS_ORDER)
        for value, expected in zip(result, [8, 7, 6, 4]):
            self.check_number(value, expected, POINTS_ORDER)


class TestBestShooter(ShotTestCase):
    def test_real_data(self):
        result = run(best_shooter, self.df.copy())
        self.check_not_none(result)
        self.assertEqual(result, "deandre jordan", msg=BEST_SHOOTER)

    def test_practice_table(self):
        result = run(best_shooter, practice.copy())
        self.check_not_none(result)
        self.assertEqual(result, "cal", msg=BEST_SHOOTER)


class TestLongestShooter(ShotTestCase):
    def test_real_data(self):
        result = run(longest_shooter, self.df.copy())
        self.check_not_none(result)
        self.assertEqual(result, "mike miller", msg=LONGEST)

    def test_practice_table(self):
        result = run(longest_shooter, practice.copy())
        self.check_not_none(result)
        self.assertEqual(result, "ben", msg=LONGEST)


if __name__ == "__main__":
    unittest.main()
