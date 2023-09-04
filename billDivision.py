'''
Problem 27. Bill Division. Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay 
for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is 
correct.

For example, assume the bill has the following prices: bill = [2,4,6]. Anna declines to eat item k=bill[2] which costs 6. 
If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of bill=[2], he will calculate 
(2+4+6)/2=6. In the second case, he should refund 3 to Anna.
https://www.hackerrank.com/challenges/bon-appetit/problem
'''
#!/bin/python3

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    TotalAmount = 0
    for values in bill:
        TotalAmount += values
    if k < len(bill) and k > -1:
        ActualCost = int((TotalAmount - bill[k])/2)
        if ActualCost == b:
            print("Bon Appetit")
        else:
            print(b - ActualCost)

if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
