import os
from setuptools import setup
from glob import glob


README_PATH = 'README.rst'
LONG_DESC = ''
if os.path.exists(README_PATH):
    with open(README_PATH) as readme:
        LONG_DESC = readme.read()

INSTALL_REQUIRES = ['Pillow']
PACKAGE_NAME = 'pytesseract_bundled4'
PACKAGE_DIR = 'src'

if not os.path.exists('src/tesseract_built'):
    raise Exception("This is meant to be a self contained package and cannot be built without the tesseract_built directory")

setup(
    name=PACKAGE_NAME,
    version='0.2.8',
    author='Samuel Hoffstaetter',
    author_email='samuel@hoffstaetter.com',
    maintainer='Matthias Lee',
    maintainer_email='pytesseract@madmaze.net',
    description=(
        "Python-tesseract is a python wrapper for Google's Tesseract-OCR"
    ),
    long_description=LONG_DESC,
    license='GPLv3',
    keywords='python-tesseract OCR Python',
    url='https://github.com/madmaze/python-tesseract',
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: PACKAGE_DIR},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': ['{0} = {0}.{0}:main'.format(PACKAGE_NAME)]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
