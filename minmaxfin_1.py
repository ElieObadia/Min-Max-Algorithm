import time
class morp:
    def __init__(self):
        self.initialize_game()
    def initialize_game(self):
        self.board = {i:' ' for i in range(1,145)}
        self.lastletter = ' '
        self.player = 'X'
        self.bot = 'O'
        self.player_turn = 'X'
        self.limit = 0
        self.limite= 10000
        self.tempom = 20
        self.tempom2 = -20
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.posiX = 0
        self.board[66] = "O"
    def draw_board(self):
      count = 1
      for i in range(23):
        if i%2 == 0:
          txt = ''
          for j in range(count,count+11):
            txt = txt + str(self.board[j])
            txt+='|'
          txt += self.board[count+11]
          count += 12
          print(txt)
        else:
          print('-+-+-+-+-+-+-+-+-+-+-+-')
      print("\n")
    def win4(self,mark):
        for col in range(12):
            for ligne in range(col*12+1,col*12+10):
                if (self.board[ligne]== self.board[ligne+1] and self.board[ligne]== self.board[ligne+2] and self.board[ligne]==mark and self.board[ligne]== self.board[ligne+3]):
                    return True
    
        for k in range(1,13):
            tempo_table = [k+12*j for j in range(12)]
            for tempo_i in range(0,9):
                if (self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+1]] and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+2]] and self.board[tempo_table[tempo_i]]==mark and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+3]]):
                    return True
            
        for k in range(0,9):
            for tempo_i in range(1,10):
                if ((self.board[k*12+tempo_i]== self.board[k*12+tempo_i+13] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+26] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+39] and self.board[k*12+tempo_i]== mark )):
                    return True              
    
            for tempo_i in range(4,13):
                if (self.board[k*12+tempo_i]== self.board[k*12+tempo_i+11] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+22] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+33]  and self.board[k*12+tempo_i]== mark ):
                    return True     
        return False       
    def Maywin3(self,mark):
        for col in range(12):
            for ligne in range(col*12+1,col*12+10):
                if (self.board[ligne]== self.board[ligne+1] and self.board[ligne]== self.board[ligne+2] and self.board[ligne]==mark and self.board[ligne+3]==" ") or (self.board[ligne+1]== self.board[ligne+2] and self.board[ligne+1]== self.board[ligne+3] and self.board[ligne+1]==mark and self.board[ligne]==" "):
                    return True
    
        for k in range(1,13):
            tempo_table = [k+12*j for j in range(12) ]
            for tempo_i in range(0,9):
                if (self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+1]] and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+2]] and self.board[tempo_table[tempo_i]]==mark and self.board[tempo_table[tempo_i+3]]==" ") or  (self.board[tempo_table[tempo_i+1]]== self.board[tempo_table[tempo_i+2]] and self.board[tempo_table[tempo_i+1]]== self.board[tempo_table[tempo_i+3]] and self.board[tempo_table[tempo_i+1]]==mark and self.board[tempo_table[tempo_i]]==" "):
                    return True
            
        for k in range(0,9):
            for tempo_i in range(1,10):
                if ((self.board[k*12+tempo_i]== self.board[k*12+tempo_i+13] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+26] and self.board[k*12+tempo_i+39]==' ' and self.board[k*12+tempo_i]== mark )) or (self.board[k*12+tempo_i+13]== self.board[k*12+tempo_i+26] and self.board[k*12+tempo_i+13]== self.board[k*12+tempo_i+39] and self.board[k*12+tempo_i]==' '  and self.board[k*12+tempo_i+39]== mark):
                    return True              
    
            for tempo_i in range(4,13):
                if (self.board[k*12+tempo_i]== self.board[k*12+tempo_i+11] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+22] and self.board[k*12+tempo_i+33]==' '  and self.board[k*12+tempo_i]== mark ) or (self.board[k*12+tempo_i+11]== self.board[k*12+tempo_i+22] and self.board[k*12+tempo_i+11]== self.board[k*12+tempo_i+33] and self.board[k*12+tempo_i]== " "  and self.board[k*12+tempo_i+33]== mark):
                    return True     
        return False 

    
    def Maywin_2(self,mark):
        for k in range(4,9):
            for i in range(4,13):
                if(self.board[k*12+i] == self.board[k*12+i-13] and self.board[k*12+i]== mark and self.board[k*12+i-26]==' ' and self.board[k*12+i-39]==' '):
                    return True
        for k in range(4,12):
            for i in range(1,9):
                if(self.board[k*12+i] == self.board[k*12+i -11] and self.board[k*12+i]== mark and self.board[k*12+i -22]==' ' and self.board[k*12+i -33]==' '):
                    return True
        for k in range(0,9):
            for i in range(1,13):
                if(self.board[k*12+i] == self.board[k*12+i+12] and self.board[k*12+i]== mark and self.board[k*12+i+24]==' ' and self.board[k*12+i+36]==' '):
                    return True
        for k in range(5,12):
            for i in range(1,13):
                if(self.board[k*12+i] == self.board[k*12+i-12] and self.board[k*12+i]== mark and self.board[k*12+i-24]==' ' and self.board[k*12+i-36]==' '):
                    return True
        count = 1
        for col in range(12):
            for ligne in range(count,count+9):
                if (self.board[ligne]== self.board[ligne+1] and self.board[ligne]==mark and self.board[ligne+3]== self.board[ligne+2] and self.board[ligne+3]==" ") or (self.board[ligne+2]== self.board[ligne+1]  and self.board[ligne+2]==mark and self.board[ligne]==' ' and self.board[ligne+3]==" ") or (self.board[ligne+2]== self.board[ligne+3]  and self.board[ligne+2]==mark and self.board[ligne]== self.board[ligne+1] and self.board[ligne+1]==" "):
                    return True
            count +=12 
    
        count = 1
        for k in range(12):
            tempo_table = [count+12*j for j in range(12) ]
            for tempo_i in range(0,9):
                if (self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+1]]  and self.board[tempo_table[tempo_i]]==mark  and self.board[tempo_table[tempo_i+2]]== self.board[tempo_table[tempo_i+3]]  and self.board[tempo_table[tempo_i+3]]==" " ) or (self.board[tempo_table[tempo_i+1]]== self.board[tempo_table[tempo_i+2]]  and self.board[tempo_table[tempo_i+1]]==mark  and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+3]]  and self.board[tempo_table[tempo_i+3]]==" " ) or (self.board[tempo_table[tempo_i+2]]== self.board[tempo_table[tempo_i+3]]  and self.board[tempo_table[tempo_i+2]]==mark  and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+1]]  and self.board[tempo_table[tempo_i]]==" " ):
                    return True
            count +=1
    
        for k in range(0,9):
            for tempo_i in range(1,10):
                if ((self.board[k*12+tempo_i]== self.board[k*12+tempo_i+13]  and self.board[k*12+tempo_i]== mark  and self.board[k*12+tempo_i+26]==' ' and self.board[k*12+tempo_i+39]==' ' and self.board[k*12+tempo_i]!=10+k*12)) or (self.board[k*12+tempo_i+13]== self.board[k*12+tempo_i+26]  and self.board[k*12+tempo_i+13]== mark and self.board[k*12+tempo_i]==' ' and self.board[k*12+tempo_i+39]==' ' and self.board[k*12+tempo_i]!=10+k*12) or (self.board[k*12+tempo_i+26]== self.board[k*12+tempo_i+39]  and self.board[k*12+tempo_i+26]== mark and self.board[k*12+tempo_i]==' ' and self.board[k*12+tempo_i+13]==' ' and self.board[k*12+tempo_i]!=10+k*12):
                    return True              
    
            for tempo_i in range(4,13):
                if ((self.board[k*12+tempo_i]== self.board[k*12+tempo_i+11]  and self.board[k*12+tempo_i]== mark  and self.board[k*12+tempo_i+22]==' ' and self.board[k*12+tempo_i+33]==' ' and self.board[k*12+tempo_i]!=10+k*12)) or (self.board[k*12+tempo_i+11]== self.board[k*12+tempo_i+22]  and self.board[k*12+tempo_i+11]== mark and self.board[k*12+tempo_i]==' ' and self.board[k*12+tempo_i+33]==' ' and self.board[k*12+tempo_i]!=10+k*12) or (self.board[k*12+tempo_i+22]== self.board[k*12+tempo_i+33]  and self.board[k*12+tempo_i+22]== mark and self.board[k*12+tempo_i]==' ' and self.board[k*12+tempo_i+11]==' ' and self.board[k*12+tempo_i]!=10+k*12):
                    return True     
        return False 
    def evaluate(self):
        if (self.win4(self.player)):
            return -1000
        elif (self.win4(self.bot)):
            return 1000
        elif (self.Maywin3(self.player)):
            return -8
        elif (self.Maywin3(self.bot)):
            return 8
        elif (self.Maywin_2(self.player)):
            return -6
        elif (self.Maywin_2(self.bot)):
            return 6
        else:
            return 0
    def proximite(self):
        tab = []
        for i in self.board:
            if (self.board[i]!=" "):
                tab.append(i)
        tab2 = []
        for i in tab:
            if (i-13>0):
                tab2.append(i-13)
            if (i-12>0):
                tab2.append(i-12)
            if (i-11>0):
                tab2.append(i-11)
            if (i-1>0):    
                tab2.append(i-1)
            if (i+1<145):
                tab2.append(i+1)
            if (i+11<145):
                tab2.append(i+11)
            if (i+12<145):
                tab2.append(i+12)
            if (i+13<145):
                tab2.append(i+13)
        tab2 = list(set(tab2))
        return tab2
            
            
            
    def spaceIsFree(self,position):
        return True if (self.board[position]==' 'and position<=144 and position>=1) else False

    def checkforWin(self):
