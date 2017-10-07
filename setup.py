from setuptools import setup, find_packages

def dependancies(file):
    with open(file) as f:
        return f.read().splitlines()


setup(
    name                 = 'Microblog',
    packages             = find_packages(exclude=('sample','tests', 'docs', 'tmp')),
    version              = '0.0.1',
    license              = 'GPL-3.0',
    description          = 'Build a microlog using Python\'s Flask ',
    long_description     = 'Flask Web Application building a microblog using Python. Full documentation available here: https://github.com/sneakymelon/microblog',
    author               = 'Allan Davidson',
    author_email         = 'allan_m_e_davidson@hotmail.com',
    url                  = 'https://github.com/sneakymelon/microblog/',
    keywords             = [],
    install_requires     = dependancies('requirements.txt'),
    tests_require        = '',
    include_package_data = True
)
