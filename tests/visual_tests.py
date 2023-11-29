from github_actions_utils.log import debug, notice

debug("This is a debug")
notice("This is just a notice")
notice("This is a notice with title and file", title="Nice Title", file="log.py")
notice("This is a notice with line", line=2)
notice("This is a notice with line and endLine", line=2, end_line=4)
notice("This is a notice with col", line=1, col=2)
notice("This is a notice with col and endCol", line=4, end_line=5)
notice("This is a notice with col and endCol", line=4, col=2, end_col=5)
