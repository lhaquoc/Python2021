# def factors(n):
#     results = []
#     for k in range(1, n + 1):
#         if n % k == 0:
#             results.append(k)
#     return results


def factors(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


print(factors(50))
