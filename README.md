# OGP Data Retriver Plugin for Sublime Text 3
## Description of the Code
This is a Python 3 code for "Sublime Text 3" plugin.

When your clipboard has a URL string, this plugin tries to retrive the OGP(Open Graph Protocol) data from the URL, process it, and then insert the string at the current cursor.

### eg.(as of Feb. 7, 2021)
clipboard string: "https://github.com/"

inserted string: "{{< blogcard title = "GitHub: Where the world builds software" description = "GitHub is where over 56 million developers shape the future of software, together. Contribute to the open source community, manage your Git repositories, review code like a pro, track bugs and feat..." site_name = "GitHub" image = "https://github.githubassets.com/images/modules/site/social-cards/github-social.png" url = "https://github.com/" >}}"

### Background
I wrote this specifically for a static site generator [Hugo](https://gohugo.io/) because Hugo's shortcode does not let user retrive external data,
and even though there are enormous workarounds on Internet, none of them seems to me OK-ish.

### Tweak
```python
shortcode_template = "{{< blogcard %s >}}"
arg_template = '%s = "%s"'
```

You can modify the processed string by changing the above two template strings.

## How to Install This Plugin
Download HugoBlogCard.py file to your Sublime Text 3 User directory, in my case(Mac) /Users/username/Library/Application Support/Sublime Text 3/Packages/User.
Binding Keys from Preferences > Key Bindings – Default menu like
```json
[
    { 
        "keys": ["ctrl+alt+b"], "command": "hugoblogcard"
    }
]
```

Note: This command should be called by the name "hugoblogcard" in Sublime Text 3 because of the Class name(see source code)

## Link
+ [My Web site(about learning English from foreign TV shows, written in Japanese)](https://www.serendipity.page/)
+ [Article about this plugin(not yet)]
