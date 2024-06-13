from setuptools import setup, find_packages
import os

# Print all files to be included (for debugging)
for dirpath, dirnames, filenames in os.walk('UploadAPI'):
    for file_name in filenames:
        print(os.path.join(dirpath, file_name))

setup(
    name="UploadAPI",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'run_UploadAPI=UploadAPI.app:main',
        ],
    },
    package_data={
        'UploadAPI': ['templates/*.html', 'uploads/*'],
    },
    author="Suhas",
    author_email="suhassahadevan02@gmail.com",
    description="This API is used to accept file uploads from end users.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SuhasSahadev/Uploadapi.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
