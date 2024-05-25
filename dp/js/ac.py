def allConstruct(s, d):
    if s == '': return ['']
    result = []
    for word in d:
        if word in s and s.index(word) == 0:
            remain = s[len(word):]
            ways = allConstruct(remain, d)
            res = [ word+' ' + w for w in ways ]
            for r in res:
                result.append(r)
    return result
x = allConstruct('purple',['purp','p','ur','le','purpl'])

print(x)
