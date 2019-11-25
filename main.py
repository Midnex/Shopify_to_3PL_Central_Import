import csv
from datetime import datetime
import PySimpleGUI as sg

# CONFIG
stamp = datetime.now().strftime('%Y%m%d')
export_file_name = f"order_import_{stamp}.txt"

def main():
    layout = [
        [sg.Text('Shopify to 3PL Central Order Converter', size=(0,1), font=('Calibri',16))], 
        [sg.Text('Select Shopify CSV file: ', size=(30,1))],
        [sg.In(disabled=True), sg.FileBrowse(file_types=(('CSV Files', 'csv'),))],
        [sg.Text('File to Export:', size=(30,1))], 
        [sg.In(default_text=export_file_name ,disabled = True), sg.Submit(button_text='Convert',bind_return_key=True)],
        [sg.Text('https://github.com/Midnex/Shopify_to_3PL_Central_Import', size=(0,1), font=('Calibri', 8))]
    ]

    window = sg.Window('Shopify to 3PL Central Order Converter').Layout(layout)
    convert_button, values = window.Read()
    if convert_button == 'Convert':
        convert(values[0])
        sg.Popup(convert_button, 'File Converted')


def txt_writer(row):
    ''' defaults to tab-delimited'''
    with open(export_file_name, 'a') as f:
        line = ''
        for value in row:
            line += f"{value}\t"
        line += '\n'
        f.write(line) 


def checkNumData(item):
    return ''.join([char for char in item if char.isdigit()])

def convert(file):
    ReferenceNumber = ''
    PurchaseOrderNumber = ''
    ShipCarrier = ''
    ShipService = ''
    ShipBilling = ''
    ShipAccount = ''
    ShipDate = ''
    CancelDate = ''
    Notes = ''
    ShipToName = ''
    ShipToCompany = ''
    ShipToAddress1 = ''
    ShipToAddress2 = ''
    ShipToCity = ''
    ShipToState = ''
    ShipToZip = ''
    ShipToCountry = ''
    ShipToPhone = ''
    ShipToFax = ''
    ShipToEmail = ''
    ShipToCustomerID = ''
    ShipToDeptNumber = ''
    RetailerID = ''
    Sku = ''
    Quantity = ''
    UseCOD = ''
    UseInsuranceSavedElements = ''
    LineItemSavedElements = ''
    Carrier = ''
    Notes = ''

    dataList = []
    with open(file, 'r') as f:
        data = csv.DictReader(f)
        for i in data:
            dataList.append([i])


    for ordDict in dataList:
        for row in ordDict:
            ReferenceNumber = row['Name'].replace('#','')
            PurchaseOrderNumber = ''
            if 'Priority Mail' == row['Shipping Method']:
                ShipCarrier = 'USPS'
                ShipService = 'Priority Mail'
            elif 'Standard Shipping' in row['Shipping Method']:
                ShipCarrier = 'USPS'
                ShipService = 'Standard Shipping'
            elif 'Â® ' in row['Shipping Method']:
                ShipCarrier = row['Shipping Method'].split('Â® ')[0]
                ShipService = row['Shipping Method'].split('Â® ')[1]
            ShipBilling = 'Prepaid'
            ShipAccount = ''
            ShipDate = ''
            CancelDate = ''
            Notes = ''
            ShipToName = row['Billing Name']
            ShipToCompany = row['Shipping Company']
            ShipToAddress1 = row['Shipping Address1']
            ShipToAddress2 = row['Shipping Address2']
            ShipToCity = row['Shipping City']
            ShipToState = row['Shipping Province']
            ShipToZip = checkNumData(row['Shipping Zip'])
            ShipToCountry = row['Shipping Country']
            ShipToPhone = checkNumData(row['Shipping Phone'])
            ShipToFax = ''
            ShipToEmail = row['Email']
            ShipToCustomerID = ''
            ShipToDeptNumber = ''
            RetailerID = ''
            Sku = row['Lineitem sku']
            Quantity = row['Lineitem quantity']
            UseCOD = ''
            UseInsuranceSavedElements = ''
            LineItemSavedElements = ''
            Carrier = ''
            Notes = row['Notes']

            line = [
                ReferenceNumber, 
                PurchaseOrderNumber, 
                ShipCarrier, 
                ShipService, 
                ShipBilling, 
                ShipAccount, 
                ShipDate, 
                CancelDate, 
                Notes, 
                ShipToName, 
                ShipToCompany, 
                ShipToAddress1, 
                ShipToAddress2, 
                ShipToCity, 
                ShipToState, 
                ShipToZip, 
                ShipToCountry, 
                ShipToPhone, 
                ShipToFax, 
                ShipToEmail, 
                ShipToCustomerID, 
                ShipToDeptNumber, 
                RetailerID, 
                Sku, 
                Quantity, 
                UseCOD, 
                UseInsuranceSavedElements, 
                LineItemSavedElements, 
                Carrier, 
                Notes
            ]

            txt_writer(line)

if __name__ == '__main__':
    main()
