import os

app_name = '"PlaceholderName"'
venv_path = '"../venv/Lib/site-packages"'
frontend_path = '"./frontend/dist"'
dist_path = '"./build/dist"'
build_path = '"./build/build"'
spec_path = '"./build/spec"'

data_root_path = os.getcwd() + "/frontend/dist"
html_path = data_root_path + "/index.html:../frontend/dist"
vite_svg_path = data_root_path + "/vite.svg:../frontend/dist"
javascript_path = data_root_path + "/assets/*.js:../frontend/dist/assets"
css_path = data_root_path + "/assets/*.css:../frontend/dist/assets"


os.system(
    f'pyinstaller ' +
    f'--onefile ' + 
    f'--clean ' +
    f'--name {app_name} ' +
    f'--paths {venv_path} ' +
    f'--distpath {dist_path} ' +
    f'--workpath {build_path} ' +
    f'--specpath {spec_path} ' +
    f'--add-data {html_path} ' +
    f'--add-data {vite_svg_path} ' +
    f'--add-data {javascript_path} ' +
    f'--add-data {css_path} ' +
    f'./backend/main.py'
)
