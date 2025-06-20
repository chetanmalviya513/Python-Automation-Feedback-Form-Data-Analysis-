
#HRDC Feedback Form Data Analysis & Visualization

#Libreary Import
import pandas as pd
import matplotlib.pyplot as plt


# Import csv file
res_sheet = pd.read_csv(r"C:\Users\abc\Desktop\feedback\feedback.csv")

# Import 13 Ques
# Did you find the course useful ?
# Online Reference Material
# Resource Persons
# Duration
# Broadening the approach
# Inspiring
# Skill Development
# Did you acquire sufficient skill in developing e-content using generic tools?
# Did you acquire sufficient knowledge regarding your role and responsibilities in higher education?
# Do you have the confidence in developing research proposal and writing research articles?
# Curriculum of the Course
# How would you rate the overall programme





# 1. Did you find the course useful ?

course_useful = "Did you find the course useful ?"
course_useful_res = res_sheet.filter(like=course_useful)

course_res = course_useful_res.values.tolist()

# Merge onlion_res all list in one list
course_list = []
for sublist in course_res:
    course_list.extend(sublist)

#course_list

# onlion res merge

Yes = 0
No = 0
Some_extent = 0

for i in course_list:
    if i == "Yes":
         Yes = Yes + 1
    if i == "No":
        No = No + 1
    if Some_extent == "Some extent":
        Some_extent = Some_extent + 1

total_cat = Yes + No + Some_extent


# Category data percentage show

Yes = (Yes*100)/total_cat
No = (No*100)/total_cat
Some_extent = (Some_extent*100)/total_cat

x_axis = ["Yes", "No","Some extent"]
y_axis=[Yes,No,Some_extent]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("1.Did you find the course useful ?", pad=30, fontsize= 20)

# Show the graph
plt.show()




#--------------------------**---------------------------------------------




# 2.Online Reference Material

onlion_ref_mat = "Online Reference Material"
onlion_res_mat_chunk = res_sheet.filter(like=onlion_ref_mat)


#onlion_res_mat_chunk

type(onlion_res_mat_chunk)
         

onlion_res = onlion_res_mat_chunk.values.tolist()

# Merge onlion_res all list in one list
onlion_res_merge = []
for sublist in onlion_res:
    onlion_res_merge.extend(sublist)

#onlion_res_merge

sufficient = 0
not_so_Sufficient = 0
Not_at_all_Sufficient = 0
 
for i in onlion_res_merge:
    if i == "Sufficient":
        sufficient = sufficient + 1
    if i == "Not so Sufficient":
        not_so_Sufficient = not_so_Sufficient + 1
    if i == "Not at all Sufficient":
        Not_at_all_Sufficient = Not_at_all_Sufficient +1
    

total_onlion_res = not_so_Sufficient + sufficient + Not_at_all_Sufficient


# category data percentage show
sufficient_res = (sufficient*100)/total_onlion_res
not_so_Sufficient_res = (not_so_Sufficient*100)/total_onlion_res


x_axis = ["Sufficient", "Not so Sufficient","Not at all Sufficient"]
y_axis=[sufficient_res,not_so_Sufficient_res,Not_at_all_Sufficient]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("2.Online Reference Material", pad=30, fontsize= 20)

# Show the graph
plt.show()


#--------------------------**-----------------------------------


# 3. Resource Persons 

question = "Resource Persons"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Very Competent":
        first = first + 1
    if i == "Competent":
        second = second + 1
    if i == "Not so Competent":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Very Competent", "Competent", "Not so Competent"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("3. Resource Persons", pad=30, fontsize= 20)

# Show the graph
plt.show()


#------------------------**---------------------------------



# 4. Duration 

question = "Duration"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Too long":
        first = first + 1
    if i == "Too Short":
        second = second + 1
    if i == "Just all right":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Too long", "Too Short", "Just all right"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("4. Duration", pad=30, fontsize= 20)

# Show the graph
plt.show()


#-------------------------**----------------------



# 5. Broadening the approach

question = "Broadening the approach"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "To a great extent":
        first = first + 1
    if i == "To some extent":
        second = second + 1
    if i == "Not at all":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["To a great extent", "To some extent", "Not at all"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("5. Broadening the approach", pad=30, fontsize= 20)

# Show the graph
plt.show()



#-------------------------**-------------------------



# 6. Inspiring

question = "Inspiring"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "To a great extent":
        first = first + 1
    if i == "To some extent":
        second = second + 1
    if i == "Not at all":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["To a great extent", "To some extent", "Not at all"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("6. Inspiring", pad=30, fontsize= 20)

# Show the graph
plt.show()



#-----------------------------**--------------------------



# 7. Skill Development

question = "Skill Development"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Adequate":
        first = first + 1
    if i == "No so adequate":
        second = second + 1
    if i == "Not at all Adequate":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Adequate", "No so adequate", "Not at all Adequate"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("7. Skill Development", pad=30, fontsize= 20)

# Show the graph
plt.show()



#--------------------------**----------------------------



# 8. Did you acquire sufficient skill in developing e-content using generic tools?

question = "Did you acquire sufficient skill in developing e-content using generic tools?"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Adequate":
        first = first + 1
    if i == "No so adequate":
        second = second + 1
    if i == "Not at all Adequate":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Adequate", "No so adequate", "Not at all Adequate"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("8. Did you acquire sufficient skill in developing e-content using generic tools?", pad=30, fontsize= 20)

# Show the graph
plt.show()



#-------------------------**----------------------



# 9. Did you acquire sufficient knowledge regarding your role and responsibilities in higher education?

question = "Did you acquire sufficient knowledge regarding your role and responsibilities in higher education?"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Adequate":
        first = first + 1
    if i == "No so adequate":
        second = second + 1
    if i == "Not at all Adequate":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Adequate", "No so adequate", "Not at all Adequate"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("9. Did you acquire sufficient knowledge regarding your role and responsibilities in higher education?", pad=30, fontsize= 20)

# Show the graph
plt.show()



#------------------------**--------------------------



# 10. Do you have the confidence in developing research proposal and writing research articles?

question = "Do you have the confidence in developing research proposal and writing research articles?"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "To a great extent":
        first = first + 1
    if i == "To some extent":
        second = second + 1
    if i == "Not at all":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["To a great extent", "To some extent", "Not at all"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("10. Do you have the confidence in developing research proposal and writing research articles?", pad=30, fontsize= 20)

# Show the graph
plt.show()



#-----------------------------**---------------------------------



# 11. Curriculum of the Course

question = "Curriculum of the Course"
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Sufficient":
        first = first + 1
    if i == "Not Sufficient":
        second = second + 1
    if i == "Not at all Sufficient":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Sufficient", "Not Sufficient", "Not at all Sufficient"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("11. Curriculum of the Course", pad=30, fontsize= 20)

# Show the graph
plt.show()



#------------------------------**------------------------------



# 12. How would you rate the overall programme 

question = "How would you rate the overall programme "
question = res_sheet.filter(like=question)


question = question.values.tolist()

# Merge onlion_res all list in one list
List = []
for sublist in question:
    List.extend(sublist)

first = 0
second = 0
third = 0

for i in List:
    if i == "Good":
        first = first + 1
    if i == "Very Good":
        second = second + 1
    if i == "Poor":
        third = third + 1

total = first + second + third


# category data percentage show
first = (first*100)/total
second = (second*100)/total
third = (third*100)/total


x_axis = ["Good", "Very Good", "Poor"]
y_axis=[first,second,third]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("12. How would you rate the overall programme ", pad=30, fontsize= 20)

# Show the graph
plt.show()




#-------------------**--------------------------