import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis_result = None
    if request.method == 'POST':
        product = request.form.get('product')
        price = request.form.get('price')
        
        if product and price:
            try:
                # Basic analysis logic
                p = int(price)
                advice = "Good price point!" if p < 1000 else "High-end product strategy needed."
                analysis_result = {
                    "status": "Success",
                    "product": product,
                    "price": price,
                    "advice": advice
                }
            except Exception as e:
                analysis_result = {"status": "Error", "message": "Please enter a valid number."}
        
    return render_template('index.html', result=analysis_result)

if __name__ == '__main__':
    # Render ke liye ye settings zaroori hain
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
