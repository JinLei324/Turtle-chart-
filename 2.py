from turtle import Turtle, Screen
from itertools import cycle


coutryData=[]
asiacountry=[]
northamericacountry=[]
southamericacountry=[]
africacountry=[]
europecountry=[]
oceancountry=[]

chinaPopu=0


myturtle = Turtle()
myturtle.screen.setup(width=1366,height=768)
def hidescreen(x,y):    
    myturtle.hideturtle()
myturtle.screen.onclick(hidescreen);

style = ('Courier', 16, 'bold') 

myturtle.write("Please Select Menu from Console.", align="center",font=style)
    
def loadCoutryData():
    rowcount = 1
    with open('WorldPopulationData2019.txt') as file:
        for line in file:
            rowcount=rowcount+1
            if(rowcount<3):
                continue 
            line=line.strip('\n')
            line=line.split('; ')
            if(line[1]=='China'):                
                chinaPopu=int(line[3])                
            if(line[7]=='Asia'):    
               asiacountry.append(line)             
            if(line[7]=='North America'):            
                northamericacountry.append(line)
            if(line[7]=='South America'):            
                southamericacountry.append(line)
            if(line[7]=='Africa'):            
                africacountry.append(line)
            if(line[7]=='Europe'):            
                europecountry.append(line)
            if(line[7]=='Oceania'):            
                oceancountry.append(line)    
            coutryData.append(line)
            

def chartDisplay():
    myturtle.showturtle()
    asia=1
    northamerica=1
    southamerica=1
    africa=1
    europe=1
    oceania=1
   
    for line in coutryData:
              
        if(line[7]=='Asia'):               
            asia=asia+int(line[3]) 
                    
        if(line[7]=='North America'):
            northamerica=northamerica+int(line[3])
            
        if(line[7]=='South America'):
            southamerica=southamerica+int(line[3])
            
        if(line[7]=='Africa'):
            africa=africa+int(line[3])
            
        if(line[7]=='Europe'):
            europe=europe+int(line[3])
            
        if(line[7]=='Oceania'):
            oceania=oceania+int(line[3]) 
            

    letter_frequencies = [\
        ('Asia', asia), ('North America', northamerica), ('South America', southamerica), ('Africa', africa), ('Europe', europe), \
        ('Oceania', oceania)]

    COLORS = cycle(['green', 'red', 'cyan', 'brown', 'blue', 'mediumpurple'])

    RADIUS = 200


    total = sum(fraction for _, fraction in letter_frequencies)  

      
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    
    myturtle.penup()
    myturtle.setx(-250)
    myturtle.sety(100)
    display="Asia ="+'{0}'.format(asia)
    myturtle.write(display, align="right",font=style)
    myturtle.sety(80)
    display="North America ="+'{0}'.format(northamerica)
    myturtle.write(display, align="right",font=style)
    myturtle.sety(60)
    display="South America="+'{0}'.format(southamerica)
    myturtle.write(display, align="right",font=style)
    myturtle.sety(40)
    display="Africa="+'{0}'.format(africa)
    myturtle.write(display, align="right",font=style)
    myturtle.sety(20)
    display="Europe="+'{0}'.format(europe)
    myturtle.write(display, align="right",font=style)
    myturtle.sety(0)
    display="Oceania="+'{0}'.format(oceania)
    myturtle.write(display, align="right",font=style)
    
    myturtle.penup()
    myturtle.setx(100)
    myturtle.sety(-RADIUS)
    myturtle.pendown()

    for _, fraction in letter_frequencies:
        myturtle.fillcolor(next(COLORS))
        myturtle.begin_fill()
        myturtle.circle(RADIUS, fraction * 360 / total)
        position = myturtle.position()
        myturtle.goto(100, 0)
        myturtle.end_fill()
        myturtle.setposition(position)

    # The labels

    myturtle.penup()
    LABEL_RADIUS = RADIUS * 1.35
    myturtle.sety(-LABEL_RADIUS)
    
    for label, fraction in letter_frequencies:
        myturtle.circle(LABEL_RADIUS, fraction * 360 / total / 2)
        percent = fraction*100/total
        display = label+" "+'{0:.1f}'.format(percent)+"%"
        myturtle.write(display, align="center",font=style)
        '''
        if(90<fraction * 360 / total / 2 <250):
            myturtle.write(display, align="left",font=style)
        else:
            myturtle.write(display, align="right",font=style)
        '''
        myturtle.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    #myturtle.hideturtle()
    
    
