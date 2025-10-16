from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("Result for curent directory")
print(get_files_info("calculator", "."))

print("Result for 'pkg' directory")
print(get_files_info("calculator", "pkg"))

print("Result for '/bin' directory")
print(get_files_info("calculator", "/bin"))

# Test getting file contents
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))  # (this should return an error string)
print(get_file_content("calculator", "pkg/does_not_exist.py")) # (this should return an error string)
