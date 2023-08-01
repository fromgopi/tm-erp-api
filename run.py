import os

from apps import db, create_app
from apps.common.constants import DEFAULT_PORT
from apps.configuration.modules.logger import RequestHandlerLoggerOverride

app = create_app()

if __name__ == "__main__":
    port = app.config.get('PORT')
    enable_debug = app.config.get('FLASK_DEBUG')
    port = int(port) if port else DEFAULT_PORT
    app.run(
        host='0.0.0.0',
        port=port,
        debug=enable_debug,
        use_debugger=enable_debug,
        use_reloader=enable_debug,
        threaded=True,
        request_handler=RequestHandlerLoggerOverride
    )