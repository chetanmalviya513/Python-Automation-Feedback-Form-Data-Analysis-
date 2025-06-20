#HRDC Faculty Rating


import pandas as pd
import matplotlib.pyplot as plt

#Import csv file
feedback_sheet = pd.read_csv(r"C:\Users\abc\Desktop\feedback\feedback.csv")

#print csv file
#feedback_sheet


#----------------------------**-------------------------------------


#Ques data
# 1. Communication Skill 2. Quality of lecture 3. Competency in Subject 4. Usefulness of Topic/s and other 13 Question chunk


# Communication skill chunk

communication_to_match = "Communication Skill"
chunk_communication = feedback_sheet.filter(like=communication_to_match)

#chunk_communication qualitative data convert quantitative data

a = chunk_communication.replace("5 (Very effective)",5)
b = a.replace("4 (Effective)",4)
c = b.replace("3 (Satisfactory)",3)
d = c.replace("2 (Ineffective)",2)
e = d.replace("1 (Netural)",1)

# store variable
communication_data = e

# row and column exchange - > (Transpose)
communication_res = communication_data.transpose()

communication_sum = communication_res.sum(axis=1)



#communication_sum

#feedback_sheet
#chunk_communication
#communication_data
#communication_res



#--------------------------**---------------------------




# Quality of lecture

match_to_column = "Quality of lecture"
chunk_quality = feedback_sheet.filter(like=match_to_column)

#chunk_communication qualitative data convert quantitative data

a = chunk_quality.replace("5 (Very Good)",5)
b = a.replace("4 (Good)",4)
c = b.replace("3 (Satisfactory)",3)
d = c.replace("2 (Ineffective)",2)
e = d.replace("1 (Netural)",1)

# store variable
quality_clean_data = e

# row and column exchange - > (Transpose)
quality_transpose = quality_clean_data.transpose()

quality_sum = quality_transpose.sum(axis=1)

#quality_sum





#--------------------------**-----------------------------------




# Competency in Subject

match_to_column = "Competency in Subject"
chunk_compentency = feedback_sheet.filter(like=match_to_column)

#chunk_compentency qualitative data convert quantitative data


#chunk_compentency

a = chunk_compentency.replace("5 (Very Competent)",5)
b = a.replace("4 (Competent)",4)
c = b.replace("3 (Satisfactory)",3)
d = c.replace("2 (Ineffective)",2)
e = d.replace("1 (Netural)",1)



# store variable
compentency_clean_data = e

# row and column exchange - > (Transpose)
compentency_transpose = compentency_clean_data.transpose()

compentency_sum = compentency_transpose.sum(axis=1)

#compentency_sum



#----------------------------**------------------------------




# Usefulness of Topic/s

match_to_column = "Usefulness of Topic/s"
chunk_usefulness = feedback_sheet.filter(like=match_to_column)

#chunk_Usefulness of Topic/s qualitative data convert quantitative data


a = chunk_usefulness.replace("5 (Very Useful)",5)
b = a.replace("4 (Useful)",4)
c = b.replace("3 (Satisfactory)",3)
d = c.replace("2 (Not Useful)",2)
e = d.replace("1 (Netural)",1)



# store variable
usefulness_clean_data = e

# row and column exchange - > (Transpose)
usefulness_transpose = compentency_clean_data.transpose()

usefulness_sum = compentency_transpose.sum(axis=1)

type(usefulness_sum)




#---------------------------**--------------------------





#feedback_sheet Faculty Name store in dataframe

type(usefulness_sum)
chunk_compentency
chunk_communication

mylist = []
for i in chunk_communication:
    mylist.append(i)

df = pd.Series(mylist)

faculty_data = pd.DataFrame({"Faculty_text":df})

faculty_data.head()

# #faculty.Faculty_text.str.extract(r'\[(.*?)\(')
faculty = faculty_data.Faculty_text.str.extract(r"\[(.*?)\(")

faculty_name = []
for i in faculty[0]:
    faculty_name.append(i)

#faculty_name



#------------------------**---------------------------

# Create Dataframe 



communication_list = communication_sum.values.tolist()
quality_list = quality_sum.values.tolist()
competency_list = compentency_sum.values.tolist()
usefulness_list = usefulness_sum.values.tolist()
#faculty_name




#DataFrame convert in all file

feedback_dataframe = pd.DataFrame({"faculty_name":faculty_name,"Communication":communication_list,"Quality":quality_list,"Competency":competency_list,"Usefulness":usefulness_list})

feedback_dataframe



#feedback_sum = feedback_dataframe.sum(axis=1)

# feedback_sum

# faculty_rating = feedback_sum/46/4



#-------------------------------**------------------------------

# Faculty average Rating Calculate

feedback = feedback_dataframe.set_index("faculty_name")[['Communication', 'Quality', 'Competency', 'Usefulness']].sum(axis=1)/46/4


#-------------------------------**----------------------------


# Data Visulization

# Plotting the bar graph
plt.figure(figsize=(12, 6))
bars = feedback.plot(kind='bar')
plt.title('Average Ratings by Faculty')
plt.xlabel('Faculty')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
plt.tight_layout()
plt.show()



#-----------------------------**-------------------------------------