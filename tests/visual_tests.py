from github_actions_utils.log import debug, notice, warning, error, group, mask

file = "tests/visual_tests.py"

debug("This is a debug")

notice("This is a notice")
notice("This is a file notice with title", title="Nice Title", file=file)

warning("This is a warning")
warning("This is a file warning with title", title="Nice Title", file=file)

error("This is a error")
error("This is a file error with title", title="Nice Title", file=file)

with group("Group title"):
    print("logs inside group")


mask("This is a mask")
print("This is a mask with title")
