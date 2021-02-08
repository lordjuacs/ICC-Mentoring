binacional = {"17/02/2019":"G" , "24/02/2019":"G",
            "03/03/2019":"P" , "10/03/2019":"G" , "17/03/2019":"G" ,
            "24/03/2019":"E" , "31/03/2019":"P" , "07/04/2019":"G" ,
            "14/04/2019":"G" , "21/04/2019":"G" , "28/04/2019":"G" ,
            "05/05/2019":"G" , "12/05/2019":"E" , "19/05/2019":"P" ,
            "26/05/2019":"G" , "02/06/2019":"G" }
# 1
binacional["09/06/2019"] = "G"
# 2
resumen = list(binacional.values())
dic_resumen = {"G": 0, "E": 0, "P": 0}
dic_resumen["G"] = resumen.count("G")
dic_resumen["E"] = resumen.count("E")
dic_resumen["P"] = resumen.count("P")
for i in dic_resumen:
    print(i + ":", dic_resumen[i])
#3
print("Puntaje total:", dic_resumen["G"] * 3 + dic_resumen["E"])