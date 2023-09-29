#weight conversion
weight_in_pounds = float(input("Enter a weight in Pounds (lb): "))
kilogram_conversion = weight_in_pounds *  0.45359237

print("Weight in Kilogram (kg) = " , str(round(kilogram_conversion,3)))

print("===============================================================================")
#length conversion
length_in_miles = float(input("Enter a length in Miles (mi): "))
kilometer_conversion = (length_in_miles) * 1.609344

print("Length  in Kilometers (km) = " , str(round(kilometer_conversion,3)))

print("===============================================================================")
#temperature conversion
temp_in_F = float(input("Enter a temperature in Fahrenheit (°F): "))
celsius_conversion = ((temp_in_F - 32) *0.55555555555)
celsius = str(round(celsius_conversion,3))

print("Temperature in Celsius (°C) = " , celsius + "°")

print("===============================================================================")
#average age of students

age1=int(input("Age of Student 1: " ))
age2=int(input("Age of Student 2: " ))
age3=int(input("Age of Student 3: " ))
age4=int(input("Age of Student 4: " ))
age5=int(input("Age of Student 5: " ))
age6=int(input("Age of Student 6: " ))
age7=int(input("Age of Student 7: " ))
age8=int(input("Age of Student 8: " ))
age9=int(input("Age of Student 9: " ))
age10=int(input("Age of Student 10: " ))

result = (age1+age2+age3+age4+age5+age6+age7+age8+age9+age10)/10
print("\n")
print ("The average age of the student is : " , str(round(result, 3)))

print("===============================================================================""\n")

title = ('"Reality is Often Dissapointing"')

#name of the characters
name_1 = "SLeigh"
name_2 = "Ligmark"
name_3 = "Paperbag"
name_4 = "Nokia"
name_5 = "Rizzler"
#place
dungeon = "Nowhere to be Found"
#combat arts
combat_art1 = "Fiery Explosion"
combat_art2 = "Dragon's Breath"
combat_art3 = "Power of Friendship"
#armor
chestplate = "Chestplate of Coolness"
leggings = "Leggings of the Alphas"
helmet = "Helmet of Rizz"
boots = "Boots of Grace"
#tools
sword = "The Penetrator"
ring = "Ring of Rizz"

print(title)
print("\n")
input_user= input("Press enter to see the full story....""\n")
print("\n"f"""After a crazy grinding in the forest. The party of "{name_1}", "{name_2}" and "{name_3}" decided 
that they are now ready to fight the main boss. So, they packed their things and moved on. 
Upon arriving at the dungeon of "{dungeon}", They encountered their first problem, 
that is to find another member to complete the party of 4.That's when a ladyboy named "{name_4}"
approached them and asked if she can join, the three agreed.

Now that the problem has been solved. The four entered the dungeon and completed the 3 phases of the 
dungeon. Immediately after that, they have arrived at the boss room. They were curious what the boss 
would like, so they immediately entered the room. To their suprise, the room was oddly empty and 
silent; the party was confused. After some time, a rumbled was heard and a dragon emerged from the 
ground. "{name_4}" wasted no time and immediately casted a spell called "{combat_art1}", this made 
the whole area burn like stove but no damage was dealt to the dragon, he was furious and casted 
another spell called "{combat_art2}", but still no damage was dealt. This made the three disheartend 
because they knew the enemy was strong. Suddenly, "{name_1}" leaped out of nowhere, along with 
"{name_3}" and "{name_2}". Together, they incanted a magic circle called "{combat_art3}". 
Unfortunately, the dragon just flicked them and they were goners.

Afterwards, the four notices that there was a shadowy figure cloaked in the darkness, that was me 
by the way and my name is "{name_5}". They were suprised, prolly and only because I look cool 
wearing the ultimate armor named "{chestplate}", "{leggings}", "{helmet}" 
and "{boots}". Anyway, I slowly step into the battlefield and summoned my ultimate sword 
"{sword}", buffed by the "{ring}". I was ready to slap this dragon but I woke up from my dream, 
and got slapped by reality once again.""")