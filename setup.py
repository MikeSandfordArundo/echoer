
#!/usr/bin/env python

from distutils.core import setup

setup(name='Echoer',
    version='1.3',
    description='Say things out loud',
    author='Mike Sandford',
    author_email='mike.sandford@arundo.com',
    url='https://github.com/MikeSandfordArundo/echoer.git',
    packages=['echoer'],
    entry_points={
        'console_scripts': [
            'echoer=echoer.start:main',
        ],
    },
    )
