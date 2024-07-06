from py2exe import freeze

freeze(
    # console=["main.py"],
    windows=[{
        "script": "main.py",
        "icon_resources": [(1, "icon.ico")],
        "dest_base": "Wazzapp"
        }],
    data_files=None,
    zipfile="library.zip",
    options={"py2exe": {"bundle_files": 1, "compressed": True}},
    version_info={"version": "1.0.0", "copyright": "Itai Shek", "product_name": "Wazzapp", "description": "Fix WhatsApp jpeg images for Photoshop"}
)


# PyInstaller exe is flagged as a virus after installation with windows msi,
# therefore I created the msi version with py2exe.