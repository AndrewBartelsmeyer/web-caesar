#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from helpers import alphabet_position, rotate_character, check_int
from caesar import user_input_is_valid, encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
<style>
.error {
    color: red;
}
</style>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Caesar Encryption!</h3>"

        # a form for adding new movies
        encrypt_form = """
        <form action="/encrypt" method="post">
            <label>
                Message to encrypt:
                <input type="text" name="tb_message"/>
                to my watchlist.
            </label>
            <input type="submit" value="Encrypt it!"/>
            <label>
                Rotate by:
                <input type="text" name="tb_rot"/>
                characters.
            </label>
        </form>
        """

        error = self.request.get('error')
        if error:
            error_element = '''<p class = "error">''' +cgi.escape(error, quote=True)+'''</p>'''

class Encrypt(webapp2.RequestHandler):
    def post(self):
        message = self.request.get("tb_message")
        rot = self.request.get("tb_rot")

        if message == "":
            error = "Please enter a message to encrypt."

        if !check_int(rot):
            error = "Rotation number must be an integer!"


            


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypt', Encrypt)
], debug=True)
