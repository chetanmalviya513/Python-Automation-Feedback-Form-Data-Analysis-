import pandas as pd
import matplotlib.pyplot as plt


# Import csv file
res_sheet = pd.read_csv(r"C:\Users\abc\Desktop\feedback\feedback.csv")



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

for i in course_list:
    if i == "Yes":
         Yes = Yes + 1
    if i == "No":
        No = No + 1

total_cat = Yes + No


# Category data percentage show

Yes = (Yes*100)/total_cat
No = (No*100)/total_cat

x_axis = ["Yes", "No"]
y_axis=[Yes,No]

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

for i in onlion_res_merge:
    if i == "Sufficient":
        sufficient = sufficient + 1
    if i == "Not so Sufficient":
        not_so_Sufficient = not_so_Sufficient + 1

total_onlion_res = not_so_Sufficient + sufficient


# category data percentage show
sufficient_res = (sufficient*100)/total_onlion_res
not_so_Sufficient_res = (not_so_Sufficient*100)/total_onlion_res


x_axis = ["Sufficient", "Not so Sufficient"]
y_axis=[sufficient_res,not_so_Sufficient_res]

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







# 3.Resource Persons

word_match = "Resource Persons"
question = res_sheet.filter(like=word_match)
         
# data list convert
ques_no = question.values.tolist()

# Merge onlion_res all list in one list
que_res = []
for sublist in ques_no:
    que_res.extend(sublist)

#onlion_res_merge

Competent = 0
Very_Competent = 0

for i in que_res:
    if i == "Competent":
        Competent = Competent + 1
    if i == "Very Competent":
        Very_Competent = Very_Competent + 1

total_res = Competent + Very_Competent


# category data percentage show
res_first = (Competent*100)/total_res
res_second = (Very_Competent*100)/total_res


x_axis = ["Competent","Very Competent"]
y_axis=[res_first,res_second]

# to plot bar graph
plt.bar(x_axis, y_axis, color="blue", width=0.9)


# Set the y-axis tick locations and labels
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Add labels and title
plt.xlabel("")
plt.ylabel("Values in Percentage %")
plt.title("3.Resource Persons", pad=30, fontsize= 20)

# Show the graph
plt.show()