# setup.py - Complete Package Configuration

from setuptools import setup, find_packages

setup(
    name="nstf-ethical-framework",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0", 
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="NSTF Ethical Framework for AI Systems - Standardized Ethical Reasoning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nstf-ethical-framework",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: AI Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8+",
    ],
    python_requires=">=3.8",
)
