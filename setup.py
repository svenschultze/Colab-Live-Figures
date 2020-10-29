import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colab_live_figures",
    version="1.0.0",
    author="Sven Schultze",
    author_email="sven.schultze@uol.de",
    description="Package for live-updating figures in Google Colaboratory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/svenschultze/Colab-Live-Figures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'numpy',
        'opencv-python',
        'ffmpeg-python'
    ]
)