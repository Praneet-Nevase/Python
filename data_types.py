agent_number = 5
speed_rating = 8.5
is_active = True
name=input("Enter your real name, Agent")
print("Name",name,"Data type --",type(name))
print("agent_number", agent_number,"Data type --",type(agent_number))
print("Speed", speed_rating,"Data type --",type(speed_rating))
print("Is active?", is_active,"Data type --",type(is_active))
first_three = name[0:3]
last_letter = name[-1]
code_name = first_three + last_letter
print("Your code name is",code_name)

reverse_name=name[::-1]
print("Reversed name is", reverse_name)

badge=("Agent" + code_name.upper())
print("Code_name", badge)