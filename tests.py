from functions.get_files_info import get_files_info

print("Result for curent directory")
print(get_files_info("calculator", "."))

print("Result for 'pkg' directory")
print(get_files_info("calculator", "pkg"))

print("Result for '/bin' directory")
print(get_files_info("calculator", "/bin"))
