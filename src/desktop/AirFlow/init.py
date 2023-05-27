import PyQt5 as ui
import base64 as b64

deConfig = input("args for starting AirFlow (separated by a comma):")

def init() :
    ui.__name__("Niosem AirFlow")
    ui.__package__("niosem.airflow.linux.de.prod")
    b64.b64encode(deConfig)