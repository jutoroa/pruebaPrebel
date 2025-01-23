import PyPDF2
from datetime import datetime
import pandas as pd

pdf_path = 'files/'

pdf_list = ['3. FAC001.pdf', '4. FAC002.pdf']

excel_path = 'files/'

excel_name = '2. BASE_DATOS_FACTURAS.xlsx'

def convert_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y").strftime("%-d/%-m/%Y")

def extract_pdf_data(file_name):

    with open(pdf_path + file_name, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    lines = text.split('\n')

    pdf_information = {
        "numero_factura": None,
        "fecha_compra": None,
        "productos": []
    }

    for line in lines:
        elements = line.split()

        if len(elements) <= 2:
            for key in pdf_information.keys():
                if key in elements:
                    pdf_information[key] = elements[-1]
        else:
            if 'codigo_producto' not in elements:
                product_info = {
                    "codigo_producto": elements[0],
                    "nombre_producto": ' '.join(elements[1:-1]),
                    "cantidad": elements[-1]
                }
                pdf_information["productos"].append(product_info)
    
    return pdf_information

def update_xlsx(pdf_list):
    df = pd.read_excel(excel_path + excel_name)
    print(df)

    for pdf in pdf_list:
        pdf_data = extract_pdf_data(pdf)

        factura = pdf_data["numero_factura"]
        fecha_compra = pdf_data["fecha_compra"]


        for product in pdf_data["productos"]:
            codigo = product["codigo_producto"]
            nombre = product["nombre_producto"]
            cantidad = product["cantidad"]

            if codigo in df["codigo_producto"].values:
                df.loc[df["codigo_producto"] == codigo, ["fecha_compra", "numero_factura"]] = [fecha_compra, factura]
            else:
                new_row = {
                    "codigo_producto": codigo,
                    "nombre_producto": nombre,
                    "cantidad": cantidad,
                    "fecha_compra": fecha_compra,
                    "numero_factura": factura
                }
                df = df.append(new_row, ignore_index=True)
    df["fecha_compra"] = df["fecha_compra"].dt.strftime("%m/%d/%Y")
    print(df)
    updated_excel_path = excel_path + "UPDATED_" + excel_name
    df.to_excel(updated_excel_path, index=False)
    print(f"Updated Excel saved to {updated_excel_path}")

update_xlsx(pdf_list)