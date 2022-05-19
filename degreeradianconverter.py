degree_num = int(input("What is the angle in degrees? "))
degree_num_original = degree_num

# Let's fix the degree so that it's between 0 and 360
while(degree_num > 360):
    degree_num = degree_num - 360

while(degree_num < 0):
    degree_num = degree_num + 360


# for fun, let's supply the reference angle.
if(degree_num >= 270):
    degree_ref = 360 - degree_num
elif(degree_num >= 180 and degree_num < 270):
    degree_ref = degree_num - 180
elif(degree_num >= 90 and degree_num < 180):
    degree_ref = 180 - degree_num
else:
    degree_ref = degree_num

# print out the information in degrees that has been accomplished.
print("Angle between 0 - 360: " + str(degree_num) + " degrees")
print("Reference Angle: " + str(degree_ref) + " degrees")


# convert the original degree_num, the degree_num2, and the ref_num to radians. Leave pi in tact.
def convert(dec_num):
    dec_num = dec_num / 360 * 2
    return dec_num
    
print("Original Angle in Radians: " + str(convert(degree_num_original)) + "π")
print("Angle between 0 and 2π: " + str(convert(degree_num)) + "π")
print("Reference Angle: " + str(convert(degree_ref)) + "π")
