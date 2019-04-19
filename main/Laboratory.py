import statistics as stats

#el promedio de la temperatura de cada departamento
def prom_temperature(temperature_departament_list):

    temperature_sum = 0
    temperature_quantity = len(temperature_departament_list)

    for prom in temperature_departament_list:
        temperature_sum += prom

    final_prom = temperature_sum / temperature_quantity

    return final_prom

#el mes mas caliente de cada departamento
def high_temperature(temperature_departament_list):
    high_temperature=temperature_departament_list[0]
    month=[]

    for temperature in temperature_departament_list:
        if temperature>high_temperature:
            high_temperature=temperature

            position=temperature_departament_list.index(high_temperature)
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
                            if position ==4:
                                month.append("may")
                            else:
                                if position ==5:
                                    month.append("june")
                                else:
                                    if position ==6:
                                        month.append("july")
                                    else:
                                        if position ==7:
                                            month.append("august")
                                        else:
                                            if position ==8:
                                                month.append("september")
                                            else:
                                                if position ==9:
                                                    month.append("october")
                                                else:
                                                    if position ==10:
                                                        month.append("november")
                                                    else:
                                                        if position ==11:
                                                            month.append("december")
return month


#meses mas calientes de los tres departamentos
def hot_prom(temperature_departament_list):
    hot_prom=temperature_departament_list[0]

    for temperature in temperature_departament_list:
        if temperature>hot_prom:
            hot_prom=temperature

    return hot_prom



'''''
Solucion Laboratorio
'''''


santanderstemperature_list=[]
print("please enter the temperatures of the department of santander")
for i in range(0, 12):

    temperature = int(input("give me the temperature of month  {}  ".format(i+1)))

santanderstemperature_list.append(temperature)

santander_prom=prom_temperature(santanderstemperature_list)
santander_high_temperature=(santanderstemperature_list)
print("the prom temperature of the depártment of santander is:{} ".format(santander_prom))
print("the hot temperature was".format(santander_high_temperature))

temp_high_santander=high_temperature(santanderstemperature_list)
standard_deviation_santander=(stats.pstdev(santanderstemperature_list))
print("desviacion=",standard_deviation_santander)

print("-------------------------------Guajira-------------------------------")
#departamento de la guajira


guajirasstemperature_list=[]
print("please enter the temperatures of the department of guajira")
for i in range(0, 12):

    temperature = int(input("give me the temperature of month  {}  ".format(i+1)))

guajirasstemperature_list.append(temperature)


guajiras_prom=prom_temperature(guajirasstemperature_list)
guajiras_high_temperature=(guajirasstemperature_list)
print("the prom temperature of the depártment of Guajira is:{} ".format(guajirasstemperature_list))
print("the hot temperature was".format(guajirasstemperature_list))

temp_high_guajira=high_temperature(guajirasstemperature_list)
standard_deviation_guajira=(stats.pstdev(guajirasstemperature_list))
print("desviacion=",standard_deviation_guajira)

print("-------------------------------Nariño-------------------------------")

#departamento de nariño



nariñosstemperature_list=[]
print("please enter the temperatures of the department of nariño")
for i in range(0, 12):

    temperature = int(input("give me the temperature of month  {}  ".format(i+1)))

nariñosstemperature_list.append(temperature)

nariño_prom=prom_temperature(nariñosstemperature_list)
nariños_high_temperature=(nariñosstemperature_list)
print("the prom temperature of the depártment of Guajira is:{} ".format(nariñosstemperature_list))
print("the hot temperature was".format(nariñosstemperature_list))

temp_high_nariño=high_temperature(nariñosstemperature_list)
standard_deviation_nariño=(stats.pstdev(nariñosstemperature_list))
print("desviacion=",standard_deviation_nariño)

print("-------------------------------NATIONAL-------------------------------")


national_prom=(santanders_prom+nariño_prom+guajiras_prom)/3
national_high_temperature=(santanders_high_temperature+guajiras_high_temperature+nariños_high_temperature)/3

print("The average of the highest temperatures is: ",national_high_temperature)
print("the average national temperature is: ",national_average)

highertemperature_list=[santanders_prom,guajiras_prom,nariño_prom]

hottest=hottest_average(highertemperature_list)

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
