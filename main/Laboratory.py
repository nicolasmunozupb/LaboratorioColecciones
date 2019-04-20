import statistics as stats
#Promedio temperatura cada departamento
def prom_temperature(temperature_department_list):
    temperature_sum=0
    temperature_quantity=len(temperature_department_list)

    for prom in temperature_department_list:
        temperature_sum +=prom

        final_prom=temperature_sum/temperature_quantity

        return final_prom

#Mes mas caliente de cada departamento
def high_temperature(temperature_department_list):
    high_temperature=temperature_department_list[0]
    month=[]

    for temperature in temperature_department_list:
        if temperature>high_temperature

        position=temperature_department_list.index(high_temperature)
        if position==0:
            month.append("january")
        else:
            if position==1:
                month.append("february")
            else:
                if position==2:
                    month.append("march")
                else:
                    if position==3:
                        month.append("april")
                    else:
                        if position==4:
                            month.append("may")
                        else:
                            if position==5:
                                month.append("june")
                            else:
                                if position==6:
                                    month.append("july")
                                else:
                                    if position==7:
                                        month.append("august")
                                    else:
                                        if position==8:
                                            month.append("september")
                                        else:
                                            if position==9:
                                                month.append("october")
                                            else:
                                                if position==10:
                                                    month.append("november")
                                                else:
                                                    if position==11:
                                                        month.append("december")
return month

#mes mas caliente de los departamentos
def hot_prom(temperature_department_list):
    hot_prom=temperature_department_list[0]

    for temperature in temperature_department_list:
        if temperature>hot_prom:
            hot_prom=temperature
return hot_prom

'''''
Solucion Laboratorio
'''

santanderstemperature_list=[]
print("please enter the temperatures of department of santander")
for i in range(0, 12):
    temperature=int(input("give me the temperature of month {} ".format(i+1)))
santanderstemperature_list.append(temperature)

santander_prom=prom_temperature(santanderstemperature_list)
santader_hig_temperature=high_temperature(santanderstemperature_list)
print("the average temperature of department of santander is: {} ".format(santander_prom))
print("the hot temperature was".format(santander_high_temperature))

santander_high_temperature=high_temperature(santanderstemperature_list)
standard_deviation_santander=(stats.pstdev(santanderstemperature_list))
print("deviation=", standard_deviation_santander)

print("------------------------------GUAJIRA------------------------------")
#departamento de la guajira

guajirastemperature_list=[]
print("please enter the temperatures of department of guajira")
for i in range(0, 12):
    temperature=int(input ("give me the temperature of the month {} ".format (guajirastemperature_list)

guajiras_prom=prom_temperature(guajirastemperature_list)
guajiras_high_temperature=high_temperature(guajirastemperature_list)
print("the average temperature of the department of guajira is: {} ".format(guajirastemperature_list))
print("hot temperature was: {} ".format(guajiras_high_temperature))

temp_high_guajira=high_temperature(guajirastemperature_list)
standard_deviation_guajira=(stats.pstdev(guajirastemperature_list))
print("deviation=", standard_deviation_guajira)

print("------------------------------Nariño------------------------------")
#Departamento de nariño

nariñostemperature_list=[]
print("please enter the temperatures of department of nariño")
for i in range(0, 12):
        temperature=int(input ("give me the temperature of the month {} ".format (nariñostemperature_list)
print("the average temperature of the department of nariños is: {} ".format(nariñostemperature_list))
print("hot temperature was: {} ".format(nariñostemperature_list))

nariño_prom=prom_temperature(nariñostemperature_list)
nariño_high_temperature=high_temperature(nariñostemperature_list)
standard_deviation_nariño=(stats.pstdev(nariñostemperature_list))
print("deviation=", standard_deviation_nariño)

print("------------------------------National------------------------------")

national_prom=(santander_prom+nariño_prom+guajiras_prom)/3
national_high_temperature=(santander_high_temperature+guajiras_high_temperature+nariño_hig)

print("the average of the highest temperature is: ", national_high_temperature)
print("the average of national temperature is: ", national_prom)

highertemperature_list=[santander_prom,guajiras_prom,nariño_prom]

hottest=hottest_averagae(highertemperature_list)
print("the hottests average is: ", hottests)

#temperatura mas caliente en todo el año y en que departamento y mes

if santander_high_temperature>guajiras_high_temperature and santander_high_temperature>nariño_high_temperature:
    print("the warmest temperature that ocurred troughout in the year was {} °C, was presented in the month {} in the department of santander".format(santander_high_temperature,santander_high_temperature ))
else:
    if guajiras_high_temperature>santander_high_temperature and guajiras_high_temperature>nariño_high_temperature:
        print("the warmest temperature that ocurred troughout in the year was {} °C, was presented in the month {} in the department of guajira".format(guajiras_high_temperature,guajiras_high_temperature ))
    else:
        if nariño_high_temperature>santander_high_temperature and nariño_high_temperature>guajiras_high_temperature:
            print("the warmest temperature that ocurred troughout in the year was {} °C, was presented in the month {} in the department of nariño".format(nariño_high_temperature,nariño_high_temperature ))

#desviacion estandar
print("------------------------------Standard Deviation------------------------------")

print("standard deviation of santander=", standard_deviation_santander)
print("standard deviation of guajira=", standard_deviation_guajira)
print("standard deviation of nariño=", standard_deviation_nariño)























print("THANKS FOR WHATCHING MY VIDEO <3")

#ATT Nicolas Muñoz :D


print("the hottest average is: ",hottest)

#cual fue la temperatura mas caliente en todo el año, en que mes se prensento y en que departamento

if temp_high_santander>temp_high_guajira and temp_high_santander>temp_high_nariño:
	print("The warmest temperature that occurred throughout the year was {} ° C, was presented in the month of {} in the department of Santander".format(temp_high_santander,santander_high_temperature))
else:
	if temp_high_guajira>temp_high_santander and temp_high_guajira>temp_high_nariño:
		print("The warmest temperature that occurred throughout the year was {} ° C, was presented in the month of {} in the department of guajira".format(temp_high_narinno,guajira_high_temperature))
	else:
		if temp_high_nariño>temp_high_santander and temp_high_nariño>temp_high_guajira:
			print("The warmest temperature that occurred throughout the year was {} ° C, was presented in the month of {} in the department of nariño".format(temp_high_guajira,nariño_high_temperature))



#Desviacion estandar de los tres departamentos

print("Standart deviation of Santander=",standard_deviation_santander)

print("Standart deviation of Guajira=",standard_deviation_guajira)

print("Standart deviation of Nariño=",standard_deviation_nariño)
