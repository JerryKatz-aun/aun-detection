from setuptools import setup, find_packages

setup(
    name='aun-detection',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Jerry Katz',
    author_email='halifaxjerrykatz@gmail.com',
    description='AI mimicry detection using symbolic collapse logic (∿)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/halifaxjerrykatz-dotcom/aun-detection',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
