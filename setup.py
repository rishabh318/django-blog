import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name = 'admindjango-ckeditor-blog',
  packages = find_packages(),
  include_package_data = True,
  version='0.1',
  description='django-blogs app to provide you facility to craete a blogs in admin panel',
  long_description = README,
  author = 'Rishabh',
  author_email = 'rishabh.khare88@gmail.com',
  url = 'https://github.com/rishabh318/django-blog', # use the URL to the github repo
  download_url = 'https://github.com/rishabh318/django-blog/archive/master.zip', # I'll explain this in a second
  keywords = ['Blog', 'Blogs', 'django', 'ckeditor'], # arbitrary keywords
  install_requires=[
         'Django==1.11.2',
         'django-ckeditor==5.2.2',
         'django-multiselectfield==0.1.7',
         'olefile==0.44',
         'Pillow==4.1.1',
         'pytz==2017.2'
     ],
  zip_safe=False,
  classifiers = [],
)
