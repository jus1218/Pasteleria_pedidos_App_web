
from ast import If
from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME'] = 'CarmenPasteleria.SA@gmail.com'
app.config['MAIL_PASSWORD'] = 'Paste1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


# Rutas
@app.route('/')
def principal():
   return  render_template('index.html')
   
@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/form',methods =['POST','GET'])
def obtener():
   output = request.form.to_dict()
   name =output["name"]
   tel = output["tel"]
   direccion = output["direccion"]
   correo = output["correo"]
   retiro = output["retiro"]
   eventos = output["eventos"]
   cantidad = output["cantidad"]
   sabores = output["sabores"]
   lutres = output["lutres"]
   tamano = output["tamano"]
   forma = output["forma"]
   adicional = output["adicional"]
   precio = 0
   
  

   if sabores == "chocolate":
      precio += 1000
   else:
      precio += 500
   
   if lutres == "fondant":
      precio += 1000
   else:
      precio += 500

   if tamano == "grande":
      precio += 1500
   elif  tamano == "mediano":
      precio += 1000
   else:
      precio += 500

   if forma == "rectangulo":
      precio += 1500
   elif  forma == "cuadrado":
      precio += 1000
   else:
      precio += 500

   if adicional != "":
      precio += 500

   if int(cantidad) > 1:
      precio = precio * int(cantidad)


   if request.method == 'POST':
      msg =Message("Pedido!!",sender='CarmenPasteleria.SA@gmail.com',recipients=[correo])
      msg.body = "<<< DATOS DEL PEDIDO >>>\nNombre: "+ name +"\nTelefono: "+ tel +"\nDireccion: "+ direccion +"\nCorreo: "+correo+"\nFecha de retiro: "+retiro+"\nEvento: "+eventos+"\nCantidad de Queques: "+cantidad+"\nSabor: "+sabores+"\nLustre: "+lutres+"\nTamaño: "+tamano+"\nForma: "+forma+"\nAdicional: "+adicional+"\nPRECIO ESTIMADO: ₡"+str(precio)+"\n\t\t\tMuchas gracias por su preferencia"
      mail.send(msg)
      return render_template('form.html',name = "pedido creado exitosamente")
   return render_template('form.html',name = "pedido creado exitosamente")

@app.route('/mensaje')
def mensaje():
   return render_template('mensaje.html')





if __name__ == '__main__':
    app.run(debug=True)