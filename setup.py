from distutils.core import setup


requirements = [
    'numpy',
    'rpy2'
]


setup(
    name='pyclub_libs',
    version='0.1.1',
    packages=['pyclub_libs',
              'pyclub_libs.logging',
              'pyclub_libs.logging'
              ],
    requires=requirements,
    download_url='git+git://github.com/swc-pyclub/pyclub_libs',
    url='https://github.com/swc-pyclub/pyclub_libs',
    license='GPLv3',
    author='PyClub',
    author_email='pyclub <pyclub@live.ucl.ac.uk>',
    description='Libraries from the SWC python club',
    classifiers=['Intended Audience :: Developers',
                 'Topic :: Software Development']
)


# TODO: add package_data={} for documentation

