#Async ka Matlab Jab hum kisi bhi func ko run karte jab tak wo run ho raha hai us waqt mai 
#jab hume wait karna padta hai us waqt khatam karne ko asynchronunces kehte hai

import Async_IO

async def Func1():
    print("1")
    asyncio.sleep(3) #Iska Matlb Jab Tak Wait Kar Raha hoo tab tak dusra kaam karlo
    print("2")
async def Func2():
    print("3")
    asyncio.sleep(3) #Iska Matlb Jab Tak Wait Kar Raha hoo tab tak dusra kaam karlo
    print("4")
async def Func3():
    print("5")
    asyncio.sleep(3) #Iska Matlb Jab Tak Wait Kar Raha hoo tab tak dusra kaam karlo
    print("6")
    
async def main():    
       await Func1(),
       await Func2(),
       await Func3()
 
    
