from setuptools import setup

setup(
    name='gammactl',
    version='0.1.0',
    py_modules=['gammactl'],
    install_requires=[
        'Click',
		'pydbus',
        'PyGObject'
    ],
    entry_points={
        'console_scripts': [
            'gammactl = gammactl:cli',
        ],
    },
)
