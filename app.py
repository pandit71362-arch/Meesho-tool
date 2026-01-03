import os
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis_result = None
    if request.method == 'POST':
        product = request.form.get('product')
        price = request.form.get('price')
        
        # Simple Logic for Analysis
        if product and price:
            try:
                price_val = int(price)
                if price_val < 500:
                    advice = "Low competition segment. Good for high volume."
                else:
                    advice = "Premium segment. Focus on branding and ads."
                
                analysis_result = {
                    "status": "Success",
                    "product": product,
                    "price": price,
                    "market_trend": "Rising",
                    "advice": advice
                }
            except:
                analysis_result = {"status": "Error", "message": "Invalid price entered."}
        
    return render_template('index.html', result=analysis_result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
