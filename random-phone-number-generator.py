"""
operator_code: Phone number prefixes of mobile operators. The ones listed here are valid for Turkey.
country_code: Country code. Enter +90 for Turkey, or enter 0 if you want the numbers to start with 0.
create_time: Enter how many phone numbers you want to generate.
"""
"""
operator_code : Mobil operatörlerin telefon numaraları. Buradakiler Türkiye için geçerlidir.
country_code : Ülke kodu. Türkiye için +90 yazın 0 ile başlamasını isterseniz 0 yazın.
create_time: Kaç tane numara oluşturmak istiyorsanız buraya girin.
"""
import random

operator_code = [532,533,534,535,536,537,538,539,541,542,543,544,545,546,547,548,549,501,502,503,504,505,506,507,551,552,553,554,555,556,508] 




def random_generator(create_no,country_code,operator_code):
    for i in range(create_no):
        remaining_numbers = []
        for j in range(7):
            sayi = random.randint(0,9)
            remaining_numbers.append(sayi)
        print(str(country_code)+ str(random.choice(operator_code))+ ''.join(str(sayi) for sayi in remaining_numbers))


create_no = int(input("Ne kadar sayıda numara oluşturulsun?"))
country_code = input("Numaralar ne ile başlayacak? Ülke kodu girin veya 0 bırakın.")
random_generator(create_no,country_code,operator_code)
print(f"{create_no} tane numara oluşturuldu!")
