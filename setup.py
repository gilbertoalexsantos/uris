from setuptools import setup


setup(name="uri",
      version="0.1.0",
      description="A command line tool to interact with URI Online Judge",
      url="http://github.com/gilbertoalexsantos/uri",
      author="Gilberto A. dos Santos",
      author_email="gilberto.alexsantos@gmail.com",
      license="MIT",
      packages=["uri"],
      zip_safe=False,
      entry_points={
          'console_scripts': ["uri=uri.main:execute"],
      },
      install_requires=[
          'Scrapy==1.0.3',
      ],
)
