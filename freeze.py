from py2exe import freeze
import os

#delete the old build drive
os.system("rmdir /s /q dist")

icon_path = r".\icon.ico"
script_path = r".\split-cost-tk.py"

freeze(
    windows=[{
        'script': 'split-cost-tk.py',
        'dest_base': 'split-cost',
        'bitmap_resources': [(1, icon_path)],
        'icon_resources': [(1, icon_path)],
    }],
    data_files=[('.', [icon_path, script_path])],
    options={
        'includes': ['tkinter'],
        'bundle_files': 1,
        'compressed': 1,
        'dll_excludes': ['libcrypto-1_1.dll', 'libffi-8.dll', 'libssl-1_1.dll'],
    },
    version_info={
        'version': '0.1',
        'copyright': 'Dan Spencer - 2023',
        'product_name': 'Split Cost',
    }
)
