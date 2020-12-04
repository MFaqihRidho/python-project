

def my_list():
    while True:
        with open('shopping.txt','a+') as file:
            item = input("Enter item: ")
            if item.lower() == 'exit':
                break
            elif item == 'list':
                file.seek(0)
                # print(file.read())
                items = list(enumerate(file.read().split(),1))
                for count,item in items:
                    print(f'{count:3d}) {item}')
            else:
                file.write(item +'\n')

   
my_list()
