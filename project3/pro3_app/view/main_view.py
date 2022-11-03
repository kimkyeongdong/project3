from flask import Blueprint, render_template
# from pro3_app import CSV_FILEPATH

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():

      return render_template('index.html')


@main_bp.route('/dashboard')
def dash():
    
    
    return render_template('dashboard.html')
