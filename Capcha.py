
slovarik1 = {'1':r'   ','2':' _ ','3':' _ ','4':'   ','5':' __','6':' _ ','7':'___','8':' _ ','9':' _ ','0':' _ ',
             'A':'  /|','B':' _ ','C':' _ ','D':' _ ', 'E':' _ ','F':' _ '}
slovarik2 = {'1':r'/| ','2':' _)','3':' _)','4':'/_|','5':'/__','6':'|_ ','7':'  /','8':'|_|','9':'|_|','0':'| |',
             'A':' /_|','B':'|_)','C':'|  ','D':'| \\','E':'|_ ','F':'|_ '}
slovarik3 = {'1':r' | ','2':'/__','3':' _)','4':'  |','5':'__/','6':'|_|','7':' / ','8':'|_|','9':' _|','0':'|_|',
             'A':'/  |','B':'|_)','C':'|_ ','D':'|_/', 'E':'|_ ','F':'|  '}
def printofslov(name,keyslist):
    i = 0
    while i != len(keyslist):
        print(name.get(f"{keyslist[i]}"), end='  ')
        i += 1
    print('')
def printhex(num):
    num = hex(num)
    text = str(num)
    text = text.upper()
    text = list(text[2::])
    printofslov(slovarik1, text)
    printofslov(slovarik2, text)
    printofslov(slovarik3, text)


