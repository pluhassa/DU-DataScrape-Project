"""Unit tests for the command-line interface in main.py."""

from pathlib import Path
import io
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import main  # pylint: disable=wrong-import-position,import-error


class TestMain(unittest.TestCase):
    """Test cases for argument parsing and output behavior."""

    def run_main_with_args(self, args):
        """Run main.main() with fake CLI args and return captured stdout."""
        fake_argv = ["main.py", *args]
        captured = io.StringIO()

        with patch.object(sys, "argv", fake_argv):
            with redirect_stdout(captured):
                main.main()
        return captured.getvalue()

    def test_defaults(self):
        """Use defaults when no arguments are supplied."""
        output = self.run_main_with_args([])
        self.assertIn("Logging level set to: INFO", output)
        self.assertIn("Selected platform: None", output)
        self.assertIn("Hello, World!", output)

    def test_all_arguments(self):
        """Accept all supported arguments and print the expected values."""
        output = self.run_main_with_args(
            [
                "--log-level",
                "DEBUG",
                "--platform",
                "X",
                "--file-path",
                "input.txt",
            ]
        )
        self.assertIn("Logging level set to: DEBUG", output)
        self.assertIn("Selected platform: X", output)
        self.assertIn("Input file path: input.txt", output)
        self.assertIn("Hello, World!", output)

    def test_invalid_log_level(self):
        """Raise SystemExit when log level is not one of the allowed choices."""
        with self.assertRaises(SystemExit):
            self.run_main_with_args(["--log-level", "INVALID"])

    def test_invalid_platform(self):
        """Raise SystemExit when platform is not one of the allowed choices."""
        with self.assertRaises(SystemExit):
            self.run_main_with_args(["--platform", "Vine"])


if __name__ == "__main__":
    unittest.main()
