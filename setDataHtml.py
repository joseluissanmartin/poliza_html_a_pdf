# This Python file uses the following encoding: utf-8
import json
import os

import pdfkit

with open("jsonEnviado.json", "r") as d:
    jsonEnviado = json.load(d)



def setDataHtml(nombre, rut, fecha_nacimiento, edad_Contratante, telefono_Contratante, email_Contratante,
                domicilio_Contratante, comuna_Contratante, saludPrevisional_Contratante, formaPago_Contratante,
                banco_Contratante, tipoCuenta_Contratante, numeroCuenta_Contratante, periodicidad_Pago,
                plan_Seleccionado, numero_De_Asegurados, tablaTotalMensualPorPagar_primaNetaTotal,
                tablaTotalMensualPorPagar_primaBrutaTotal, tablaTotalMensualPorPagar_iva, Rut_dependiente,
                fecha_nacimiento_dependiente, fecha_nacimiento_dependiente2, Institucion_salud_dependiente,
                Institucion_salud_dependiente2, relacion_dependiente, relacion_dependiente2, preexistencias,
                preexistencias_2, nombreCarga_dependiente, nombreCarga_dependiente2):

    template = "/html/poliza_standar.html"

    with open(os.path.dirname(os.path.abspath(__file__)) + template, 'r', encoding='utf-8') as f:
        datos_format = f.read()

        # datos_format = datos_format.replace("[nombre_del_contratante]", str(nombre))
        # datos_format = datos_format.replace("[rut_del_contratante]", str(rut))
        # datos_format = datos_format.replace("[fecha_nacimiento_contratante]", str(fecha_nacimiento))
        # datos_format = datos_format.replace("[edad_Contratante]", str(edad_Contratante))
        # datos_format = datos_format.replace("[telefono_Contratante]", str(telefono_Contratante))
        # datos_format = datos_format.replace("[email_Contratante]", str(email_Contratante))
        # datos_format = datos_format.replace("[domicilio_Contratante]", str(domicilio_Contratante))
        # datos_format = datos_format.replace("[comuna_Contratante]", str(comuna_Contratante))
        # datos_format = datos_format.replace("[saludPrevisional_Contratante]", str(saludPrevisional_Contratante))
        # datos_format = datos_format.replace("[formaPago_Contratante]", str(formaPago_Contratante))
        # datos_format = datos_format.replace("[banco_Contratante]", str(banco_Contratante))
        # datos_format = datos_format.replace("[tipoCuenta_Contratante]", str(tipoCuenta_Contratante))
        # datos_format = datos_format.replace("[numeroCuenta_Contratante]", str(numeroCuenta_Contratante))
        # datos_format = datos_format.replace("[periodicidad_Pago]", str(periodicidad_Pago))
        # datos_format = datos_format.replace("[plan_Seleccionado]", str(plan_Seleccionado))
        # datos_format = datos_format.replace("[numero_De_Asegurados]", str(numero_De_Asegurados))
        # datos_format = datos_format.replace("[tablaTotalMensualPorPagar_primaNetaTotal]", str(tablaTotalMensualPorPagar_primaNetaTotal))
        # datos_format = datos_format.replace("[tablaTotalMensualPorPagar_primaBrutaTotal]", str(tablaTotalMensualPorPagar_primaBrutaTotal))
        # datos_format = datos_format.replace("[tablaTotalMensualPorPagar_iva]", str(tablaTotalMensualPorPagar_iva))
        # datos_format = datos_format.replace("[nombreCarga_dependiente]", str(nombreCarga_dependiente))
        # datos_format = datos_format.replace("[Rut_dependiente]", str(Rut_dependiente))
        # datos_format = datos_format.replace("[fecha_nacimiento_dependiente]", str(fecha_nacimiento_dependiente))
        # datos_format = datos_format.replace("[Institucion_salud_dependiente]", str(Institucion_salud_dependiente))
        # datos_format = datos_format.replace("[relacion_dependiente]", str(relacion_dependiente))
        # datos_format = datos_format.replace("[nombreCarga_dependiente2]", str(nombreCarga_dependiente2))
        # datos_format = datos_format.replace("[fecha_nacimiento_dependiente2]", str(fecha_nacimiento_dependiente2))
        # datos_format = datos_format.replace("[Institucion_salud_dependiente2]", str(Institucion_salud_dependiente2))
        # datos_format = datos_format.replace("[relacion_dependiente2]", str(relacion_dependiente2))
        # datos_format = datos_format.replace("[preexistencias]", str(preexistencias))
        # datos_format = datos_format.replace("[preexistencias_2]", str(preexistencias_2))

    return datos_format




