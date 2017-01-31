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
    <title>Web Casear</title>
<style>
.error {
    color: red;
}
</style>
</head>
<body>
    <h1>Web Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

encrypted_message = ""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        header = "<h3>Caesar Encryption!</h3>"

        message = self.request.get('tb_message')
        rot = self.request.get('tb_rot')

        if len(rot) > 0:
            rot = int(self.request.get('tb_rot'))
            encrypted_message = encrypt(message, rot)
        else:
            encrypted_message = message

        textarea = '''<textarea>
                Message to encrypt:
                <input type="text" name="tb_message" value="''' + encrypted_message+ '''"/>
            </textarea>
            </br>
            <label>
                Rotate by:
                <input type="text" name="tb_rot"/>
                characters.
            </label>
            </br>'''

        submit = '''<input type="submit" value="Encrypt it!"/>'''

        encrypt_form = '''<form action="/encrypt" method="post">''' + textarea + submit + '''</form>'''

        # error = self.request.get('error')
        # if error:
        #     error_element = '''<p class = "error">''' +cgi.escape(error, quote=True)+'''</p>'''
        # else:
        #     error_element = ""

        page_content = page_header + header + encrypt_form + page_footer

        self.response.write(page_content)
#
# class Encrypt(webapp2.RequestHandler):
#     def post(self):
#         message = self.request.get("tb_message")
#         rot = self.request.get("tb_rot")
#         error = ""
#         encrypted_message = ""
#
#         if message == "":
#             error = "Please enter a message to encrypt."
#
#         if not check_int(rot):
#             error = "Rotation number must be an integer!"
#             encrypted_message = message
#
#         if error == "":
#             encrypted_message = encrypt(message,int(rot))
#
#         self.redirect('/?error='+ error)






class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
