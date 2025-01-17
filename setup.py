from setuptools import setup, find_packages

setup(
    name='sorl-thumbnail',
    use_scm_version=True,
    description='Thumbnails for Django',
    long_description=open('README.rst').read(),
    author="Mikko Hellsing",
    author_email='mikko@aino.se',
    maintainer="Jazzband",
    maintainer_email="roadies@jazzband.co",
    license="BSD",
    url='https://github.com/jazzband/sorl-thumbnail',
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms='any',
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
    ],
    setup_requires=['setuptools_scm'],
)
