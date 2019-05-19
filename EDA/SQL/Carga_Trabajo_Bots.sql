Select 
COUNT(DISTINCT(VEHICULO)) BOTS,
COUNT(1) Operaciones,
convert(date, fecha, 103) fecha,
MONTH(FECHA) Mes,
DATEPART(dw, fecha) dia_semana,
CONVERT(VARCHAR(2), Fecha, 108) hora
from SISTEMA_BMS_ORDENES 
WHERE FECHA >='2017/01/10'
GROUP BY 
convert(date, fecha, 103),
DATEPART(dw, fecha),
MONTH(FECHA),
CONVERT(VARCHAR(2), Fecha, 108)
order by fecha,hora;