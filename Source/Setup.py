from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but some modules need help.
build_exe_options = {
    "packages": ["os", "sys", "pandas", "numpy"],  # Add any other packages you use
    "excludes": [],
}

setup(
    name="DR64-PDF.Converter",
    version="0.1",
    description="A simple PDF converter for extracting text quickly",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "DR64-PDF.Converter.py",
            base=None,  # Use "Win32GUI" if your script is a GUI application
            icon=r"C:\Users\danre\OneDrive\Desktop\DR64\OPEN SOURCE\DR64 - PDF Converter\Source\Icon\DR64-PDF.Converter.ico"  # Path to your icon file
        )
    ]
)
