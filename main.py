def addition(mat1, mat2, row, col):
    
    res = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    
    for i in range(row):
        for j in range(col):
            res[i][j] = mat1[i][j] + mat2[i][j]
            print(res[i][j], end=" ")
        print("\n")

def subtraction(mat1, mat2, row, col):
    
    res = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    
    for i in range(row):
        for j in range(col):
            res[i][j] = mat1[i][j] - mat2[i][j]
            print(res[i][j], end=" ")
        print("\n")
        
def multiplication(mat1, mat2, row, col):
    
    res = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    
    for i in range(row):
        for j in range(col):
            res[i][j] = mat1[i][j] * mat2[i][j]
            print(res[i][j], end=" ")
        print("\n")
        
def transpose(mat, row, col):
    
    res = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    
    for i in range(col):
        for j in range(row):
            res[i][j] = mat[j][i]
            print(res[i][j], end=" ")
        print("\n")
        

mat_1 = []
mat_2 = []

row = int(input("\nEnter the number of rows for the matrix:"))
col = int(input("\nEnter the number of columns for the matrix:"))

print("\nEnter the values for first matrix-\n")
for i in range(row):
    z = []
    for j in range(col):
        num = int(input("Enter the value [%d] [%d]:"%(i, j)))
        z.append(num)
    mat_1.append(z)
    
print("\nEnter the values for second matrix-\n")
for i in range(row):
    z = []
    for j in range(col):
        num = int(input("Enter the value [%d] [%d]:"%(i, j)))
        z.append(num)
    mat_2.append(z)
    
print("\n\nFirst matrix:\n")
for i in range(row):
    for j in range(col):
        print("%d"%(mat_1[i][j]), end=" ")
    print("\n")
    
print("Second matrix:\n")
for i in range(row):
    for j in range(col):
        print("%d"%(mat_2[i][j]), end=" ")
    print("\n")

def main():
    try: 
        while 1:
            print("======= MAIN MENU =======")
            print("What operation do you want to perform?")
            print("1.Addition of matrices\n2.Subtraction of matrices")
            print("3.Multiplication of matrices\n4.Transpose of matrix")
            print("5.Exit")
            choice = int(input("Please enter your choice:"))
            print("-------------------------")
            
            if choice == 1:
                print("\nAddition of matrices:")
                addition(mat_1, mat_2, row, col)
                
            elif choice == 2:
                print("\nSubtraction of matrices:")
                subtraction(mat_1, mat_2, row, col)
                
            elif choice == 3:
                print("\nMultiplication of matrices:")
                multiplication(mat_1, mat_2, row, col)
                
            elif choice == 4:
                print("\nTranspose of first matrix:")
                transpose(mat_1, row, col)
                print("\nTranspose of second matrix:")
                transpose(mat_2, row, col)
                
            elif choice == 5:
                exit(0)
                
            else:
                print("Invalid choice! Please try again.")

    except ValueError:
        print("Please enter only numeric values!")
        main()

main()
