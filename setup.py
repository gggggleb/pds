from setuptools import setup
setup(
    name='pds',
    version='2.3',
    description='Pds server',
    url='https://git.glebmail.xyz/PythonPrograms/pds',
    author='gleb',
    packages=['pds'],
    author_email='gleb@glebmail.xyz',
    license='GNU GPL 3',
    scripts=['bin/pds'],
    install_requires=[
        'pyyaml',
    ],
)
