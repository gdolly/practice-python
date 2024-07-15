class MaxProductSubarray:
    # def __init__(self):
    def max_product(self, input):
        result = []
        for i, n in enumerate(input):
            r = range(1, i + 1)
            print("n, ", n, "r===", r)
            for j in r:
                print("j==", j,"res",result[j*-1], "n=",n)
                result.append(result[j*-1] * n)
                print(result)
            result.append(n)
            print(result)
        return max(result)


if __name__ == '__main__':
    # product = MaxProductSubarray().max_product([2, 3, -2, 4])
    product = MaxProductSubarray().max_product([-2, 0, -1])
    print(product)
