
dic=[]
with open('BridgeFDB.txt') as fileFDB:
    for line in fileFDB: 
        line=line.strip('\n')
        dic.append(line)
#define mac:port dictionary from BridgeFDB.txt
#like {'00-00-00-11-0b-0d': '1', '00-13-46-c6-a5-35': '2'}
mac_portdic = dict(zip(dic[0::2],dic[1::2]))


dic.clear()

with open('RandomFrames.txt') as fileFrames:
    for line in fileFrames: 
        line=line.strip('\n')
        dic.append(line)

#define source:[dest,port] dictionary from RandomFrames.txt
#like {'00-00-00-11-0b-0d': ['00-13-46-c6-a5-35', '1'], '00-0c-29-51-33-c1': ['01-00-5e-7f-ff-64', '4']}
    
frames={}
for i in range(0,len(dic),3):
    frames[dic[i]] = [dic[i+1],dic[i+2]]

output=[]
fileoutput = open('BridgeOutput.txt','w')
fileFDB=open('BridgeFDB.txt','a+')
for key, value in frames.items():
    if(key in mac_portdic ):        
        if(value[0] in mac_portdic):
            fileoutput.write("%s\t%s\t%s\tForward on port %s\n"%(key,value[0],value[1],mac_portdic[value[0]]))
        else:
            fileoutput.write("%s\t%s\t%s\tDiscarded\n"%(key,value[0],value[1]))
    else:
        #source update
        fileFDB.write("%s\n"%key)
        fileFDB.write("%s\n"%value[1])
        
        if(value[0] in mac_portdic):
            fileoutput.write("%s\t%s\t%s\tForward on port %s\n"%(key,value[0],value[1],mac_portdic[value[0]]))
        else:
            fileoutput.write("%s\t%s\t%s\Broadcast\n"%(key,value[0],value[1]))    

fileoutput.close()
fileFDB.close()