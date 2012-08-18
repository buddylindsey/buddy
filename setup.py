from distutils.core import setup

setup(
    name='buddy',
    description='Helpers and Utilities for Django',
    version='0.1',
    packages=['buddy'],
    author='Buddy Lindsey',
    author_email='percent20@gmail.com',
    url='https://github.com/buddylindsey/buddy',
    license=open("LICENSE").read(),
    install_requires=['boto==2.5.2','geopy'],
    package_data={'buddy': ['static/browserid/*.js']},
)
