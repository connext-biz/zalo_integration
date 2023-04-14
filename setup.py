from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='zalo_sdk',
    version='0.1.0',
    description='Zalo SDK'
    long_description=readme,
    author='Khoa Tran',
    author_email='khoa@connext.biz'
    url='https://github.com/connext_biz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
