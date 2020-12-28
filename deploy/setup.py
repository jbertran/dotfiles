import setuptools

setuptools.setup(
    name='deploy',
    version='0.1.0',
    description='Deploy a dev environment from a YAML desciption file',
    author='Jordi Bertran',
    author_email='j.debalanda@gmail.com',
    setup_requires='setuptools',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(),
    install_requires=['PyYAML', 'doit']
)
