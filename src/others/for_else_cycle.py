
for x in range(3):
    # This statment will never be executed
    if x == 100:
        break
    print(x)
else:
    print("The cycle was executed without interrupts")
