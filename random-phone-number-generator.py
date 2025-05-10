import random

operator_code = [532,533,534,535,536,537,538,539,541,542,543,544,545,546,547,548,549,501,502,503,504,505,506,507,551,552,553,554,555,556,508]



def random_generator(creation_time,country_code,operator_code):
    for i in range(creation_time):
        remaining_numbers = []
        for j in range(7):
            sayi = random.randint(0,9)
            remaining_numbers.append(sayi)
        print(str(country_code)+ str(random.choice(operator_code))+ ''.join(str(sayi) for sayi in remaining_numbers))


creation_time = int(input("Ne kadar sayıda numara oluşturulsun?"))
country_code = input("Numaralar ne ile başlayacak? Ülke kodu girin veya 0 bırakın.")
random_generator(creation_time,country_code,operator_code)
print(f"{creation_time} tane numara oluşturuldu!")