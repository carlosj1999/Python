def read_int(prompt, min, max):
        try:
            if not (min <= prompt <= max):
                raise AttributeError(f"the value is not within permitted range ({min}..{max})")
            else:
                return prompt
        except ValueError:
            print("Error: Wrong input")
    

v = read_int("a", -10, 10)
print("The number is:", v)
