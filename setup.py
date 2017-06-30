import setuptools

setuptools.setup(
    name="domain.uptime",
    version="1.0.0",
    url="https://github.com/humberthomattar/domain.uptime",

    author="Humbertho Mattar",
    author_email="humberthomattar[at]gmail[dot]com",

    description="Simple way to evaluates if yours domains are up. Line command and batch process.",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
