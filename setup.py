from setuptools import setup

setup(
    name="gpt-interface",
    version="0.1",
    packages=["gpt_interface"],
    entry_points={
        "console_scripts": [
            "gpt=gpt_interface.interface:main",
        ],
    },
)
