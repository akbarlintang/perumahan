import mysql.connector
from openpyxl import Workbook

def main():

    # Connect to DB -----------------------------------------------------------
    db = mysql.connector.connect( user='root', password='', host='127.0.0.1:8080')
    cur = db.cursor()

    database = 'perum'

    SQL = 'USE ' + database + ';'

    # Create Excel (.xlsx) file -----------------------------------------------
    wb = Workbook()

    SQL = 'SELECT no_unit, tipe_unit, nama_lok, status_rumah FROM perum_unit INNER JOIN perum_lokasi on perum_unit.lokasi_id=perum_lokasi.id INNER JOIN perum_tipe on perum_unit.tipe_id=perum_tipe.id WHERE status_rumah='Tersedia';'
    cur.execute(SQL)
    results = cur.fetchall()
    ws = wb.create_sheet(0)
    ws.title = cars_table_name
    ws.append(cur.column_names)
    for row in results:
        ws.append(row)

    workbook_name = "test_workbook"
    wb.save(workbook_name + ".xlsx")

if  __name__ =='__main__':main() 