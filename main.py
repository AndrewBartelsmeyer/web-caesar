import webapp2
from helpers import alphabet_position, rotate_character, check_int
from caesar import user_input_is_valid, encrypt
import cgi


def build_page(textarea_content):
    message = 'I hate video tutorials'
    encrypted_message = encrypt(message,13)

    header = "<h1>Web Caesar</h1>"
    rotlabel = "<label>Rotate by:</label>"
    rotinput = "<input type='number' name='rotation'/>"
    messagelabel = "<label>Message to encrypt:</label>"
    textarea = "<textarea name = 'message'>" + textarea_content + "</textarea>"
    submit = "<input type = 'submit'/>"
    form = "<form method = 'post'>" + rotlabel + rotinput + "<br>" + messagelabel + textarea + "<br>" + submit + "</form>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rot = self.request.get("rotation")
        if check_int(rot):
            rot = int(rot)
            encrypted_message = encrypt(message, rot)
        else:
            encrypted_message = message
        escaped_message = cgi.escape(encrypted_message, quote=True)
        content = build_page(escaped_message)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug = True)