# ROW CHECK
        count = 1
        for col in range(12):
    
            for ligne in range(count,count+9):
                if (self.board[ligne]== self.board[ligne+1] and self.board[ligne]== self.board[ligne+2] and self.board[ligne]== self.board[ligne+3] and self.board[ligne]!=' '):
                    self.lastletter = self.board[ligne]
                    return self.board[ligne]
            count +=12
    # COL CHECK
        count = 1
        for k in range(12):
            tempo_table = []
            for nombre_col in (count, count+12, count+12*2, count+12*3, count+12*4, count+12*5, count+12*6, count+12*7, count+12*8, count+12*9, count+12*10, count+12*11):
                tempo_table.append(nombre_col)
            for tempo_i in range(0,9):
                if (self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+1]] and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+2]] and self.board[tempo_table[tempo_i]]== self.board[tempo_table[tempo_i+3]] and self.board[tempo_table[tempo_i]]!=' '):
                    
                    self.lastletter = self.board[tempo_table[tempo_i]]
                    return self.board[tempo_table[tempo_i]]
            count +=1
            
    # DIAGO CHECK
        count = 1
        for k in range(0,9):
            for tempo_i in range(1,10):
                if (self.board[k*12+tempo_i]== self.board[k*12+tempo_i+13] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+26] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+39] and self.board[k*12+tempo_i]!=' ' and self.board[k*12+tempo_i]!=10+k*12):
                    
                    self.lastletter = self.board[k*12+tempo_i]
                    return self.board[k*12+tempo_i]
            count +=1
    # DIAGO CHECK droite gauche
        count = 1
        for k in range(0,9):
            for tempo_i in range(4,13):
                if (self.board[k*12+tempo_i]== self.board[k*12+tempo_i+11] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+22] and self.board[k*12+tempo_i]== self.board[k*12+tempo_i+33] and self.board[k*12+tempo_i]!=' ' and self.board[k*12+tempo_i]!=10+k*12):
                    
                    self.lastletter = self.board[k*12+tempo_i]
                    return self.board[k*12+tempo_i]
            count +=1
            
            
        for k in range(1,144):
              if (self.board[k] == ' '):
                 return None
                    
                    
        return ' ' 

    def max_alpha_beta(self,alpha, beta):
        maxv = -20
        self.limit = self.limit+1
        result = self.checkforWin()
        if result == 'X':
            return (-10, 1, 0)    
        elif result == 'O':
            return (10, 1, 0)
        elif result == ' ':
            return (0, 1, 0)
        if(self.limit>self.limite) : 
            self.tempom = self.evaluate()
            return (self.tempom,self.x2,self.y2)
        for emplacement in self.proximite():
            
                if self.board[emplacement]== ' ':
                    self.board[emplacement] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    self.board[emplacement] =' '   
                    if m > maxv:
                        maxv = m
                        px = emplacement%12
                        py = emplacement//12
                        if(maxv>5):
                            return(maxv,px,py)
                    if m > alpha:
                        alpha = m
        return (maxv, px, py)

    def min_alpha_beta(self,alpha, beta):
        minv = 20
        self.limit = self.limit+1
        result = self.checkforWin()
        if result == 'X':
            return (-10, 1, 0)
        elif result == 'O':
            return (10, 1, 0)
        elif result == ' ':
            return (0, 1, 0)  
        if(self.limit>self.limite) :  
            self.tempom = self.evaluate()
            return (self.tempom,self.x1,self.y1)
        for emplacement in self.proximite():
                if self.board[emplacement] == ' ':
                    self.board[emplacement] = 'X'
                    # self.insertLetter('X',i*12+j)
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    self.board[emplacement] = ' '
                    if m < minv:
                        minv = m
                        px = emplacement%12
                        py = emplacement//12
                        if(minv<-5):
                            return(minv,px,py)
                    if m < beta:
                        beta = m
        return (minv, px, py)
    def play_alpha_beta(self):
         while True:
            self.draw_board()
            self.result = self.checkforWin()
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == ' ':
                    print("It's a tie!")
    
    
                self.initialize_game()
                return
    
            if self.player_turn == 'X':
    
                while True:
                    position = int(input("Entrer la position pour X :"))
                    if (position<145 and position >0 and self.spaceIsFree(position)):
                        self.board[position] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')
    
            else:
                self.limit = 0
                (m, px, py) = self.max_alpha_beta(-20, 20)
                self.board[py*12+px] = 'O'
                self.tempom = -20
                self.tempom2 = 20
                self.x1 = None
                self.y1 = None
                self.x2 = None
                self.y2 = None
                self.player_turn = 'X'
                print("le move de l'ordi est : X = " + str(px) + " Y= " + str(py))
def main():
    g = morp()
    g.play_alpha_beta()

if __name__ == "__main__":
    main()