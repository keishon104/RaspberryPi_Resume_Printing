# Author: Keishon Smith
# Date: January 10, 2019
# Purpose: USE CUPS to print a document with a specified path.
def printDocument(printerName,filePath,copies):
    import cups
    # TEST_DOCUMENT = '/home/pi/Documents/paperfairy/documents/DOC083118-08312018163618.pdf'
    # PRINTER_NAME = 'Brother_HL-L3270CDW_series'
    copies = '5'
    conn = cups.Connection ()
    printers = conn.getPrinters ()
    # Uncomment the loop below to display all printers that are available.
    # for printer in printers:
    #     print printer, printers[printer]["device-uri"]
    # conn.printFile('Brother_HL-L3270CDW_series', DOCUMENT, "Test_Print",{"copies": "1"})
    conn.printFile(printerName, filePath, "Test_Print",{"copies": copies})

    print('The printer works')

# printDocument(PRINTER_NAME, DOCUMENT, copies)
