def get_bordered_str(arg):
    result = ""
    sep = "*"
    length = len(arg)
    result = result + (sep * (length + 4) + "\n")
    result = result + (sep + " " + arg + " " + sep + "\n")
    result = result + (sep * (length + 4))
    return result

print(get_bordered_str("Hello, World!"))
print(get_bordered_str("323"))
