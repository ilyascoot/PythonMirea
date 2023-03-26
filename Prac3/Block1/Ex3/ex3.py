from ex3_1 import GLOBAL_VAR

global GLOBAL_VAR

print(GLOBAL_VAR)

GLOBAL_VAR = 42

def printGllobal_Var():
    print(GLOBAL_VAR)

printGllobal_Var()