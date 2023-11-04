import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "pyblox",
    "version": "2.0.0",
    "author": "invalidkaro",
    "author_email": "mail@invalidkaro.dev",
    "description": "Pyblox is a  object-oriented asynchronous Python wrapper for the Roblox web API.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/invalidkaro/pyblox",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Software Development :: Libraries"
    ],
    "project_urls": {
        "Discord": "https://discord.gg/",
        "Issue Tracker": "https://github.com/invalidkaro/pyblox/issues",
        "GitHub": "https://github.com/invalidkaro/pyblox",
        "Examples": "https://github.com/invalidkaro/pyblox/tree/main/examples",
        "Twitter": "https://twitter.com/karoschal"
    },
    "python_requires": '>=3.7',
    "install_requires": [
        "httpx>=0.21.0",
        "python-dateutil>=2.8.0"
    ]
}


setuptools.setup(**setup_info)
