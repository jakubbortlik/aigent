import os

from common.errors import format_error


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        full_dir = os.path.join(working_directory, directory)
    except Exception:
        return format_error(
            f"Cannot concatenate full_dir from {working_directory=} and {directory=}"
        )

    if not full_dir.startswith(working_directory):
        return format_error(
            f"Cannot list '{directory}' as it is outside the permitted working directory"
        )

    try:
        if not os.path.isdir(full_dir):
            return format_error(f"'{directory}' is not a directory")
    except Exception:
        return format_error(f"Cannot determine if '{full_dir=}' is a directory")

    result = []
    try:
        dir_contents = os.listdir(full_dir)
    except Exception:
        return format_error(f"Cannot list contents of directory '{full_dir=}'")

    for file in dir_contents:
        try:
            full_path = os.path.join(full_dir, file)
        except Exception:
            return format_error(f"Cannot join path of '{full_dir}' and '{file}'")

        try:
            file_size = os.path.getsize(full_path)
        except Exception:
            return format_error(f"Cannot get size of '{full_path}'")

        try:
            is_dir = os.path.isdir(full_path)
        except Exception:
            return format_error(f"Cannot determine if '{full_path=}' is a directory")

        result.append(f" - {file}: {file_size=} bytes, {is_dir=}")

    return "\n".join(result)
