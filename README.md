## 🤖👾 ReFleX - Deep Image Search/Recognition 

Core idea is to develop a software to capture and identify an image and search for the same on websites, social medias and search engines using an optimized image recognition algorithm.

### Image Search engines

- Social Catfish – https://socialcatfish.com/reverse-image-search/
- Tiny Eye – https://www.tineye.com/
- Image Raider – https://www.imageraider.com/
- Small SEO Tools – http://smallseotools.com/reverse-image-search/
- Google Image Search: https://www.google.com/imghp
- Bing Image Search: https://www.bing.com/images/ (Best if location and language is set to US English)
- Yahoo Image Search: https://images.search.yahoo.com/
- Flickr Advanced Search: https://www.flickr.com/search/advanced/ (Best if logged in)
- DuckDuckGo Image Search: https://duckduckgo.com/test?ia=images
- Dogpile Image Search: https://www.dogpile.com/?qc=images
- Pinterest Visual Search Tool: https://www.pinterest.com/

------

#### Useful for:

1. Verifying the identity of a person you meet online
2. Photographers trying to find people using their copyrighted photos
3. Identify if a rental is being listed on other sites illicitly
4. Find products you want that you see on pinterest or other sites
5. Track down artists whom you wish to find more of their art
   And more...

#### To-Do

- [ ] Deep-Learning model
- [ ] Search engine integrations
- [ ] Report/Result module

##### Project Structure

Please follow the below project structure for this project when contributing. For more details refer: https://exploreflask.com/en/latest/organizing.html

<pre>
config.py
requirements.txt
run.py
instance/
    config.py
reflex/
    __init__.py
    views.py
    models.py
    forms.py
    static/
    templates/
</pre>
##### Structure details 
<pre>
run.py	This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.
requirements.txt	This file lists all of the Python packages that your app depends on. You may have separate files for production and development dependencies.
config.py	This file contains most of the configuration variables that your app needs.
/instance/config.py	This file contains configuration variables that shouldn’t be in version control. This includes things like API keys and database URIs containing passwords. This also contains variables that are specific to this particular instance of your application. For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development. Since this file will be read in after config.py, it will override it and set DEBUG = True.
/yourapp/	This is the package that contains your application.
/yourapp/__init__.py	This file initializes your application and brings together all of the various components.
/yourapp/views.py	This is where the routes are defined. It may be split into a package of its own (yourapp/views/) with related views grouped together into modules.
/yourapp/models.py	This is where you define the models of your application. This may be split into several modules in the same way as views.py.
/yourapp/static/	This directory contains the public CSS, JavaScript, images and other files that you want to make public via your app. It is accessible from yourapp.com/static/ by default.
/yourapp/templates/	This is where you’ll put the Jinja2 templates for your app.
</pre>


Please read the [LICENSE](https://github.com/dedsecinside/ReFleX/blob/master/LICENSE) here.



