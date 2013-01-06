from setuptools import setup, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

class PyTestWithCov(PyTest):
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py', '--cov-report=html', '--cov=.', '--pdb'])
        raise SystemExit(errno)

setup(
    name='fanstatic',
    version='0.13dev',
    description="Flexible static resources for web applications.",
    classifiers=[
      "Programming Language :: Python :: 2.5",
      "Programming Language :: Python :: 2.7",
    ],
    keywords='',
    author='ENDOH takanao',
    long_description=open('README.txt').read(),
    license='BSD',
    url='http://fanstatic.org',
    packages=['fanstatic'],
    include_package_data=True,
    zip_safe=False,
    extras_require = dict(
        test=['pytest >= 2.0'],
    ),
    cmdclass = {
      'test': PyTest,
      'cov': PyTestWithCov,
    },
)
