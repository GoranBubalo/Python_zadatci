kubovi = [{number : number ** 3} if number % 3 == 0 else {number:number} for number in range(1,11) ] 
print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9:
# 729}, {10: 10}]