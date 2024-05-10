from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    content = request.form.get('content')  # Obtém o conteúdo do formulário
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Salva a imagem temporariamente
    img_path = 'qrcode.png'
    img.save(img_path)

    # Retorna a imagem para download
    return send_file(img_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
