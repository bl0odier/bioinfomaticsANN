import array
import numpy as np

def parsecoding(char: chr,l,pos: int):
    if char is 'A':
        l[pos*20 + 0]=1
    if char is 'C':
        l[pos*20 +1]=1
    if char is 'D':
        l[pos*20 +2]=1
    if char is 'E':
        l[pos*20 +3]=1
    if char is 'F':
        l[pos*20 +4]=1
    if char is 'G':
        l[pos*20 +5]=1
    if char is 'H':
        l[pos*20 +6]=1
    if char is 'I':
        l[pos*20 +7]=1
    if char is 'K':
        l[pos*20 +8]=1
    if char is 'L':
        l[pos*20 +9]=1
    if char is 'M':
        l[pos*20 +10]=1
    if char is 'N':
        l[pos*20 +11]=1
    if char is 'P':
        l[pos*20 +12]=1
    if char is 'Q':
        l[pos*20 +13]=1
    if char is 'R':
        l[pos*20 +14]=1
    if char is 'S':
        l[pos*20 +15]=1
    if char is 'T':
        l[pos*20 +16]=1
    if char is 'V':
        l[pos*20 +17]=1
    if char is 'W':
        l[pos*20 +18]=1
    if char is 'Y':
        l[pos*20 +19]=1
    
    
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))



num_examples = 400
nn_input_dim = 180
nn_output_dim = 1

epsilon = 0.5



f = open('data_b.dat','r')
first200lines=f.readlines()[0:199]
i=0
for line in first200lines:
    inputlist = [0]*180
    outputlist = [1]
    line = first200lines[i]
    parsecoding(line[0],inputlist,0)
    parsecoding(line[1],inputlist,1)
    parsecoding(line[2],inputlist,2)
    parsecoding(line[3],inputlist,3)
    parsecoding(line[4],inputlist,4)
    parsecoding(line[5],inputlist,5)
    parsecoding(line[6],inputlist,6)
    parsecoding(line[7],inputlist,7)
    parsecoding(line[8],inputlist,8)

    np.random.seed(1)
    w1= 2*np.random.random((180,5))-1
    w2= 2*np.random.random((5,1))-1
    j=0
    for j in range(50):
        l0 = inputlist
        l1 = nonlin(np.dot(l0,w1))
        l2 = nonlin(np.dot(l1,w2))

        l2E = outputlist - l2
        if(j%10) == 0:
            print ("Error:" + str(np.mean(np.abs(l2E))))

        l2D = l2E*nonlin(l2,deriv=True)
        l1E = l2D.dot(w2.T)
        l1D = l1E * nonlin(l1,deriv=True)
        w2 += l2.T.dot(l2D)
        w1 += l1.T.dot(l1D)
        j+=0

    i+=1
f.close()


f = open('data_nb.dat','r')
first200lines=f.readlines()[0:199]
i=0
for line in first200lines:
    inputlist = [0]*180
    outputlist = [0]
    line = first200lines[i]
    parsecoding(line[0],inputlist,0)
    parsecoding(line[1],inputlist,1)
    parsecoding(line[2],inputlist,2)
    parsecoding(line[3],inputlist,3)
    parsecoding(line[4],inputlist,4)
    parsecoding(line[5],inputlist,5)
    parsecoding(line[6],inputlist,6)
    parsecoding(line[7],inputlist,7)
    parsecoding(line[8],inputlist,8)

    np.random.seed(1)
    w1= 2*np.random.random((180,5))-1
    w2= 2*np.random.random((5,1))-1
    j=0
    for j in range(50):
        l0 = inputlist
        l1 = nonlin(np.dot(l0,w1))
        l2 = nonlin(np.dot(l1,w2))

        l2E = outputlist - l2
        if(j%10) == 0:
            print ("Error:" + str(np.mean(np.abs(l2E))))

        l2D = l2E*nonlin(l2,deriv=True)
        l1E = l2D.dot(w2.T)
        l1D = l1E * nonlin(l1,deriv=True)
        w2 += l2.T.dot(l2D)
        w1 += l1.T.dot(l1D)
        j+=0

    i+=1
f.close()




f = open('data_b.dat','r')
first200lines=f.readlines()[200:399]
i=0
for line in first200lines:
    inputlist = [0]*180
    outputlist = [1]
    line = first200lines[i]
    parsecoding(line[0],inputlist,0)
    parsecoding(line[1],inputlist,1)
    parsecoding(line[2],inputlist,2)
    parsecoding(line[3],inputlist,3)
    parsecoding(line[4],inputlist,4)
    parsecoding(line[5],inputlist,5)
    parsecoding(line[6],inputlist,6)
    parsecoding(line[7],inputlist,7)
    parsecoding(line[8],inputlist,8)

    np.random.seed(1)
    w1= 2*np.random.random((180,5))-1
    w2= 2*np.random.random((5,1))-1
    j=0
    for j in range(50):
        l0 = inputlist
        l1 = nonlin(np.dot(l0,w1))
        l2 = nonlin(np.dot(l1,w2))

        l2E = outputlist - l2
        if(j%10) == 0:
            print ("Error:" + str(np.mean(np.abs(l2E))))

        l2D = l2E*nonlin(l2,deriv=True)
        l1E = l2D.dot(w2.T)
        l1D = l1E * nonlin(l1,deriv=True)
        w2 += l2.T.dot(l2D)
        w1 += l1.T.dot(l1D)
        j+=0

    i+=1

print(line)
print(inputlist)
    


f.close()
