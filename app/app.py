from datetime import datetime
hoy = datetime.now().date()
print("Se le asignó un turno para el dia: " , hoy.strftime('%d/%m/%Y'))