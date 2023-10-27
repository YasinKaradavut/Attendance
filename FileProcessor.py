def get_people_list(file_name="People.txt"):
    people_list=[]
    with open(file_name,"r",encoding="utf-8") as people_file:
        people_list=people_file.readlines()
    
    return people_list
def add_people_list(new_people):
    if new_people=="":
        return 0
    with open("People.txt" , "a" , encoding= "utf-8") as people_file:
        new_people="\n"+new_people
        people_file.write(new_people)
def delete_people_list(person):
    people=get_people_list()
    with open("People.txt" , "w" , encoding= "utf-8") as people_file:
        for i in people:
            
            if i==person+"\n" or i== person:
                pass
            else: 

                people_file.write(i)

