# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""Marker shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin
from nikola.plugins.compile import markdown

def removePtags(data):
    data = data.replace("<p>", "", 1)
    li = data.rsplit("</p>", 1)
    data = "".join(li)

    return data

class Plugin(ShortcodePlugin):
    """Plugin for marker directive."""

    name = "marker"

    def handler(self, signal="warning", site=None, data=None, lang=None, post=None):
        """Create HTML for marker."""

        if signal.lower() not in ["error", "warning", "red", "yellow", "green", "cyan", "blue", "purple"]:
            signal = "warning"

        signal = signal.lower()

        compiler = markdown.CompileMarkdown()
        compiler.set_site(site)

        data, _ = compiler.compile_string(data)
        data = removePtags(data.strip())

        output = '<span class="highlight-short-{0}"> {1} </span>'.format(signal, data)

        return output, []
