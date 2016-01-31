import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World! from Lin Haoran')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
