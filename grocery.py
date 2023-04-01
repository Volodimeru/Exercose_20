def main():
    d = {}
    while True:
        try:
            z=input("").lower()
            if z in d:
                d[z] +=1
            else:
                d[z] = 1
        except EOFError:
            break
    s=sorted(d)
    for z in s:
        print(d[z], z.upper())
main()