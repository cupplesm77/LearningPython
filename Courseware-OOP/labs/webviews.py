'''_

Let's create a simple web application framework. We'll need view
classes for each page on the site:

>>> home_view = HomePageView()
>>> home_view.render()
'<html><body>Welcome!</body></html>'
>>> home_view.body
'Welcome!'

>>> about_view = AboutPageView()
>>> about_view.render()
'<html><body>This is a simple website about nutrition.</body></html>'

To route URLs to views, we'll create a global webapp object.

>>> app = WebApp()

It will keep track of the mappings with a protected variable:

>>> type(app._routes)
<class 'dict'>

Routings - that is, a mapping from a URL to a view object - are
created with add_route(). Then you can get and render the view with
get().

>>> app.add_route("/", home_view)
>>> app.add_route("/about/", about_view)
>>> app.get("/")
'<html><body>Welcome!</body></html>'
>>> app.get("/about/")
'<html><body>This is a simple website about nutrition.</body></html>'

Let's create some more views. This site has two kinds of endpoints:
HTML pages, for browser content, and JSON objects, for API access.

>>> class ContactView(HTMLView):
...     body = 'Get in touch at hello@example.com'
...
>>> app.add_route("/contact/", ContactView())
>>> app.get("/contact/")
'<html><body>Get in touch at hello@example.com</body></html>'

(Hint for the JSON endpoints: One of the functions in the json module
takes an option to sort object keys.)

>>> class CarrotInfoView(JSONView):
...     def data(self):
...         return {
...             'serving_size': 61,
...             'fat': 0.1,
...             'calories': 25,
...             'protein': 0.6,
...             }

>>> carrot_view = CarrotInfoView()
>>> carrot_view.render()
'{"calories": 25, "fat": 0.1, "protein": 0.6, "serving_size": 61}'
>>> app.add_route("/api/carrot/", carrot_view)

Create a view for baked chicken nutritional info:

>>> app.add_route("/api/chicken/", ChickenInfoView())
>>> app.get("/api/chicken/")
'{"calories": 231, "fat": 5, "protein": 43, "serving_size": 140}'

And another for tomato:

>>> app.add_route("/api/tomato/", TomatoInfoView())
>>> app.get("/api/tomato/")
'{"calories": 22, "fat": 0.2, "protein": 1.1, "serving_size": 123}'

And let's add a helper to give us a sorted list of all URLs defined so far.

>>> app.urls()
['/', '/about/', '/api/carrot/', '/api/chicken/', '/api/tomato/', '/contact/']

It's important to keep your class hierarchies well-organized. Since
every view has a render() method, it makes sense to put that in a
common base class.

>>> type(View.render)
<class 'function'>

>>> isinstance(home_view, View)
True
>>> issubclass(ChickenInfoView, View)
True

And we can have more specialized views, FOR EXAMPLE WHEN WE WANT TO
OUR WRITING TO MAKE AN IMPACT:

>>> class LegalView(ShoutingHTMLView):
...     body = 'you agree to our terms of service!'

>>> legal_view = LegalView()
>>> app.add_route("/legal/", legal_view)
>>> app.get("/legal/")
'<HTML><BODY>YOU AGREE TO OUR TERMS OF SERVICE!</BODY></HTML>'
>>> isinstance(legal_view, HTMLView)
True

Python lets you do something called "monkey patching".  It can lead to
hard-to-understand code, so don't overuse it. But it can be useful
when working with certain libraries whose source you cannot/do not
want to modify, for example.

The idea is you modify a method of an already-created object, or a
superclass deep in an inheritance hierarchy, by assigning to it
directly. It works because in Python, (a) everything is an object, and
(b) methods are just attributes that can be assigned to.

>>> original_htmlview_render = HTMLView.render
>>> def new_htmlview_render(self):
...     # Add <p> tag around content
...     return '<html><body><p>' + self.body + '<p></body></html>'
>>> HTMLView.render = new_htmlview_render

Now that HTMLView is modified, instances of its subclasses are
modified too - provided that subclass reuses that method defined in
the superclass:

>>> legal_view.render()
'<HTML><BODY><P>YOU AGREE TO OUR TERMS OF SERVICE!<P></BODY></HTML>'

'''

# Write your code here:
    
# classes:
    
class WebApp:
    def __init__(self):
        self._routes = {}
        
    def add_route(self, path, view):
        self._routes[path] = view.render()
        
    def get(self, path):
        msg = self._routes[path]
        #print(msg)
        return msg
    
    def urls(self):
        url_list = sorted([value for value in self._routes.keys()])
        return url_list
    
import abc    
class View(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self):
        pass

# from bs4 import BeautifulSoup as bs4
class HTMLView(View):
    body = ''
    # DEFAULT_HTML_MESSAGE = '''
    # <html><body></body></html>
    # '''.strip()
    # soup = bs4(DEFAULT_HTML_MESSAGE, 'html.parser')
    # body = soup.find('body').text
    
    def render(self): 
        return '<html><body>' + self.body + '</body></html>'

