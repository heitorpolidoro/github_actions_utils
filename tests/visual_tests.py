import sys
from github_actions_utils.log import debug, notice, warning, error

sys.path.append('.')

file = "tests/visual_tests.py"

debug("This is a debug")

notice_start_line = 10
notice("This is just a notice")
notice("This is a notice with", title="Nice Title", file=file)

warning_start_line = 10
warning("This is just a warning")
warning("This is a warning with", title="Nice Title", file=file)

error_start_line = 10
error("This is just a error")
error("This is a error with", title="Nice Title", file=file)
