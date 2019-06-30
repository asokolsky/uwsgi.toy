#
#  Flask app launcher
#

from app import create_app

# print( '__file__:' + ___file__ )

app = create_app('alex.cfg')
app.run()
