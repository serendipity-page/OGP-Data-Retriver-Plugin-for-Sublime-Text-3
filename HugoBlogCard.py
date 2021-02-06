""" OGP Data Retriver Plugin for Sublime Text 3
Author: insanely serendipitous(Twitter: @drama_eigo)
Webpage: https://www.serendipity.page/

Main goal of this plugin is make writing Hugo articles experience
less painful, which is, Hugo's shortcode feature has no ability to
retrive OGP data from given url when you want to make a fancy visual link
like twitter has instead of good ol' markdown [text](link).

Some people's already come up with several ideas aka workarounds
like running JSON API server in the background or something.
However, to me it's just too much.

My idea here is why not retrive the whole data when you're editing?,
which led to this plugin.

Simply, this command executes the followings:

1. get url from the clipboard(beforehand you need to copy the target url)
2. retrive the OGP data from the url
3. modify the OGP data for HUGO shortcode
4. insert the modified string at the current cursor

I try to avoid any external module, so I believe this'll work for all ST3.

If an error occurs, nothing will happen.
Just spit the error information into the ST3 console.

You can modify the template and use it as a general OGP Data Retriver.

If you like this plugin, you can bind the command to a specific key combination
from Preferences > Key Bindings – Default menu.

Once binding a key, what you need is copy the url you want to link,
and move the cursor to the place where you want to insert the link,
and execute the command by pressing binded key combination.

Thanks and have a heavenly day!
"""

import sublime, sublime_plugin
from html.parser import HTMLParser
import urllib.request

referer     = "http://www.yahoo.com/"
user_agent  = "Mozilla/5.0"
html_decode = "utf-8"
tag_name    = "meta"

# retrive all meta tag info
class MetaGrabber(HTMLParser):        
    def handle_starttag(self, tag, attrs):
        if tag == tag_name:
            self.meta.append(attrs)

    def feed(self, content):
        self.meta = []
        super().feed(content)

    def get_meta_data(self):
      return self.meta

# to avoid a 403 response from web servers
# Perhaps you need more headers, at least my website requires these two.
def create_request(url):
    ret = urllib.request.Request(url)
    ret.add_header("Referer", referer)
    ret.add_header("User-Agent", user_agent)
    return ret

# retrive the whole HTML source of the given url
def read_url_as_utf8(url):
    req = create_request(url)
    with urllib.request.urlopen(req) as res:
        ret = res.read().decode(html_decode)
    return ret

# check whether or not attr is property="og:title"
def is_property_og(attr):
    return (attr[0] == "property") and attr[1].startswith("og:")

# extract ogp from attrs and add it into dic
# takes care of the reverse order
# Eg.
# <meta property="og:title" content="My Website Yippee!!" />
# <meta content="My Website Yippee!!" property="og:title" />
def extract_ogp_from_and_add_to(attrs, dic):
    if len(attrs) != 2:
        return
    if (len(attrs[0]) != 2) or (len(attrs[1]) != 2):
        return
    for i in range(2):
        if is_property_og(attrs[i]):
            if attrs[1-i][0] == "content":
                dic[attrs[i][1][3:]] = attrs[1-i][1]

# obtain all OGP meta tags and append them into a dictionary
def grab_ogp_info_from_url(url):
    ret = {}
    try:
        html = read_url_as_utf8(url)
        ogp = MetaGrabber()
        ogp.feed(html)
        meta = ogp.get_meta_data()
        # gather og properties from meta data
        for attrs in meta:
            extract_ogp_from_and_add_to(attrs, ret)
    except Exception as err:
        print(err) # for debug by using console in ST3
    return ret

shortcode_template = "{{< blogcard %s >}}"
arg_template = '%s = "%s"'
shorten_width = 300 #to avoid letting Hugo shortcode fat
args = ["title", "description", "site_name", "image", "url"]

# shorten a long description
def shorten(str, width):
    if len(str)<=width:
        return str
    return str[:width] + '...'

# <meta property="og:title" content="My Website Yippee!!" />
# add string 'title = "My Website Yippee!!"' to the list
# with template, or do nothing if there is no str key in dic.
def add_arg_code(str, dic, arg_template, list):
    if str in dic:
        content = dic[str].replace('\n', '')
        if str == "description":
            content = shorten(content, shorten_width)
        list.append(arg_template%(str, content))

# <meta property="og:title" content="My Website Yippee!!" />
# <meta property="og:image" content="https://example.com/a.jpg" />
# returns
# '{{< blogcard title = "My Website Yippee!!" image = "https://example.com/a.jpg">}}'
# string with default templates
def formatted_string_from_url(url, whole_template, arg_template):
    ogp_info = grab_ogp_info_from_url(url)
    arg_strs = []
    for arg in args:
        add_arg_code(arg, ogp_info, arg_template, arg_strs)
    ret = whole_template%(" ".join(arg_strs))
    return ret

# This class is used by ST3
# which means you can execute the command
# by enter "view.run_command('hugoblogcard')" on ST3 console
# Bear in mind class name matters, not python file name.
# If you change this class name, say into AbcdefgCommand,
# you should change the command as well into 'abcdefg'.
class HugoblogcardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current_cursor_pos = self.view.sel()[0].begin()
        url = sublime.get_clipboard()
        inserted = formatted_string_from_url(
            url, shortcode_template, arg_template)
        self.view.insert(edit, current_cursor_pos, inserted)
