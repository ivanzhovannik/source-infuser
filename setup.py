from setuptools import setup, find_packages

def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()

setup(
    name='source_infuser',
    version='0.0.1',  # Update this version before each release
    author='Ivan Zhovannik',
    author_email='i.zhovannik-at-maastrichtuniversity-dot-nl',
    description='A package to prepare your software project for continuous infusion into your AI assistant',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/ivanzhovannik/source-infuser',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'source_infuser=scripts.infuser:main',
            'psi=scripts.infuser:main'
        ],
    },
)
