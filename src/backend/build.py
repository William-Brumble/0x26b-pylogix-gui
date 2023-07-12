import os
import sys

app_name = 'PlaceholderName'
venv_path = '../venv/Lib/site-packages'
frontend_path = './frontend/dist'
dist_path = './build/dist'
build_path = './build/build'
spec_path = './build/spec'

frontend_html = os.path.join(os.getcwd(), "dist", "index.html") +";./dist/"
vite_svg = os.path.join(os.getcwd(), "dist", "vite.svg") +";./dist/"
frontend_assets = os.path.join(os.getcwd(), "dist", "assets", "*") +";./dist/assets"

os.system(
    f'pyinstaller ' +
    f'--windowed ' +
    f'--clean ' +
    f'--name "{app_name}" ' +
    f'--paths "{venv_path}" ' +
    f'--distpath "{dist_path}" ' +
    f'--workpath "{build_path}" ' +
    f'--specpath "{spec_path}" ' +
    f'--add-data "{frontend_html}" ' +
    f'--add-data "{vite_svg}" ' +
    f'--add-data "{frontend_assets}" ' +
    f'main.py'
)
