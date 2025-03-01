import re

def remove_ansi(text):
    """Removes ANSI escape sequences from a given text."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text).strip()

def format_progress_bar(filename, percentage, done, total_size, status, eta, speed, elapsed, user_mention, user_id):
    """Formats a progress bar for downloads."""
    bar_length = 10
    
    # Clean and convert percentage
    percentage = float(remove_ansi(str(percentage)).replace("%", "").strip())

    filled_length = int(bar_length * percentage / 100.0)
    bar = '★' * filled_length + '☆' * (bar_length - filled_length)

    def format_size(size):
        """Formats file size in a human-readable format."""
        if size is None or size == 0:
            return "0 B"
        size = int(size)
        if size < 1024:
            return f"{size} B"
        elif size < 1024 ** 2:
            return f"{size / 1024:.2f} KB"
        elif size < 1024 ** 3:
            return f"{size / 1024 ** 2:.2f} MB"
        else:
            return f"{size / 1024 ** 3:.2f} GB"

    def format_time(seconds):
        """Formats time in a human-readable format."""
        if seconds is None or seconds <= 0:
            return "N/A"
        seconds = int(seconds)
        if seconds < 60:
            return f"{seconds} sec"
        elif seconds < 3600:
            return f"{seconds // 60} min"
        else:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours} hr {minutes} min"

    return (
        f"┏ ғɪʟᴇɴᴀᴍᴇ: {filename}\n"
        f"┠ [{bar}] {percentage:.2f}%\n"
        f"┠ ᴘʀᴏᴄᴇssᴇᴅ: {format_size(done)} ᴏғ {format_size(total_size)}\n"
        f"┠ sᴛᴀᴛᴜs: {status}\n"
        f"┠ sᴘᴇᴇᴅ: {format_size(speed)}/s\n"
        f"┠ ᴇᴛᴀ: {format_time(eta)}\n"
        f"┖ ᴜsᴇʀ: {user_mention} | ɪᴅ: {user_id}"
    )
