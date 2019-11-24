import csv

import_file_name = 'Nov22_orders_export.csv'
export_file_name = 'wms_import.txt'
timestamp = '2019.11.23'

def txt_writer(row):
    with open (f"{timestamp}.{export_file_name}", 'a') as f:
        line = ''
        for value in row:
            line += f"{value}\t"
        line += '\n'
        f.write(line) 

def checkNumData(item):
    return ''.join([char for char in item if char.isdigit()])
    
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
with open(import_file_name, 'r') as f:
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

        line = [ReferenceNumber, PurchaseOrderNumber, ShipCarrier, ShipService, ShipBilling, ShipAccount, ShipDate, CancelDate, Notes, ShipToName, ShipToCompany, ShipToAddress1, ShipToAddress2, ShipToCity, ShipToState, ShipToZip, ShipToCountry, ShipToPhone, ShipToFax, ShipToEmail, ShipToCustomerID, ShipToDeptNumber, RetailerID, Sku, Quantity, UseCOD, UseInsuranceSavedElements, LineItemSavedElements, Carrier, Notes]
        txt_writer(line)
