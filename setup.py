from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tableau-python-integration",  # Replace with your own package name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python project to integrate Tableau with Python and manage server setups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tableau-python-integration",  # Replace with the actual repo URL
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/tableau-python-integration/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with the correct license for your project
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    python_requires=">=3.6",  # Define your Python version compatibility
    install_requires=[  # List of dependencies
        "requests",  # Example: Add actual required packages
        "pyyaml",
        "tabpy",  # Include TabPy for Tableau Python integration
    ],
    entry_points={
        "console_scripts": [
            "run_tabpy=server_setup.run_tabpy_server:main",  # Add a command-line script for running the TabPy server
        ],
    },
    # Optional dependencies for other use cases
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",  # For formatting
            "flake8",  # For linting
        ],
    },
)
