Bonus homework 10.1: CSV files
This homework is not mandatory.

Remember the example in the bonus section above?

Tina,23,female
Jakob,35,male
Barbara,44,female

Your task is to create a Python program, that will go through this CSV file and print the following text in the Terminal:

Tina is 23 years old and female

Jakob is 35 years old and male

Barbara is 44 years old and female

Hint: You might need a string method called split():
row_data = row.split(",")
The row_data will consist of three pieces of data: name, age and gender. 
You will be able to access each of these pieces of data by its index number, for example, a 
person's name is row_data[0] and gender is row_data[2].

This is possible because row_data is a data structure called list. You will learn more about lists in the next lesson.

When you complete the homework, store it on GitHub and share the link to it on Slack.