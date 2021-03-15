import logging

from flask import Flask

import configs


app = Flask(__name__)
app.logger.setLevel(getattr(logging, configs.LOG_LEVEL))
