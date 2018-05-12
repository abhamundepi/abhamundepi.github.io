# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""panel shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin
from nikola.plugins.compile import markdown


def removePtags(data):
    data = data.replace("<p>", "", 1)
    li = data.rsplit("</p>", 1)
    data = "".join(li)

    return data


class Plugin(ShortcodePlugin):
    """Plugin for panel directive."""

    name = "panel"

    def handler(self, signal="primary", header="", title="", site=None, data=None, lang=None, post=None):
        """Create HTML for marker."""

        if signal.lower() not in ["primary", "warning", "danger", "info", "success"]:
            signal = "primary"

        signal = signal.lower()

        compiler = markdown.CompileMarkdown()
        compiler.set_site(site)

        data, _ = compiler.compile_string(data)
        data = removePtags(data.strip())

        headTag = ""
        titleTag = ""

        if header:
            header, _ = compiler.compile_string(header)
            header = removePtags(header.strip())
            headTag = '<div class="card-header">{}</div>'.format(header)

        if title:
            title, _ = compiler.compile_string(title)
            title = removePtags(title.strip())
            titleTag = '<h4 class="card-title">{}</h4>'.format(title)

        output = '''
<div class="card text-white bg-{0} mb-3" style="max-width: 20rem;">
  {2}
  <div class="card-body">
    {3}
  <p class="card-text">{1}</p>
  </div>
</div>
'''.format(signal, data, headTag, titleTag)

        return output, []
