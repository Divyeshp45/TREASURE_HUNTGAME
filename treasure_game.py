print('''                  

                                              _____            ____   ______  __     __ ______
                             \      _      / |____   | |     |       |    |  | \___/ | |___
                              \    / \    /  |____|  | |___  |       |    |  |       | |___|   
                               \__/   \__/   |_____  |_____| |____   |____|  |       | |______  
                                                           _____________                             
                                                           |____   ____|  ____
                                                                |  |     |    |
                                                                |  |     |    |
                                                                |__|     |____|          
                                   __      __
                                  |  \    /  |    ____   _____      _________      ______      __      __   _______
                                  |   \__/   |    \   |__|   /      |             /      \     | \    / |  |
                                  |          |     \__    __/       |    ____    /   __   \    |  \__/  |  |____
                                  |          |        |  |          |    |  |   /   |  |   \   |        |  |
                                  |          |        |  |          |____|  |   |___|  |___|   |        |  |_______   
                        _____________     __________        __________   _______       ________                 _________    ________
                       |             |   |    _     |      |            |       |     /           |          |  |        \  |
                       |____     ____|   |   |_|    |      |_____       |_______|    |            |          |  |        |  |_____
                            |   |        |    __    )      |     |      |       |    \_________   |          |  |    ___ /  |_____|
                            |   |        |   |  \   \      |_____|      |       |              \  |          |  |    \      |
                            |   |        |   |   \   \     |            |       |               | \          /  |      \    |
                            |___|        |   |    \___\    |__________  |       |     _________/   \________/   |        \  |_________
                                                ___        ___________
                     |  |___|  |  |  |  |   |  |   \    |      | |
                     |  ______ |  |  |  |   |  |    \   |      | |
                     |  |    | |  |  |__|   |  |     \__|      | |
                     |  |    | |  \         /  |               | |
                     |  |    | |   \_______/   |               | |
''')










print("Welcome to the Treasure Island")
print("Your Mission is to find the Treasure")
direct=input('''You are into a dense forest and suddenly you stumbled upon a cross road.
                    
                    
               Choose which direction to Move Left or Right \n''').lower()


if direct=="left" :
     lake=input('''You reached to a shore of  a lake on the other end there is a Small Cave.
                A ferry man is aproaching Towards You.....
               
               
               Choose if you want to wait or swim and cross the lake?,Enter wait or swim \n''').lower()
     
     if  lake=="wait" :
          riddle=input('''HERE ferry man asks you a riddle if you are able to solve it then you can ride along.
               
               
               What has to be broken before You can eat it?? 
                                                          hint:one has white outside or inside''').lower()
                                  
     else:
       print('''You were Eaten by crocodile!,GAME OVER!
                                              ''')
     if riddle=="egg" or riddle=="coconut" :
          doors=input('''YOu crossed the lake entered into the cave there You see three doors of red ,blue,yellow.
              Choose anyone \n''').lower()
     
     else:
            print("You got it wrong Think hard and come again!!.  hint:Thing in white shell \n")                                         
     if doors=="red":
               print("YOU die due to fire.GAME OVER!!\n")     
     elif doors=="blue":
               print("There is Monster that ate YOu. GAME OVER!!!\n")  
     else:
               print("You have successfully found the treasure.YOU WIN!!!!")            
                                   
else:
     
     print("You fell into a hidden pit and died instantly .GAME OVER!!") 
             
    

                 
                     