def sortChangeFunc(e):
    return e[6]

def displayAllCountry(count):
    myturtle.showturtle()  
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    myturtle.penup()
    coutryData.sort(key=sortChangeFunc,reverse=True)
    #print(coutryData[0])
    style = ('Courier', 10, 'bold')
    
    myturtle.setx(-500)    
    myturtle.sety(350)
    display="Country name sorted by population change"
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(330)
    display='{0:>5} {1:^40} {2:30} {3:6}'.format("Range","Country Name","Population(2019)","Change" )
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(310)
    display='======================================================================================='
    myturtle.write(display, align="left",font=style)
    
    ypos = 310
    for i in range(0,count):
        ypos = ypos-20
        myturtle.sety(ypos)

        display='{0:>5} {1:^40} {2:30} {3:6}'.format(i+1,coutryData[i][1],coutryData[i][3],coutryData[i][6] )
        
        myturtle.write(display, align="left",font=style)
  
    #myturtle.hideturtle()
    
    
def displayBarCountry(count):
    coutryData.sort(key=sortChangeFunc,reverse=True)
    
    myturtle.showturtle()  
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    myturtle.penup()
    
    #print(coutryData[0])
    style = ('Courier', 10, 'bold')
    
    myturtle.setx(0)    
    myturtle.sety(200)
    display="Country name sorted by population change"
    myturtle.write(display, align="center",font=style)
    
    myturtle.setx(-60*count/2)    
    myturtle.sety(-250)
    myturtle.pendown()
    myturtle.forward(60*count)
   
    COLORS = cycle(['green', 'red', 'cyan', 'brown', 'blue', 'mediumpurple'])
    xpos = -60*count/2+20
    
    for i in range(0,count):
        myturtle.fillcolor(next(COLORS))
        myturtle.begin_fill()
        myturtle.penup()        
        myturtle.setx(xpos)
        myturtle.pendown()
        myturtle.left(90)
        
        height = 80*(float(coutryData[i][6]))
        myturtle.forward(int(height))
        display='{0:6}'.format(coutryData[i][6] )
        myturtle.write(display,align="left",font=style)
        myturtle.right(90)
        myturtle.forward(20)
        myturtle.right(90)
        myturtle.forward(int(height))
        myturtle.left(90)       
        myturtle.end_fill()
        xpos = xpos+60
        
    xpos = -60*count/2+30
    myturtle.penup()
    myturtle.setx(xpos)
    myturtle.sety(-280)
    
    for i in range(0,count,3):
        display='{0}'.format(coutryData[i][1])        
        myturtle.write(display, align="center",font=style)
        xpos=xpos+180
        myturtle.setx(xpos)
    
    xpos = -60*count/2+90
    myturtle.penup()
    myturtle.setx(xpos)
    myturtle.sety(-300)
    
    for i in range(1,count,3):
        display='{0}'.format(coutryData[i][1])        
        myturtle.write(display, align="center",font=style)
        xpos=xpos+180
        myturtle.setx(xpos)
        
    xpos = -60*count/2+150
    myturtle.penup()
    myturtle.setx(xpos)
    myturtle.sety(-320)
    
    for i in range(2,count,3):
        display='{0}'.format(coutryData[i][1])        
        myturtle.write(display, align="center",font=style)
        xpos=xpos+180
        myturtle.setx(xpos)
        
        
    #myturtle.hideturtle()
def sortNameFunc(e):
    return e[1]
