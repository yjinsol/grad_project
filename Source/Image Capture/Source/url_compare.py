def url_compare():

    b = 'https://spot.wooribank.com/pot/Dream?withyou=bp' + '\n'
    f = open("test.txt", 'r')
    while 1:
        k = f.readline()
        if not k: break
        if b == k:
            print("This URL is matching")
            break
        else:
            pass

url_compare()