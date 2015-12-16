from setuptools import setup, find_packages


setup(name="uris",
      version="0.1.0",
      description="A command line tool to interact with URI Online Judge",
      url="https://github.com/gilbertoalexsantos/uris",
      author="Gilberto A. dos Santos",
      author_email="gilberto.alexsantos@gmail.com",
      license="MIT",
      packages=find_packages(),
      zip_safe=False,
      entry_points={
          'console_scripts': ["uris=uris.main:execute"],
      },
      install_requires=[
          'Scrapy==1.0.3',
      ],
)
