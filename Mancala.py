'''
Mini 4
Javier Jo 14343
Pablo Lopez

'''

class Mancala:


    def __init__(self):
        self.table = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        self.plyrTurn = 1
        self.frstMove = None


    def jugada(self,posicion_de_jugada):
        stack_de_piezas = self.table[posicion_de_jugada]
        self.table[posicion_de_jugada] = 0
        ultimo_turno = self.distribucion(stack_de_piezas,posicion_de_jugada)
        self.specialMove(ultimo_turno)
        self.nextTurn()


    def distribucion(self, stack, takenPos):
        actualPos = 0
        while stack > 0:
            takenPos += 1

            if (actualPos+takenPos) >= len(self.table):
                actualPos -= 14
            if self.plyrTurn == 1 and (actualPos+takenPos) != 13:
                self.table[actualPos+takenPos] += 1
                stack -= 1

            if self.plyrTurn == 2 and (actualPos+takenPos) != 6:
                self.table[actualPos+takenPos] += 1
                stack -= 1

        ultima_piedra = (actualPos+takenPos)
        return ultima_piedra

    def posibleMove(self):

        posibleMoves = []
        if self.plyrTurn == 1:
            posibleMoves = [0,1,2,3,4,5]
        else:
            posibleMoves = [7,8,9,10,11,12]
        elements_to_delete = []
        for x in posibleMoves:
            if self.table[x] == 0:
                elements_to_delete.append(x)
        
        for x in elements_to_delete:
            posibleMoves.remove(x)

        return posibleMoves


    def specialMove(self, finalPos):

        # Jugador 1
        if self.plyrTurn == 1: 
            if finalPos == 6:
                self.nextTurn()
            elif self.table[finalPos] == 1:
                self.table[finalPos] = 0
                self.table[6] += 1
                self.table[6] += self.table[12-finalPos]
                self.table[12-finalPos] = 0
        # Jugador 2
        else:
            if finalPos == 13:
                self.nextTurn()
            elif self.table[finalPos] == 1:
                self.table[finalPos] = 0
                self.table[13] += 1
                self.table[13] += self.table[12-finalPos]
                self.table[12-finalPos] = 0



    def nextTurn(self):
        next_player = self.plyrTurn % 2
        self.plyrTurn = next_player + 1



    def get_ganador(self, end=False):
        plyr1 = sum(self.table[0:7])
        plyr2 = sum(self.table[7:14])
        if end:
            print('Puntaje del jugado: {}'.format(plyr2))
            print('Puntaje del AI: {}'.format(plyr1))

        if (plyr1 > plyr2):
            return 1
        elif(plyr1 < plyr2):
            return 2
        else:
            return 0


    def getFrstMove(self):
        return self.frstMove


    def setFrstMove(self, move_1):
        self.frstMove = move_1

    def print_table(self):
        return self.table

    def __str__(self):
        tabl_reverse = self.table[::-1]
        table_en_string = " " + str(tabl_reverse[8:]) + "\n"
        table_en_string += str(self.table[6])+ "                  "+ str(self.table[13]) + "\n"
        table_en_string += " " + str(self.table[7:13])
        return table_en_string