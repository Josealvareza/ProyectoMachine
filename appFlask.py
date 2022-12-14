import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prediccion',methods=['GET','POST'])

def predict():
    if request.method == 'POST':
        try:
            var_1=float(request.form['var_1'])    
            var_2=float(request.form['var_2'])    
            var_3=float(request.form['var_3'])    
            var_4=float(request.form['var_4'])  
            var_5=float(request.form['var_5'])

            pred_args=[var_1,var_2,var_3,var_4,var_5]
            pred_arr=np.array(pred_args)
            preds=pred_arr.reshape(1, -1)
            modelo=open("./Modelonb.pkl","rb")
            modelo_class=joblib.load(modelo)
            prediccion_modelo=modelo_class.predict(preds)
            prediccion_modelo=round(float(prediccion_modelo),2)
            if(prediccion_modelo == 1.0):
                prediccion_modelo="1"
            else:
                prediccion_modelo="0"
        except ValueError:
            return "Ingrese valores validos"
        return render_template('prediccion.html', prediccion=prediccion_modelo)

if __name__ =='__main__':
    app.run(debug=True)
