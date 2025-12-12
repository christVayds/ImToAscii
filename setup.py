from setuptools import setup, find_packages

setup(
    name='imtoascii',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "pillow"
    ],
    entry_points={
        'console_scripts': [
            'imtoascii=imtoascii.main:main'
        ]
    }
)
