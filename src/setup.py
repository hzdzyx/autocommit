from setuptools import setup

setup(
    name='autocommit',
    version='0.1',
    py_modules=['gpt','prompt','git','apikey'],
    entry_points={
        'console_scripts': [
            'autocommit = gpt:main',
        ],
    },
)