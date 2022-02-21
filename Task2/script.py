import job1
import job2
from datetime import date,timedelta
today1 = date.today()
co2_data = False
while co2_data==False:
    co2_data = job1.getCO2(str(today1))
    today1 = today1 - timedelta(days=1)
today2 = date.today()
fx_data = False
while fx_data==False:
   fx_data= job2.getFX("GBP",str(today2))
#    today = today - timedelta(days=1)

print('''The cycle CO2 is {cycle}, trend CO2 is {trend} as on date {date1} and 
        Foreign Exchange rates for GBP to USD is {fx} as on date {date2}
        '''.format(cycle=co2_data["cycle"], trend=co2_data["trend"], fx=fx_data, date1=today1, date2=today2))
# print(co2_data)
# print(fx_data)