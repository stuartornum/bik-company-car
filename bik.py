#!/usr/bin/env python

from flask import Flask, render_template, request


def get_bik_rate(co2, fuel):
    f = open('rates.csv')
    bik_rates = []
    for i in f.readlines():
        bik_rates.append(i.strip().split(','))

    petrol = None
    diesel = None
    for i in xrange(0, len(bik_rates)):
        if co2 < int(bik_rates[i][0]):
            petrol = bik_rates[i-1][1]
            diesel = bik_rates[i-1][2]
            break

    if fuel == 'petrol':
        return float('0.{0}'.format(petrol))
    else:
        return float('0.{0}'.format(diesel))



app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        p11d = int(request.form['p11d'])
        co2 = int(request.form['co2'])
        fuel = request.form['fuel']
        tax = float(request.form['tax'])
        bik_percentage = get_bik_rate(co2, fuel)
        data = {
            'bik_pc': bik_percentage * 100,
            'p11d': p11d,
            'co2': co2,
            'fuel': fuel,
            'tax': tax * 100,
            'bik': p11d * bik_percentage,
            'tax_cost': (p11d * bik_percentage) * tax
        }
        return render_template('index.html', data=data)
    else:
        data = {}
        return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

