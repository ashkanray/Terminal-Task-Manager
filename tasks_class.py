#!/usr/bin/env python

import pickle
import datetime
import pandas as pd
from tabulate import tabulate
import pytz

class Tasks:
    """A list of `Task` objects."""
   
    def __init__(self):
        """Read pickled tasks file into a list"""

        # List of Task objects
        self.tasks = []


    def pickle_tasks(self):
        """Pickle your task list to a file"""
        
        #Creating or opening a pickle file
        dbfile = open('.todo.pickle', 'wb')
      
        #Dumping our tasks list to our file
        pickle.dump(self.tasks, dbfile)  

        dbfile.close()


    def unpickle_tasks(self):
        """UnPickle your task list to a Tasks Object"""

        #Opening our pickle file
        dbfile = open('.todo.pickle', 'rb')     

        #Saving our unpickled tasks list to our self.tasks variable
        self.tasks = pickle.load(dbfile)

        dbfile.close()


    def list(self):
        """Outputs our incomplete tasks to a formatted list"""
        table = []

        #We iterate and include ONLY tasks that are not completed
        for i in self.tasks:
            if i.completed_date == "-":

                #Calcualte the age of the task
                i.task_age()

                #Append the task in proper order to a table list
                table.append([i.id, str(i.age) + "d", str(i.due_date), i.priority, i.name])


        print("")
        #Sharing our full table using pandas, tabulate
        df = pd.DataFrame(table, columns =["ID", "Age", "Due Date", "Priority", "Task"])
        print(tabulate(df, showindex=False, headers=df.columns, numalign="left"))
        print("")


    def report(self):
        """Outputs our full list of tasks to a formatted list with more comprehensive columns"""

        table = []

        #We include ALL tasks in our list, sorted
        for i in self.tasks:

            #Calculate the age of the task
            i.task_age()

            #Append the task in proper order to a table list
            table.append([i.id, str(i.age) + "d", i.due_date, i.priority, i.name, i.created_detail, i.completed_date])


        print("")
        #Sharing our full table using pandas, tabulate
        df = pd.DataFrame(table, columns =["ID", "Age", "Due Date", "Priority", "Task", "Created", "Completed"])
        print(tabulate(df, showindex=False, headers=df.columns, numalign="left"))
        print("")



    def done(self, id_num):
        """Completed specified tasks - saves a completed date"""

        #We obtain the Task object from our tasks list
        item = self.tasks[id_num]

        #We save our completed date using proper CST time format
        chicagoTz = pytz.timezone("America/Chicago") 
        now = datetime.datetime.now(chicagoTz)

        item.completed_date = now.strftime("%a %b %d %H:%M:%S %Z %Y")



    def query(self, keywords):
        """Search our existing tasks list for tasks that match input keywords"""

        table = []
        id_tracker = []

        #Iterate over all of our tasks
        for i in self.tasks:

            #We match the tasks that contain any of the keywords that were input - we also want to avoid duplicates
            #where a task has multiple of the same keywords
            if any(word.lower() in i.name.lower() for word in keywords) and i.id not in id_tracker:

                #Calculate the age of the task
                i.task_age()

                #Append the task in proper order to a table list
                table.append([i.id, str(i.age) + "d", str(i.due_date), i.priority, i.name])

                #Track the ID of the task so we don't append duplicates
                id_tracker.append(i.id)


        print("")
        #Sharing our full table using pandas, tabulate
        df = pd.DataFrame(table, columns =["ID", "Age", "Due Date", "Priority", "Task"])
        print(tabulate(df, showindex=False, headers=df.columns, numalign="left"))
        print("")


    #Appends task objects to our main tasks list
    def add(self, task_obj):
        """Adds a new task object to our main tasks list"""
        self.tasks.append(task_obj)
        
    #Sorts our tasks list based on the following keys, in this order:
    #1) Completed Date
    #2) Due Date
    #3) Priority

    def sort_tasks(self):
        """Sorts our tasks by completed date, due date, and priority"""
        sorted_tab = sorted(self.tasks, key = lambda x: (x.completed_date, x.due_date, -x.priority), reverse=True)
        self.tasks = sorted_tab
        
        #Everytime we sort our list, we need to re-update the IDs if anything has shifted or been removed
        for i in range(len(self.tasks)):
            self.tasks[i].id = i + 1


    #Deletes any task objects with the matching ID - aka the index in our task list
    def delete(self, id_num):
        """Delete a task from our task object list"""
        del self.tasks[id_num-1]

        #We reassign our IDs since the table has shifted
        for i in range(len(self.tasks)):
            self.tasks[i].id = i + 1

            