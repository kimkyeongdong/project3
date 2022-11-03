import csv
import pickle
from flask import Blueprint, render_template, request
from pro3_app import CSV_FILEPATH



area_bp = Blueprint('area', __name__, url_prefix='/area')

# 위에서 /area가 붙어있으므로 /만쓴다.
@area_bp.route('/')
def area_input():

    return render_template('area.html')

@area_bp.route('/result', methods= ['POST', 'GET'])
def area_result():
    # form 형식 -> post로 받을경우 args가 아닌 form 으로 사용
    ph = request.form.get('PH')
    cod = request.form.get('COD')
    toc = request.form.get('TOC')
    ss = request.form.get('SS')
    doc = request.form.get('DOC')
    tp = request.form.get('TP')
    tcoli = request.form.get('TCOLI')
    ecoli = request.form.get('ECOLI')
    X_test = [ph,cod,toc,ss,doc,tp,tcoli,ecoli]

    
    params = {'PH' : ph, 'COD': cod, 'TOC': toc, 'SS': ss, 'DOC': doc, 'TP': tp, 'TCOLI': tcoli, 'ECOLI': ecoli}
    
    with open('./model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)
        X_test = [X_test]
        result = model.predict(X_test)
    
    
    return render_template('result.html', input=params, result_input=result)

@area_bp.route('/result1', methods= ['POST', 'GET'])
def area_result1():
    import pandas as pd
    
    area = request.form.get('AREA')
    # 경로설정 주의!! 
    data = pd.read_csv("./pro3_app/water2.csv")
    re = data[(data['PT_NM'] == area) & (data['WMYR'] == 2022) & (data['WMWK'] == "3회차") & (data['WMOD'] == 5)]
    
    resu = re[['ITEM_PH','ITEM_COD','ITEM_TOC','ITEM_SS','ITEM_DOC','ITEM_TP','ITEM_TCOLI','ITEM_ECOLI']]

    # 쉼표생성기
    sel = []
    for i in resu.columns:
        col = resu[i].values
        sel.extend(col)      
    X_test = [sel]
        
    with open('./model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)
        result = model.predict(X_test)
    
    
    return render_template('result1.html', input2=X_test,result_input2=result, input_area=area)
