#continue = ctn

fuirt = [
    {
    "name" : "apple" ,
    "price" : 5 
    },
    {
    "name" : "oranges" ,
    "price" : 4
    },
    {
    "name" : "banana" ,
    "price" : 2
    },
    {"name" : "avocado" ,
    "price" : 3
    } ]
print (fuirt)

strd =[]
many = []
tong = 0
contin = "a"
def bill(many) :
    global tong
    for i in range (len(many)):
        tong += many[i]
    
        

def choose() :
    fui_choo = input ("what are you buy?")
    for x in fuirt :
        if fui_choo in x.values() :
            quantity = input("how much you want to buy?")
            total_price =  int(quantity) * int(x["price"])
            print ("{0} {1} have value {2}".format(quantity, x["name"],total_price))
            
            name = x["name"]
            strd.append ("{0} voi gia {1} thanh tien {2}".format(x["name"],x["price"],total_price))
            many.append (total_price)
            print (many)
    contin = input("continue_?")
    if contin == "oki" :
        bill(many)

        print ("your total " ,"\n", strd )
        print ("tong tien your bill" , tong)
        
##            else :
##                
##                choose ()

        
while contin!="oki":
    choose ()
