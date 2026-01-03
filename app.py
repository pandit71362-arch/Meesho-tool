import os
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    # HEAD request handle karne ke liye (errors se bachne ke liye)
    if request.method == 'HEAD':
        return make_response('', 200)

    analysis_result = None
    if request.method == 'POST':
        product = request.form.get('product')
        price = request.form.get('price')
        
        if product and price:
            try:
                # Price ko number mein badalna
                p = float(price) 
                advice = "Good price point!" if p < 1000 else "High-end product strategy needed."
                analysis_result = {
                    "status": "Success",
                    "product": product,
                    "price": price,
                    "advice": advice
                }
            except ValueError:
                analysis_result = {"status": "Error", "message": "Please enter a valid number for price."}
        
    return render_template('index.html', result=analysis_result)

if __name__ == '__main__':
    # 'appo' ko 'app' se fix kiya gaya hai
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
