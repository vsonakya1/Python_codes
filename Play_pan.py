
import pandas


class Main_class:
    def tables():
        x= int(input("Please enter a number: "))

        for i in range (1,11):
            print(x ," X ", i ," = ", x*i)


    def Temp_convert():        
        conversion_factor = int(input("please enter conversion factor for\n Fahrenheit to Centigrade enter 1\n Centigrade to Fahrenheit enter 2\n"))

        if conversion_factor ==1:
            x= int(input("please enter temp in Fahrenheit : "))
            return str(round((5/9)*(x-32))) +" Centigrade"
        elif conversion_factor ==2:
            x= int(input("please enter temp in Centigrade : "))
            return str(round((x*(9/5))+32)) +" Fahrenheit"
    def length_conversion():
        conversion_factor = int(input("please enter conversion factor for\n miles to kilomerter enter 1\n Centigrade to Fahrenheit enter 2\n"))
        
