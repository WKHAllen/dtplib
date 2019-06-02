from setuptools import setup

setup(
    name = 'dtplib',
    packages = ['dtplib'],
    version = '1.1.1',
    license = 'MIT',
    description = 'Data Transfer Protocol Library - Network server classes',
    long_description = ''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type = 'text/markdown',
    author = 'Will Allen',
    author_email = 'wkhallen@gmail.com',
    url = 'https://github.com/WKHAllen/dtplib',
    keywords = ['sockets', 'networking', 'server', 'client'],
    install_requires = ['compressdir', 'cryptography', 'rsa'],
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
