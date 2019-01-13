from setuptools import setup


with open('LICENSE') as f:
    license = f.read()

setup(
    name='pytuya',
    version='0.0.2',
    description='Pytuya with persistent connections',
    author='Glen Takahashi',
    author_email='',
    url='https://github.com/glentakahashi/python-tuya-experimental',
    license=license,
    packages=['pytuya'],
    package_dir={'pytuya': 'pytuya'}
)
