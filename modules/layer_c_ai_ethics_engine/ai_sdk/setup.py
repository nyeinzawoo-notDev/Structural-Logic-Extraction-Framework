from setuptools import setup, find_packages

with open("README_MM.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nstf-ethics",
    version="1.0.0",
    author="NSTF Research Team",
    author_email="nstf@example.com",
    description="Myanmar Cultural & Ethical AI Framework - NSTF-NNLDS Core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "aiohttp>=3.8.0",
        "nest-asyncio>=1.5.0",
    ],
    package_data={
        "nstf_ethics": ["data/*.csv"],
    },
    include_package_data=True,
    keywords="myanmar, ethics, ai, nstf, cultural, framework",
    project_urls={
        "Documentation": "https://github.com/nstf-ethics/nstf-sdk",
        "Source Code": "https://github.com/nstf-ethics/nstf-sdk",
    },
)
