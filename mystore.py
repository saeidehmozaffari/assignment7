#!/usr/bin/env python
# coding: utf-8

# In[10]:


from pyfiglet import Figlet
import qrcode

def loadd():
    print('loading...')
    myfile=open('C:\\Users\\Sazgar\\Downloads\\store.txt','r+')
    data=myfile.read().split('\n')
    for i in range(len(data)):
        if data[i]=='':
            break
        productInfo=data[i].split(',')
        PRODUCT.append({'id':int(productInfo[0]),'name':productInfo[1],
                        'price':float(productInfo[2]),'count':int(productInfo[3])})
    print('welcome')
def showMenu():
    print('1-add product')
    print('2-edit product')
    print('3-search product with name')
    print('4-delete product')
    print('5-show product')
    print('6-buy product')
    print('7-Exit')
    print('8-qrcode')
    
def showProduct():
    for i in range(len(PRODUCT)):
        print(str(PRODUCT[i]['id'])+'\t'+PRODUCT[i]['name']
              +'\t'+str(PRODUCT[i]['price'])+'\t'+str(PRODUCT[i]['count']))
def addProduct(): 
    PRODUCT.append({'id':int(input('enter id')),'name':input('enter name'),
                    'price':float(input('enter price')),'count':int(input('enter number of product'))})
    print('prodact added')
    
def editProduct():
    productdict=searchName()
    if productdict!='product not found':
        print('1-edit id')
        print('2-edit name')
        print('3-edit price')
        print('4-edit number of product')
        num=int(input('enter number'))
        if num==1:
            productdict['id']=int(input('id is '+str(productdict['id'])+' enter new id'))
            print('id updated')   
        elif num==2:
            productdict['name']=input('name is '+productdict['name']+' enter new name')
            print('name updated') 
        elif num==3:
            productdict['price']=float(input('price is '+str(productdict['price'])+' enter new price'))
            print('price updated')
        elif num==4:
            productdict['count']=int(input(' new number of product is '+str(productdict['count'])+' enter new number of product'))
            print('number of product updated')
    else:
        print('product not found')
def deleteProduct():
    txt=input('enter name of product')
    for product in PRODUCT:
        if txt==product['name']:
            sure=input('are you sure to delete this product?Y/N')
            if sure=='y' or sure=='Y':
                PRODUCT.remove(product)
                print('product deleted')
                break
            else:
                break
    else:
            print('product not found')
def searchName():
    txt=input('enter name of product')
    for product in PRODUCT:
        if txt==product['name']:
            return product
    else:
            return 'product not found'
def searchid():
    txt=input('enter id of product or enter * for exit')
    if txt=='*':
        return '*'
    for product in PRODUCT:
        if txt==str(product['id']):
            return product
    else:
            return 'product not found'
sabadKharid=[]
def buy():
    totalprice=0

    while True:
        productdict=searchid()
        if productdict=='*':
            showsabadkharid()
            break
        
        elif productdict!='product not found':
            num=int(input('enter number of product you want to buy'))
            productNumber=productdict['count']
            if num<=productNumber:
                productNumber-=num
                sumprice=productdict['price']*num
                totalprice+=sumprice
                sabadKharid.append({'count':num,'name':productdict['name'],'price':productdict['price'],
                                    'sumprice':sumprice,'totalprice':totalprice})
                productdict['count']=productNumber
                print('product added to cart')
            else:
                print('insufficient inventory! you can buy up to '+str(productdict['count'])+' of these product')
        elif productdict=='product not found':
            print('product not found')
def showsabadkharid():
    for i in range(len(sabadKharid)):
        print(str(sabadKharid[i]['count'])+'\t'+sabadKharid[i]['name']
              +'\t'+str(sabadKharid[i]['price'])+'\t'+str(sabadKharid[i]['sumprice'])+'\t'+str(sabadKharid[i]['totalprice']))
def qcode():
    id= searchid()
    img=qrcode.make(id)
    img.save('qrcode.png')
PRODUCT=[]
loadd()
while True:
    showMenu()
    f=Figlet(font='standard')
    print(f.renderText('store'))
    num=int(input('enter a number:'))
    if num==1:
        addProduct()
    elif num==2:
        editProduct()
    elif num==3:
        print(searchName())
    elif num==4:
        deleteProduct()
    elif num==5:
        showProduct()
    elif num==6:
        buy()
    elif num==7:
        myfile=open('C:\\Users\\Sazgar\\Downloads\\store.txt','w')

        for i in range(len(PRODUCT)):
            if i<len(PRODUCT):
                myfile.write(str(PRODUCT[i]['id'])+','+PRODUCT[i]['name']+','+str(PRODUCT[i]['price'])+
                             ','+str(PRODUCT[i]['count'])+'\n')
            else:
                myfile.write(str(PRODUCT[i]['id'])+','+PRODUCT[i]['name']+','+str(PRODUCT[i]['price'])+
                             ','+str(PRODUCT[i]['count']))

        myfile.close()
        break
        exit()
    elif num == 8:
        qcode()





