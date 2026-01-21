from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pomodoro-timer",
    version="1.0.0",
    author="dtt4h",
    author_email="dtt4h322@gmail.com",
    description="A modern, minimalist Pomodoro timer application built with Python and PyQt5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pomodoro-timer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    install_requires=[
        "PyQt5>=5.15.0",
    ],
    entry_points={
        "console_scripts": [
            "pomodoro-timer=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/*", "logs/*"],
    },
    zip_safe=False,
)
