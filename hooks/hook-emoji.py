from PyInstaller.utils.hooks import collect_data_files

# Collect data files from the emoji library
datas = collect_data_files('emoji')
