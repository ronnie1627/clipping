"""
General helper utilities for Studio rendering workflow.
"""

import os


def format_seconds(seconds):
    """
    Format a duration in seconds into HH:MM:SS.

    Args:
        seconds: Numeric duration in seconds.

    Returns:
        Duration string in `HH:MM:SS` format, clamped to non-negative.
    """
    seconds = max(0, int(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def escape_ffmpeg_filter_value(value: str) -> str:
    """
    Escape a value so it is safe in FFmpeg filter expressions.

    Args:
        value: Raw value to place inside an FFmpeg filter string.

    Returns:
        Escaped value string for FFmpeg filter usage.
    """
    text = str(value)
    if os.name == "nt":
        # FFmpeg parses filter strings in two passes (graph, then options),
        # so the drive-letter colon needs a double escape on Windows.
        text = text.replace("\\", "/")
        return text.replace(":", r"\\:").replace("'", r"\\\'")
    return text.replace("\\", r"\\").replace(":", r"\:").replace("'", r"\'")
