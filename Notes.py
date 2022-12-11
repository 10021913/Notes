def generalNotes():
    """
    General Notes:
    - 

    Concepts to Learn:
    - Turing Machines

    Notes To Create:
     - output 10^9 + 7
     - Trees/Binary Tree
    """



# Main notes
def competativeProgramingNotes():
    """
    Topic: Bitwise XOR Operation
    
    Explantion: 
        A bitwise XOR is a binary operation that takes two bit patterns of equal length and 
    performs the logical exclusive OR operation on each pair of corresponding bits. The 
    result in each position is 1 if only one of the bits is 1, but will be 0 if both are 0 or both are 1


        0101 (decimal 5)
    XOR 0011 (decimal 3)
      = 0110 (decimal 6)
    
    Applications:
        encryption, compression, graphics, communications over 
    ports/sockets, embedded systems programming and finite state machines

    """
    # How to perform XOR in python
    print(5 ^ 3) # resutls in 6





    """
    Topic: output 10^9 + 7

    Explantion: 
        when numbers are too large to compute, the mod of the number is used when compution. 
        Saves space, time and in some languages prevents an overflow error
        Properties: 
            ( a + b) % c = ( ( a % c ) + ( b % c ) ) % c
            ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c
            ( a – b) % c = ( ( a % c ) – ( b % c ) ) % c
            ( a ^ b) % x = ( ( a % c ) ^ B ) % c

    Continue : https://www.youtube.com/watch?v=-OPohCQqi_E&ab_channel=Errichto 
    # Create (10 ^ 9) + 7 function for all the functions in the video
    """
    # How to perform mod 10^9 + 7 with multiplication:
    answer = 1
    for a in range(100000):
        answer = (answer  * 2) % 1000000007
    print(answer) # answer would be a number from 0 - 9

    # How to perform mod 10^9 + 7 with 


    


