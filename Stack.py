lst=[]
def display():
    print(lst)
def push(a):
    lst.append(a)
def pop():
    if lst==[]:
        print('underflow')
    else:
        printlst.pop(),"popped")
         

ch=0
while(1):
    print('1.push')
    print('2.pop')
    print('3.display')
    print('4.exit')
    ch=int(input('enter choice:\t'))
    if ch==1:
        a=int(input('enter input:\t'))
        push(a)
    elif ch==2:
          pop()
    elif ch==3:
         display()
    elif ch==4:
         print('exit')
