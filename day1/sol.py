
def main():
    f= open('input.txt', 'r')
    content= f.readlines()
    sol = 0 
    for x in content: 
        sol = sol + int(x)
    f.close()
    print('Result is: ', sol)

if __name__== "__main__":
  main()