class ShoutingHTMLView(HTMLView):
    body = ''
    # def render(self):  
    #     return '<html><body>'.upper() \
    #         + self.body.upper() \
    #             + '</body></html>'.upper()
    def render(self):
        return super().render().upper()             


class HomePageView(HTMLView):
    body = 'Welcome!'
    # HOMEPAGE_HTML_MESSAGE = '''
    # <html><body>Welcome!</body></html>
    # '''.strip()
    # soup = bs4(HOMEPAGE_HTML_MESSAGE, 'html.parser')
    # body = soup.find('body').text     
    

class AboutPageView(HTMLView):
    body = 'This is a simple website about nutrition.'
    # ABOUTPAGE_HTML_MESSAGE = '''
    # <html><body>This is a simple website about nutrition.</body></html>
    # '''.strip()     
    # soup = bs4(ABOUTPAGE_HTML_MESSAGE, 'html.parser')
    # body = soup.find('body').text    

class ContactView(HTMLView):
    body = 'Get in touch at hello@example.com'
    # CONTACT_HTML_MESSAGE = '''
    # <html><body>Get in touch at hello@example.com</body></html>
    # '''.strip()    
    # soup = bs4(CONTACT_HTML_MESSAGE, 'html.parser')
    # body = soup.find('body').text
    def render(self):
        return super().render()    

class LegalView(ShoutingHTMLView):
    body = 'you agree to our terms of service!'
    def render(self):  
        return super().render().upper()

import json
class JSONView(View):
    @abc.abstractmethod
    def data(self):
        return {}    
    # def render(self):        
    #     return json.dumps(dict(sorted(self.data().items())))    
    def render(self):
        return json.dumps(self.data(), sort_keys=True)    

class CarrotInfoView(JSONView):
    def data(self):
        return {
                'serving_size': 61,
                'fat': 0.1,
                'calories': 25,
                'protein': 0.6,
                }
    
    # def render(self):    
    #     return json.dumps(dict(sorted(self.data().items())))

class ChickenInfoView(JSONView):
    def data(self):
        return {
                'serving_size': 140,
                'fat': 5,
                'calories': 231,
                'protein': 43,
                }
    
    # def render(self):    
    #     return json.dumps(dict(sorted(self.data().items())))


class TomatoInfoView(JSONView):
    def data(self):
        return {
                'serving_size': 123,
                'fat': 0.2,
                'calories': 22,
                'protein': 1.1,
                }
    
    # def render(self):    
    #     return json.dumps(dict(sorted(self.data().items())))


# body of code

home_view = HomePageView()
print(home_view.render())
print(home_view.body)

about_view = AboutPageView()
print(about_view.render())

print(type(View.render))
isinstance(home_view, View)

app = WebApp()
print(type(app._routes))

app.add_route("/", home_view)
app.add_route("/about/", about_view)
print(app.get("/"))
# '<html><body>Welcome!</body></html>'
print(app.get("/about/"))
# '<html><body>This is a simple website about nutrition.</body></html>'

#contact_view = ContactView()
#print(contact_view.body)
app.add_route("/contact/", ContactView())
#app.add_route("/contact/", ContactView())
print(app.get("/contact/"))
# '<html><body>Get in touch at hello@example.com</body></html>'
    
carrot_view = CarrotInfoView()
print(carrot_view.render())
# # '{"calories": 25, "fat": 0.1, "protein": 0.6, "serving_size": 61}'
app.add_route("/api/carrot/", carrot_view)

app.add_route("/api/chicken/", ChickenInfoView())
print(app.get("/api/chicken/"))
#'{"calories": 231, "fat": 5, "protein": 43, "serving_size": 140}'

app.add_route("/api/tomato/", TomatoInfoView())
print(app.get("/api/tomato/"))
#'{"calories": 22, "fat": 0.2, "protein": 1.1, "serving_size": 123}'

print(app.urls())
# ['/', '/about/', '/api/carrot/', '/api/chicken/', '/api/tomato/', '/contact/']

print(type(View.render))
#<class 'function'>

print(isinstance(home_view, View))
#True
print(issubclass(ChickenInfoView, View))
#True

legal_view = LegalView()
app.add_route("/legal/", legal_view)
print(app.get("/legal/"))
# '<HTML><BODY>YOU AGREE TO OUR TERMS OF SERVICE!</BODY></HTML>'
print(isinstance(legal_view, HTMLView))

original_htmlview_render = ShoutingHTMLView.render
def new_htmlview_render(self):
    # Add <p> tag around content
    return '<html><body><p>' \
        + self.body \
            + '<p></body></html>'
ShoutingHTMLView.render = new_htmlview_render

print(legal_view.render())
# '<HTML><BODY><P>YOU AGREE TO OUR TERMS OF SERVICE!<P></BODY></HTML>'

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
