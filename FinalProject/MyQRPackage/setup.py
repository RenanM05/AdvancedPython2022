from setuptools import setup, find_packages

setup(
    name='MyQRPackage',
    version='0.1',
    author='Renan Maciel',  
    author_email='renan.maciel@physics.uu.se',  
    url='https://github.com/RenanM05/AdvancedPython2022/tree/main/FinalProject/MyQRPackage',      
    description='A package for QR decomposition using Householder reflections.',
    classifiers=[
        'License :: OSI Approved :: MIT License',        
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',        
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy',  
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
)
