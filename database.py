from flask import Flask, request, jsonify
import pyodbc
from datetime import datetime
import traceback

app = Flask(__name__)

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER = {ODBC Driver 17 for SQL Server};'
            'SERVER = .\SQLEXPRESS;'
            'DATABASE=NovaAkademi;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print (f"Veri tabanı bağlantı hatası: {e}")
        return None

@app.route('/add-book', methods=['POST'])
def add_book():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.json
        print(f"Alınan veri: {data}")  # Debug için alınan veriyi yazdırıyoruz.

        YazarID = data.get('YazarID')
        Baslik = data.get('Başlık')
        yayin_yili_str = data.get('YayınYılı')

        if YazarID is None or Baslik is None or yayin_yili_str is None:
            return jsonify({"error": "Eksik veri: YazarID, Başlık ve YayınYılı gerekli."}), 400

        # Yayın yılını doğrulama ve formatlama
        try:
            yayin_yili = datetime.strptime(yayin_yili_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error":"YayınYılı geçersiz formatta. Format: YYYY-MM-DD"}), 400

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dbo.Kitaplar (YazarID, Başlık, YayınYılı) VALUES (?,?,?)",
            (YazarID, Baslik, yayin_yili)
        )
        conn.commit()

        return jsonify({"message":"Kitap başarıyla eklendi."}), 201

    except pyodbc.Error as e:
        # Hata detaylarını loglama
        print("Hata:", e)
        print ("Traceback:", traceback.format_exc())
        return jsonify({"error":"Veritabanı hatası: {e}"}), 500

    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)