from setuptools import setup, find_packages

setup(
    name='MyQRPackage', 
    version='0.1.0',  
    author='Renan Maciel',  
    author_email='renan.maciel@physics.uu.se',  
    description='A package for QR decomposition using Householder reflections', 
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    url='https://github.com/RenanM05/AdvancedPython2022/tree/main/FinalProject/MyQRPackage',  
    packages=find_packages(),  
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    # Minimum version requirement of the package
    python_requires='>=3.6', 
    install_requires=[
        'numpy',  
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    include_package_data=True, 
    zip_safe=False, 
)