nombre = jsonEnviado['nombre']
rut = jsonEnviado['rut']
fecha_nacimiento = jsonEnviado['fecha de nacimiento']
edad_Contratante = jsonEnviado['edad']
telefono_Contratante = jsonEnviado['telefono']
email_Contratante = jsonEnviado['correo electronico']
domicilio_Contratante = jsonEnviado['domicilio']
comuna_Contratante = jsonEnviado['comuna']
saludPrevisional_Contratante = jsonEnviado['sistema de salud previsional']
formaPago_Contratante = jsonEnviado['forma de pago reembolso']
banco_Contratante = jsonEnviado['banco']
tipoCuenta_Contratante = jsonEnviado['tipo de cuenta']
numeroCuenta_Contratante = jsonEnviado['numero de cuenta']
periodicidad_Pago = jsonEnviado['periodicidad de pago']
plan_Seleccionado = jsonEnviado['plan seleccionado']
numero_De_Asegurados = jsonEnviado['numero de asegurados']
tablaTotalMensualPorPagar_primaNetaTotal = jsonEnviado['primaNetaTotal']
tablaTotalMensualPorPagar_primaBrutaTotal = jsonEnviado['primaBrutaToltal']
tablaTotalMensualPorPagar_iva = jsonEnviado['iva']
nombreCarga_dependiente = jsonEnviado['tabla asegurados dependientes'][0]['nombreCarga']+" "+jsonEnviado['tabla asegurados dependientes'][0]['apellidoPaternoCarga']+" "+jsonEnviado['tabla asegurados dependientes'][0]['apellidoMaternoCarga']
nombreCarga_dependiente2 = jsonEnviado['tabla asegurados dependientes'][0]['nombreCarga']+" "+jsonEnviado['tabla asegurados dependientes'][0]['apellidoPaternoCarga']+" "+jsonEnviado['tabla asegurados dependientes'][0]['apellidoMaternoCarga'] #TODO: revisar como tomar los segundos valores
Rut_dependiente = str(jsonEnviado['tabla asegurados dependientes'][0]["rutCarga"])+"-"+jsonEnviado["tabla asegurados dependientes"][0]["cargaDv"]
fecha_nacimiento_dependiente = jsonEnviado['tabla asegurados dependientes'][0]['fechaNacimientoCarga']
fecha_nacimiento_dependiente2 = jsonEnviado['tabla asegurados dependientes'][0]['fechaNacimientoCarga']
Institucion_salud_dependiente = jsonEnviado['tabla asegurados dependientes'][0]['institucionSaludCarga']
Institucion_salud_dependiente2 = jsonEnviado['tabla asegurados dependientes'][0]['institucionSaludCarga']
relacion_dependiente = jsonEnviado['tabla asegurados dependientes'][0]['relacionCarga']
relacion_dependiente2 = jsonEnviado['tabla asegurados dependientes'][0]['relacionCarga']
preexistencias = jsonEnviado['tabla asegurados dependientes'][0]['preexistencias'][0]['diagnosticoAltaCarga']
preexistencias_2 = jsonEnviado['tabla asegurados dependientes'][0]['preexistencias'][0]['diagnosticoAltaCarga']

htmlTerminado = setDataHtml(nombre, rut, fecha_nacimiento, edad_Contratante, telefono_Contratante, email_Contratante,
                domicilio_Contratante, comuna_Contratante, saludPrevisional_Contratante, formaPago_Contratante,
                banco_Contratante, tipoCuenta_Contratante, numeroCuenta_Contratante, periodicidad_Pago,
                plan_Seleccionado, numero_De_Asegurados, tablaTotalMensualPorPagar_primaNetaTotal,
                tablaTotalMensualPorPagar_primaBrutaTotal, tablaTotalMensualPorPagar_iva, Rut_dependiente,
                fecha_nacimiento_dependiente, fecha_nacimiento_dependiente2, Institucion_salud_dependiente,
                Institucion_salud_dependiente2, relacion_dependiente, relacion_dependiente2, preexistencias,
                preexistencias_2, nombreCarga_dependiente, nombreCarga_dependiente2)

#print(htmlTerminado)

#encodedBytes = base64.b64encode(htmlTerminado.encode("utf-8"))
#encodedStr = str(encodedBytes, "utf-8")
#print(encodedStr)

options = {
    'page-size' : 'Letter',
    "margin-right":15,
    "margin-left":15,
    "minimum-font-size":18
}
#config = pdfkit.configuration(wkhtmltopdf="binary/wkhtmltopdf")
pdfkit.from_string(htmlTerminado, 'demo.pdf' ,options=options)