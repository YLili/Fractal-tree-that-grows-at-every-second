__author__ = 'Lili'
#coding: utf-8
import matplotlib.pyplot as plt
import Queue
import math
import time

##----------  Setup two queque, NodeQue is stored the nodes that are printed this time. -----
##----------  NewNodeQue is stored the nodes that will be printed the next time.   ------
NodeQue = Queue.Queue()
NewNodeQue = Queue.Queue()

##----------  Initialize the parameter ------------------------
length = 30     #  setup the branch length
angle = 45      #  setup the branch angle
lineWidth = 10  #  setup the branch width

##----------  Calulate the new points based on the father node information ------------
def rotate_point(p1,p2,nodeAngel):
    p3 = [0,0]
    p4 = [0,0]
    p3[0] = p1[1]
    p4[0] = p2[1]
    p3[1] = p1[1] + length * math.cos(math.radians(nodeAngel))
    p4[1] = p2[1] + length * math.sin(math.radians(nodeAngel))
    return (p3,p4)

##----------  Input the father node, and get the banch node ------------
def branch(nodeTuple):
    if nodeTuple[0] == 'a':
        p3,p4 = rotate_point(nodeTuple[1],nodeTuple[2],nodeTuple[3]+angle)
        cNode = ('c',p3,p4,nodeTuple[3]+angle)
        NewNodeQue.put(cNode)
        bNode = ('b',[nodeTuple[1][1],2*nodeTuple[1][1]-nodeTuple[1][0]],[nodeTuple[2][1],2*nodeTuple[2][1]-nodeTuple[2][0]],nodeTuple[3])
        NewNodeQue.put(bNode)
    elif nodeTuple[0] == 'b':
        p3,p4 = rotate_point(nodeTuple[1],nodeTuple[2],nodeTuple[3]-angle)
        eNode = ('e',p3,p4,nodeTuple[3]-angle)
        NewNodeQue.put(eNode)
        aNode = ('a',[nodeTuple[1][1],2*nodeTuple[1][1]-nodeTuple[1][0]],[nodeTuple[2][1],2*nodeTuple[2][1]-nodeTuple[2][0]],nodeTuple[3])
        NewNodeQue.put(aNode)
    elif nodeTuple[0] == 'c':
        bNode = ('b',nodeTuple[1],nodeTuple[2],nodeTuple[3])
        NewNodeQue.put(bNode)
    #elif nodeTuple[0] == 'd':
        #self.d_branch()
    elif nodeTuple[0] == 'e':
        p3,p4 = rotate_point(nodeTuple[1],nodeTuple[2],nodeTuple[3]+angle)
        aNode = ('a',p3,p4,nodeTuple[3]+angle)
        NewNodeQue.put(aNode)
        bNode = ('b',[nodeTuple[1][1],2*nodeTuple[1][1]-nodeTuple[1][0]],[nodeTuple[2][1],2*nodeTuple[2][1]-nodeTuple[2][0]],nodeTuple[3])
        NewNodeQue.put(bNode)

# Each node is expressed as a tuple: (node type, [x1,x2],[y1,y2],grow angle)
FirstNode = ('a',[0,0],[0,50],90)
NodeQue.put(FirstNode)
fig = plt.figure()
plt.xlim(-300.0,300.0)
plt.ylim(0.0, 550.0)
for timeIndex in range(0,10):
    while ( not NodeQue.empty()):
        GrowNode = NodeQue.get()
        plt.plot(GrowNode[1],GrowNode[2], color = "green",linewidth = lineWidth)
        branch(GrowNode)
    plt.title("The "+str(timeIndex)+"ed time")
    fig.savefig('c:/MeiYin/'+str(timeIndex).zfill(2)+'.png')
    timeIndex +=1
    #print NewNodeQue.qsize()
    while ( not NewNodeQue.empty()):
        node = NewNodeQue.get()
        NodeQue.put(node)
    #time.sleep(1)
    lineWidth = 14*lineWidth/15
plt.close(fig)
