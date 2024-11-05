# write your code here
def split_name(full_name):
    first_name = ""
    for i in range(0, len(full_name)):
        if full_name[i] == " ":
            #write here your code to exit the loop
            return (first_name, full_name[i + 1:])
        else:
            first_name += full_name[i]



print (split_name("Quinten Vanderpooten"))