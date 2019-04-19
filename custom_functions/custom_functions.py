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


