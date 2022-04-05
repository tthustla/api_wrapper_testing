from setuptools import setup, find_namespace_packages


def read_version():
    return "0.1"


required = [
    "requests==2.11.1",
    "vcrpy==1.10.3",
    "pytest==3.0.3",
    "python-dotenv==0.20.0"
]


setup(
    name="api_wrapper_testing",
    version=read_version(),
    packages=find_namespace_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    long_description="""
    simple pipeline from api to sqlite
    """,
)