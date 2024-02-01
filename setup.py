from setuptools import setup, find_packages

setup(
    name='ml-refresher',
    version='0.0',
    packages=find_packages(),
    url='<Your-Project-URL>',
    license='MIT License',
    author='aboissie',
    author_email='aboissie[at]stanford[dot]edu',
    description='A short refresher of the main methods used in machine learning',
    install_requires=[
        'numpy>=1.18.1',
        'pandas>=1.0.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
)