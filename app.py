import logging
 
from flask import Flask
import papermill as pm
 
app = Flask(__name__)
 
 
@app.route('/')
def main(request=None):
    logging.info("starting job")
    
    pm.execute_notebook(
        'cloud_run.ipynb',
        'tmp/cloud_run_out.ipynb',
    )
    logging.info("job completed")
    return 'ok'
 
 
if __name__ == '__main__':
    import os
 
    port = os.environ.get('PORT', '8080')
    app.run(port=port)