from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo de motos en stock
motos = [
    {"id": 1, "marca": "Yamaha", "modelo": "MT-07", "precio": 8500, "color": "Azul", "cilindrada": "700cc"},
    {"id": 2, "marca": "Honda", "modelo": "CBR600RR", "precio": 12000, "color": "Rojo", "cilindrada": "600cc"},
    {"id": 3, "marca": "Kawasaki", "modelo": "Ninja 400", "precio": 5000, "color": "Verde", "cilindrada": "400cc"},
    {"id": 4, "marca": "Suzuki", "modelo": "GSX-R750", "precio": 11000, "color": "Blanco", "cilindrada": "750cc"},
]

@app.route('/')
def index():
    return render_template('index.html', motos=motos)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")