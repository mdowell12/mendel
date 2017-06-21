from setuptools import setup

setup(
    name='myservice',
    version='0.1',
    packages=['hello'],
    include_package_data=True,
    license=None,
    url="fake url",
    description="A basic python app.",
    classifiers=[],
    # Note that we currently need something here, or the distribution
    # won't have a 'require.txt' file, which mendel assumes is present:
    install_requires=['requests'],
)
