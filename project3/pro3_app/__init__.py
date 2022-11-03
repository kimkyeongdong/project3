import os
from flask import Flask

# CSV 파일 경로와 임시 파일 경로입니다.
CSV_FILEPATH = os.path.join(os.getcwd(), __name__, 'water.csv') 



def create_app(config=None):
    
    app = Flask(__name__)
    if config is not None:
        app.config.update(config)

    from pro3_app.view.main_view import main_bp
    from pro3_app.view.area_view import area_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(area_bp, url_prefix='/area')
    
       
    return app

if __name__=="__main__":
    app = create_app()
    app.run(debug = True)

