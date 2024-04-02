"""
Información de instalación
"""
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Recoger la descripción larga del archivo README
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Obtener la información del paquete
info_paquete = {}
with open(path.join('src', 'idealista', 'info_paquete.py')) as fp:
    exec(fp.read(), info_paquete)
# Uso: info_paquete['__version__']

setup(
    name=info_paquete['__name__'],
    version=info_paquete['__version__'],
    description=info_paquete['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jaime S.',
    author_email='_',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy',
        'deepdiff',
        'toml',
        'Pillow',
        'rich',
        'xlrd',
        'toml>=0.10.2'
    ],
    package_data={
        'idealista': ['data/*.toml']
    },

    entry_points={'console_scripts': [
        'idealista=idealista.main:main'
    ],
    },
)
