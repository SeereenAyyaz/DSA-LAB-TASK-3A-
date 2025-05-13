def permute(s):
    def backtrack(start, end, path, results):
        if start == end:
            results.append("".join(path))
        for i in range(start, end):
            if i > start and s[i] == s[start]:
                continue 
            path[start], path[i] = path[i], path[start]
            backtrack(start + 1, end, path, results)
            path[start], path[i] = path[i], path[start] 

    results = []
    backtrack(0, len(s), list(s), results)
    return results

# test case
print(permute("ABC"))
