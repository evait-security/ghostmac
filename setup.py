from setuptools import setup, find_packages

setup(
    name='ghostmac',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scapy',
    ],
    entry_points={
        'console_scripts': [
            'ghostmac=ghostmac.main:main',
        ],
    },
    description='GhostMAC: A tool to brute force DHCP by sending DISCOVER packets with random MAC addresses',
    author='FLX',
    author_email='flx@evait.de',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/evait-security/ghostmac',
)
