import sys

sys.path.append('.')
from github_actions_utils.log import debug, notice, warning, error

file = "tests/visual_tests.py"

debug("This is a debug")

notice_start_line = 10
notice("This is just a notice")
notice("This is a notice with title and file", title="Nice Title", file=file)
notice("This is a notice with line", line=notice_start_line + 3, file=file)
notice(
    "This is a notice with line and endLine",
    line=notice_start_line + 4,
    end_line=notice_start_line + 9,
    file=file
)
notice("This is a notice with col", line=notice_start_line + 10, col=2, file=file)
notice("This is a notice with col and endColumn", line=notice_start_line + 11, col=2, end_column=5, file=file)

warning_start_line = 10
warning("This is just a warning")
warning("This is a warning with title and file", title="Nice Title", file=file)
warning("This is a warning with line", line=warning_start_line + 3, file=file)
warning(
    "This is a warning with line and endLine",
    line=warning_start_line + 4,
    end_line=warning_start_line + 9,
    file=file
)
warning("This is a warning with col", line=warning_start_line + 10, col=2, file=file)
warning("This is a warning with col and endColumn", line=warning_start_line + 11, col=2, end_column=5, file=file)

error_start_line = 10
error("This is just a error")
error("This is a error with title and file", title="Nice Title", file=file)
error("This is a error with line", line=error_start_line + 3, file=file)
error(
    "This is a error with line and endLine",
    line=error_start_line + 4,
    end_line=error_start_line + 9,
    file=file
)
error("This is a error with col", line=error_start_line + 10, col=2, file=file)
error("This is a error with col and endColumn", line=error_start_line + 11, col=2, end_column=5, file=file)
