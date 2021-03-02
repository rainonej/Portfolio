# modified from https://gist.github.com/tebeka/5426211
# updated to work with Python 3

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
import cherrypy
from io import BytesIO
import base64

class HelloWorld:
    def index(self):
        d = self.plot()
        return ''' <form action="/">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="firstname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
 <img src="data:image/png;base64,%s" width="640" height="480" border="0" /> ''' %(d.decode('utf8'))
    index.exposed = True
    print(cherrypy.request.params.get('firstname'))

    def plot(self):
        image = BytesIO()
        x = numpy.linspace(0, 10)
        y = numpy.sin(x)
        pyplot.plot(x, y)
        pyplot.savefig(image, format='png')
        return base64.encodestring(image.getvalue())

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())