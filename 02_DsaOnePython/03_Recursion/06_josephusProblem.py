'''
n = [ A, B, C, D, E, F, G ]==> 7
k = 3
_ =  to Kill 

      i     _      
-   [ A, B, C, D, E, F, G ] ==> 0 -> 3 <- Answer          ( 0 + 3 ) % 7  =  3  

            _
-   [ D, E, F, G, A, B ] ==> 3 -> 0                       ( 1 + 3 ) % 7  =  4

            _
-   [ G, A, B, D, E ] ==> 0 -> 3                          ( 2 + 3 ) % 7  =  5  

            _      
-   [ D, E, G, A ] ==> 1 -> 0                             ( 3 + 3 ) % 7  =  6

            _
-   [ A, D, E ] ==> 1 -> 1                                ( 4 + 3 ) % 7  =  0

      _
-   [ A, D ] ==> 0  -> 1                                  ( 5 + 3 ) % 7  =  1  
  

-   [ D ] ==>                                             ( 6 + 3 ) % 7  =  2  

'''

def josephusProblem(n,k):
    if n == 1:
        return 0

    return (josephusProblem(n-1,k) + k) % n


arr = 7
k = 3
print('Safe place is: ',josephusProblem(arr,k))
