"""
Name: Jacob Scheetz
Assignment: TEA attack python - Assignment 1
Course: CPS - 472 Computer & Network Security
Professor: Dr. Yao
Date: Febuary 4 2021
File name: Scheetz-AS1.py
===============================================================
Description: 
script that reads in 32 bit unsigned integer plaintext/ciphertext pairs to perform a bruteforce attack on 1 round of the TEA. 
by using a plaintext/ciphertext pair consisting of 32 bits a piece, we essentially reduce TEA's key space in half. By repeatedly guessing
32 bits of the key, this script deduces the remaining 32 bits of the key left.
"""
import ctypes
import time 
import sys

# === Function Definitions ===

#define small modular additions and subtractions to ensure 32 bit unsigned ints
def mod_add(x: int, y: int) -> int:
    return (x + y) & 0xffffffff

def mod_sub(x: int, y: int) -> int:
    return (x - y) & 0xffffffff

# defines the calculations given by class slides to get key1 given 
def guessKey1(pairList: list, x: int, delta: int) -> int:
    return mod_sub(
    mod_sub(pairList[3], pairList[0]) ^ mod_add((pairList[1] << 4) & 0xffffffff, x) ^ mod_add(pairList[1], delta),
    (pairList[1] >> 5) & 0xffffffff)


# === END FUNCTION DEFINITIONS ===



# === BEGIN MAIN ===
def main():
    beginingTime = time.time()

    file = sys.argv[1]
    f = open(file, "r")

    with f:
        delta = 0x9e3779b9 # schedule key constant, given
        firstPair = ([int(i) for i in f.readline().split()]) # take first cipher/plaintext pair from input file
        secondPair = ([int(i) for i in f.readline().split()]) # take first cipher/plaintext pair from input file
        verifyPairs = [[int(i) for i in f.readline().split()] for j in range(10)] # gets next ten lines from file so the assumed key can be verified
        
        for i in range (2 ** 32): # begin cycle of checking key space (2^32)
            subkeyGuess1 = guessKey1(firstPair, i, delta) # calculates k1 for the current subkey and first cipher/plaintext pair
            subkeyGuess2 = guessKey1(secondPair, i, delta)# calculates k1 for the current subkey and second cipher/plaintext pair

            if subkeyGuess1 == subkeyGuess2:
                potentialKey = True # mark that there is a potential match 
                for x in verifyPairs:
                    #check varification cipher/plaintext pairs 10 times to ensure key is valid
                    if guessKey1(x, i, delta) != subkeyGuess1:
                        potentialKey = False
                if potentialKey:
                    endTime = time.time()
                    print("Matching keys have been found and verfied!\nFirst Key (k0) is: {:d}\nSecond Key (k1) is: {:d}\n Runtime of bruteforce was: {:f} seconds".format(
                    i, subkeyGuess1, endTime - beginingTime))
                    exit(0)



if __name__ == "__main__":
    main()
# === END MAIN ===
                    





        

















