"""
A cafe has N computers. Several customers come to the cafe to use these computers. A customer will be serviced only if there is
any unoccupied computer at the moment the customer visits the cafe. If there is no unoccupied computer, the customer leaves the cafe.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""
def customersWalkedAway(N,S):

    CompNum=N
    WalkedAwayCount=0
    customerCame=set()
    for customer in S:
        if customer not in customerCame:#came assigned available computer
            if CompNum>0:
                CompNum=CompNum-1
                customerCame.add(customer)
                #print(customerCame)
                
            else:#came but leaving as no computer available
                WalkedAwayCount=WalkedAwayCount+1
                customerCame.add(customer)

        else:

                    CompNum=CompNum+1
                    customerCame.remove(customer)
    return WalkedAwayCount
            
def main():
    N1 = 3
    S1 = "GACCBDDBAGEE"
    print(f"Customers Walked Away for {S1}:",customersWalkedAway(N1, S1)) 

    N2 = 1
    S2 = "ABCBAC"
    print(f"Customers Walked Away for {S2}:", customersWalkedAway(N2, S2))  # Expected output: 2

if __name__ == "__main__":
    main()