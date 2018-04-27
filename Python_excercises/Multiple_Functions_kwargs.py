
#Define a function called MultipleFunc with three Arguments
def MultipleFunc(var_A, var_B, **kwargs):

#Check if the keyword action kwargs for options was triggered,
#if the value triggered was "sum",return the addition of both variables
    if kwargs.get("action") == "sum":
        print("The sum is: %d" %(var_A + var_B))

#Check if the keyword "Returnvar" option for kwargs was triggered,
#if the value triggered is "varA",return the value for VarA
#this works as a getter function for var A
    if kwargs.get("Returnvar") == "varA":
        return var_A
#Check if the keyword "Returnvar" option for kwargs was triggered,
#if the value triggered is "varB",return the value for VarB
#this works as a getter function for var B
    if kwargs.get("Returnvar") == "varB":
        return var_B

#Variable to hold the results form the fucntion
result = MultipleFunc(1,2, kwargs = "sum",Returnvar="varB")
print("Result: %d" %(result))