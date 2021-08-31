from JaGuGae_w3_04 import Student

assistant = []
num_assistant = int(input("Input the number of assistant: "))

for i in range(num_assistant):
    if i == 0:
        new_name = input("Please enter a name: ")
        new_id = int(input("Please enter an id: "))
    else:
        new_name = input("Please enter another name: ")
        new_id = int(input("Please enter another id: "))
    assistant.append(Student(new_name, new_id))

for j in range(num_assistant):
    print(j, assistant[j].get_name(), assistant[j].get_id())