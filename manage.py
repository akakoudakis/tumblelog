# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from tumblelog import app

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    port=int(os.getenv('VCAP_APP_PORT', '5000')),
    host='0.0.0.0')
)

if __name__ == "__main__":
    manager.run()