def displayCountryLetter(name_letter):
    myturtle.showturtle()  
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    myturtle.penup()
    coutryData.sort(key=sortNameFunc)
    #print(coutryData[0])
    style = ('Courier', 10, 'bold')
    
    myturtle.setx(-500)    
    myturtle.sety(350)
    display="Country name by letter"
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(330)
    display='{0:>5} {1:^40} {2:30} '.format("No.","Country Name","Population(2019)" )
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(310)
    display='======================================================================================='
    myturtle.write(display, align="left",font=style)
    
    ypos = 310
    row = 0;
    letter_len = len(name_letter)
    name_letter=name_letter.title()
    
    for line in coutryData:
        country_name_len=len(line[1])
        if(country_name_len< letter_len):
            continue
        if(name_letter==line[1][:letter_len]):
            ypos = ypos-20
            row=row+1
            myturtle.sety(ypos)
            display='{0:>5} {1:^40} {2:30} '.format(row,line[1],line[3])        
            myturtle.write(display, align="left",font=style)

def displayCountryAlph(number_alph):
    myturtle.showturtle()  
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    myturtle.penup()
    coutryData.sort(key=sortNameFunc)
    #print(coutryData[0])
    style = ('Courier', 10, 'bold')
    
    myturtle.setx(-500)    
    myturtle.sety(350)
    display="Country name by letter"
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(330)
    display='{0:>5} {1:^40} {2:30} '.format("No.","Country Name","Population(2019)" )
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(310)
    display='======================================================================================='
    myturtle.write(display, align="left",font=style)
    
    ypos = 310
    row = 0;    
        
    for line in coutryData:
        num = 0
        for i in range(0,len(line[1])):
            if(line[1][i].isalpha()):
                num=num+1        
        if(num==number_alph):        
            ypos = ypos-20
            row=row+1
            myturtle.sety(ypos)
            display='{0:>5} {1:^40} {2:30} '.format(row,line[1],line[3])        
            myturtle.write(display, align="left",font=style)
    #myturtle.hideturtle()    
    

def sortIncreaseFunc(e):
    return int(e[3])-int(e[2])
def displayLagestIncrease(number):
    myturtle.showturtle()  
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    myturtle.penup()
    coutryData.sort(key=sortIncreaseFunc,reverse=True)
    #print(coutryData[0])
    style = ('Courier', 10, 'bold')
    
    myturtle.setx(-500)    
    myturtle.sety(350)
    display="Country name by Increase population"
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(330)
    display='{0:>5} {1:^40} {2:20} {3:20} {4:20}'.format("No.","Country Name","Population(2019)","Population(2018)","Increase population" )
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(310)
    display='=================================================================================================================='
    myturtle.write(display, align="left",font=style)
    
    ypos = 310
    for i in range(0,number):
        ypos = ypos-20
        myturtle.sety(ypos)

        display='{0:>5} {1:^40} {2:20} {3:20} {4:20}'.format(i+1,coutryData[i][1],coutryData[i][3],coutryData[i][2],int(coutryData[i][3])-int(coutryData[i][2]) )
        
        myturtle.write(display, align="left",font=style)
        
        
def sortPopulationFunc(e):
    return int(e[3])
