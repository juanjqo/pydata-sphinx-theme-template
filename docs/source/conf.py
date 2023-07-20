# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path
import datetime


sys.path.append(str(Path(".").resolve()))
path_str = str(Path(__file__).parent.parent)

# -- Project information

project = 'MyProject'
copyright = str(datetime.date.today().year)+' Gabriel Garcia Marques'
author = 'Gabriel Garcia Marques'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = "pydata_sphinx_theme"

html_logo = path_str + "/build/html/_images/mylogo.svg"
html_favicon = path_str + "/build/html/_images/mylogo.svg"

language = "en"
html_sourcelink_suffix = ""

html_theme_options = {
    "external_links": [

        {
            "url": "https://github.com/dqrobotics/learning-dqrobotics-in-matlab",
            "name": "Learn DQ Robotics",
        },
        {
            "url": "https://hal.science/hal-01478225v1",
            "name": "Learn Dual Quaternion Algebra",
        },
        {
            "url": "https://ros2-tutorial.readthedocs.io/en/latest/",
            "name": "Learn ROS2",
        },
    ],
    "header_links_before_dropdown": 4,
    "icon_links": [

        {
            "name": "GitHub",
            "url": "https://github.com/juanjqo/pydata-sphinx-theme-template",
            "icon": "fa-brands fa-github",
        },

        {
            "name": "MyLogo",
            "url": "https://github.com/juanjqo/pydata-sphinx-theme-template",
            "icon": "https://raw.githubusercontent.com/juanjqo/pydata-sphinx-theme-template/main/docs/_static/mylogo.svg",
            "type": "local",
            "attributes": {"target": "_blank"},
        },
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    "logo": {
        "text": "Home",
        "image_dark": "/docs/build/html/_static/mylogo.svg",
        "alt_text": "MyProject",
    },
    "use_edit_page_button": False,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    #"navbar_center": ["version-switcher", "navbar-nav"],
    #"announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
    # "show_nav_level": 2,
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    #"primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "article_footer_items": ["test.html", "test.html"],
    # "content_footer_items": ["test.html", "test.html"],
    # "footer_start": ["test.html", "test.html"],
    # "secondary_sidebar_items": ["page-toc.html"],  # Remove the source buttons

    #"primary_sidebar_end": ["sidebar-ethical-ads"],
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
}

html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"]
}

# -- Options for EPUB output
epub_show_urls = 'footnote'