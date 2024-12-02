def remove_empty_lines(source, destination):
    with open(source, 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    
    with open(destination, 'w', encoding="utf-8") as file:
        for line in lines:
            if line != "\n":
                file.write(line)
                

#remove_empty_lines("input.txt", "output.txt")