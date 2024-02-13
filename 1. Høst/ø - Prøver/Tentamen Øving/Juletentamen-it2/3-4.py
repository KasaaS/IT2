def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal > bortemaal:
        return hjemmelag
    elif hjemmemaal < bortemaal:
        return bortelag
    else:
        return "uavgjort"
    


print(vinnerlag("brann", "molde", 2, 3))
print(vinnerlag("brann", "molde", 3, 2))
print(vinnerlag("brann", "molde", 2, 2))