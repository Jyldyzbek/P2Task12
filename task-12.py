a = input()
if a.count('f') == 0:
    None
elif a.count('f')>1:
    print(a.find('f'))
    print(a.rfind('f'))
else:
    print(a.find('f'))