def displaySmallAndLarge():
    myturtle.showturtle()  
    myturtle.clear()
    style = ('Courier', 10, 'bold')
    myturtle.penup()
    coutryData.sort(key=sortPopulationFunc)
    
    sum_pop=0
    count = 0
    
    chinap=0
    for line in coutryData:
        if(line[1]=='China'):
            chinap=int(line[3])
    
    for line in coutryData:
        sum_pop=sum_pop+int(line[3])
        count = count+1
        if(sum_pop>chinap):
            break;
    #print(coutryData[0])
    style = ('Courier', 10, 'bold')
    
    myturtle.setx(-500)    
    myturtle.sety(350)
    display="how many countries are required to add up to the population of China in 2019? "+'{0}'.format(count)+"countries"
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(330)
    display='{0:>20} {1:^40} {2:20} '.format("Continent","Country Name","Population(2019)" )
    myturtle.write(display, align="left",font=style)
    
    myturtle.sety(310)
    display='==============================================================================================='
    myturtle.write(display, align="left",font=style)
    
    #print(asiacountry)
    asiacountry.sort(key=sortPopulationFunc)
    #print(asiacountry)
    northamericacountry.sort(key=sortPopulationFunc)
    southamericacountry.sort(key=sortPopulationFunc)
    africacountry.sort(key=sortPopulationFunc)
    europecountry.sort(key=sortPopulationFunc)
    oceancountry.sort(key=sortPopulationFunc)
    
    ypos = 310
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Asia',asiacountry[0][1],asiacountry[0][3])
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Asia',asiacountry[len(asiacountry)-1][1],asiacountry[len(asiacountry)-1][3])   
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('North America',northamericacountry[0][1],northamericacountry[0][3])
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('North America',northamericacountry[len(northamericacountry)-1][1],northamericacountry[len(northamericacountry)-1][3])   
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('South America',southamericacountry[0][1],southamericacountry[0][3])
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('South America',southamericacountry[len(southamericacountry)-1][1],southamericacountry[len(southamericacountry)-1][3])   
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Africa',africacountry[0][1],africacountry[0][3])
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Africa',africacountry[len(africacountry)-1][1],africacountry[len(africacountry)-1][3])   
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Europe',europecountry[0][1],europecountry[0][3])
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Europe',europecountry[len(europecountry)-1][1],europecountry[len(europecountry)-1][3])   
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Oceania',oceancountry[0][1],oceancountry[0][3])
    myturtle.write(display, align="left",font=style)
    
    ypos = ypos-20
    myturtle.sety(ypos)
    display='{0:>20} {1:^40} {2:20}'.format('Oceania',oceancountry[len(oceancountry)-1][1],oceancountry[len(oceancountry)-1][3])   
    myturtle.write(display, align="left",font=style)
    
#=========#=========#=========#=========#=========#=========#=========#
def main():
    loadCoutryData()
    myturtle.hideturtle()
    while True:
        print ("  ========================================")
        print ("  World Population Data 2019 Program Menu")
        print ("  ========================================")
        print
        print ("  1 - Continents Population")
        print ("  2 - Population change")
        print ("  3 - Country name started letter")
        print ("  4 - Country name with number of Alphbet")
        print ("  5 - Lagest increase in population")
        print ("  6 - Show larget and smallest populations")
        print
        print ("  X - Exit")
        print

        choice = input('Enter your choice: ')

        if (choice == 'x') or (choice == 'X'):
            break
        if choice == '1':
           chartDisplay()
        elif choice == '2':
            print ("  Select Submenu")
            print ("  ============")
            print
            print ("  1 - Display Changes by country name")
            print ("  2 - Display Bar with n Country")
            print 
            print ("  c - Back Main Menu")
            sub_choice = input('Enter your choice: ')
            if(sub_choice=='c' or sub_choice=='C'):
                break;
            count=input('Enter Country Count: ')
            if(sub_choice=='1'):
                displayAllCountry(int(count))
                pass
            elif(sub_choice=='2'):                
                displayBarCountry(int(count))
                pass
        elif choice == '3':
            name_letter = input('Enter Country Name Letter: ')
            displayCountryLetter(name_letter)
            pass
        elif choice == '4':
            number_alph = input('Enter Number of Alphabet Country Name: ')
            displayCountryAlph(int(number_alph))
        elif choice == '5':
            number = input('Enter Country Count : ')
            displayLagestIncrease(int(number))
        elif choice == '6':
            
            displaySmallAndLarge()
        else:
            print
            print ('  Try again')
            print
    #screen = Screen()
    #screen.exitonclick()
            
    


#=========#=========#=========#=========#=========#=========#=========#
if __name__ == "__main__":
    main()
    
