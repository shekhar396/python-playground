class BitWise:
    @staticmethod
    def swapVariable():
        # Initial values
        a = 5
        b = 3
        # Swapping values using XOR
        a = a ^ b  # Step 1: a becomes a XOR b
        b = a ^ b  # Step 2: b becomes (a XOR b) XOR b, which simplifies to a
        a = a ^ b  # Step 3: a becomes (a XOR b) XOR a, which simplifies to b

        print("After swapping:")
        print("a =", a)
        print("b =", b)

    @staticmethod
    def swapVariable2():
        a=5
        b=3
        a=a+b
        b=a-b
        a=a-b
        print("After swapping:")
        print("a =", a)
        print("b =", b)



BitWise.swapVariable2()