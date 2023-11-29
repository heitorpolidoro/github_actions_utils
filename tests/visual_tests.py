import sys
from github_actions_utils.log import debug, notice, warning, error

sys.path.append('.')

file = "tests/visual_tests.py"

debug("This is a debug")

notice_start_line = 10
notice("This is a notice")
notice("This is a file notice with title", title="Nice Title", file=file)

warning_start_line = 10
warning("This is a warning")
warning("This is a file warning with title", title="Nice Title", file=file)

error_start_line = 10
error("This is a error")
error("This is a file error with title", title="Nice Title", file=file)
