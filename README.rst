=====
Blogs
=====

Blogs is a simple Django app to conduct Web-based Blogs. This Blog app
allows authorized users to maintain a blog. Blogs are a series of posts
that are time stamped and are typically viewed by date. Blog entries can
be made depending on which roles have access to add blog.

Quick start
-----------

1. Add "blog" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'blog',
        'ckeditor',
        'ckeditor_uploader',
    ]

2. Add following lines to your settings.py:

    MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
    MEDIA_URL = "/uploads/"

    CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
    CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
    CKEDITOR_IMAGE_BACKEND = "pillow"
    CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
    CKEDITOR_UPLOAD_PATH = "uploads/"

    CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'full',
        'height': 100,
        'allowedContent': True,
    },
    }
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

3. Add following lines in url.py file

   from django.conf.urls import url, include
   from django.conf import settings
   from django.views.static import serve
   from django.conf.urls.static import static
   from django.core.urlresolvers import reverse

   add the following url in urlpatterns:
   url(r'^ckeditor/', include('ckeditor_uploader.urls')),

   and at the end of urlpatterns:
   '+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'

    urlpatterns += [
      url(r'^media/(?P<path>.*)$', serve, {
          'document_root': settings.MEDIA_ROOT,
      }),
    ]

3. Run `python manage.py makemigrations` to create the blogs models.

4. Run `python manage.py migrate` to create the blogs models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a blog (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/blog/ to participate in the Blog.
