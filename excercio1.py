def temperatura (temperatura, origem, destino):
   if origem =='C' and destino =='F':
      return [(tempo*9/5)+32 for tempo in temperatura]
   elif origem =='F' and destino=='C': 
       return [(tempo -32)*5/9 for tempo in temperaturas]
   else:
     return"escala invalida"
celsius=[0,25,100]
fahrenheit=temperatura(celsius, 'C','F')
print(fahrenheit)