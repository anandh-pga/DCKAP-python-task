ones = ['', 'one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen', 'eighteen', 'nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = ['', 'hundred','2hundred','3hundred','4hundred','5hundred','6hundred','7hundred','8hundred', '9hundred']
thousands =  ['', 'thousands', '2thousands', '3thousands', '4thousands', '5thousands', '6thousands', '7thousands', '8thousands','9thousands',]
lakhs = ['', '10thousands', '20thousands', '30thousands', '40thousands', '50thousands', '60thousands', '70thousands', '80thousands','90thousands',]
lakhs_10 = ['', '1lakhs', '2lakhs', '3lakhs', '4lakhs', '5lakhs', '6lakhs', '7lakhs', '0thousands','9lakhs',]

print("######### enter the numbers between 0 to 9999999#######")
print("-----------------------------------------------------")
print("Min - 0 , Max - 1000000")
n = int(input('enter your number: '))

word = ''

if n == 0:
    print('zero')
elif 1 <= n <= 19:
    print(ones[n])

elif 20 <= n <= 99:
    print(tens[n//10] + " " + ones[n%10])

elif 100 <= n <= 999:
    h = str(n)[1:]
    H=int(h)
    print(hundred[n//100]+ " " + tens[H//10] + " " + ones[H%10])

elif 1000 <= n <=9999:
    t = str(n)[1:]
    T = int(t)
    h = str(n)[2:]
    H  = int(h)
    print(thousands[n//1000]+ " " + hundred[T//100]+ " " +tens[H//10] + " " + ones[H%10])

elif 10000 <= n <=99999:
    t = str(n)[1:]
    T = int(t)
    h = str(n)[2:]
    H  = int(h)
    ts = str(n)[3:]
    TS = int(ts)
    print(lakhs[n//10000] + " " +thousands[T//1000] + " " + hundred[H//100] + " " +tens [TS//10] + " " + ones[TS%10])

elif 100000 <= n <= 999999:
    l = str(n)[1:]
    L = int(l)
    t = str(n)[2:]
    T = int(t)
    h = str(n)[3:]
    H  = int(h)
    ts = str(n)[4:]
    TS = int(ts)
    print(lakhs_10[n//100000]+ " " + lakhs[L//10000] + " " +thousands[T//1000] + " " + hundred[H//100] + " " +tens [TS//10] + " " + ones[TS%10])

elif n ==1000000:
    print("1 milllion")

else:
    print("Give the numbers between 0 to 1-million only")



