def remove_duplicate_lines(source, destination):
    with open(source, 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    
    with open(destination, 'w', encoding="utf-8") as file:
        last_line = ""
        for line in lines:
            if line != last_line:
                file.write(line)
                last_line = line
                
