import os

from common.errors import format_error
from config import MAX_CHARACTER_COUNT


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)

        if not full_path.startswith(working_directory):
            return format_error(
                f"Cannot read '{file_path}' as it is outside the permitted working directory"
            )

        if not os.path.isfile(full_path):
            return format_error(
                f"File not found or is not a regular file: '{file_path}'"
            )

        with open(full_path) as file:
            contents = file.read()
            if len(contents) > MAX_CHARACTER_COUNT:
                truncated = contents[:MAX_CHARACTER_COUNT]
                return f'{truncated}[...File "{file_path}" truncated at 10000 characters]'
            return contents

    except Exception as e:
        return format_error(f"Reading '{file_path=}' failed: {e}")
