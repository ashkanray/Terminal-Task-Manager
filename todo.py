#!/usr/bin/env python

import sys
from tasks_class import Tasks
from task_class import Task
from dateutil import parser
from parser_arg import parser_func
import os.path


def todo():

    #We call our argparse function
    #We initialize our Tasks class
    try:
        args = parser_func()
        tasks_tracker = Tasks()

    #Any invalid arguments after calling our argparse function will call an IndexError
    except IndexError:
        print("Invalid arguments!")
        sys.exit(1)

    #Once we initialize our classes and our inputs, we unpickle our files IF they exist
    if os.path.exists('.todo.pickle'):
        tasks_tracker.unpickle_tasks()
    

    """--add Command"""
    #We check if the "--add" command was passed through 
    if args.add_t:

        task_add = args.add_t
        task_add.strip()

        if task_add.isdigit() or len(task_add) == 0:
            print("Please add a valid task name -Use -h for more help")
        
        else:
            item = Task(args.add_t)
            item.unique_id(len(tasks_tracker.tasks)+1)


            """--due Command"""

            #We check if the input due date was not given - the default value is "-"
            if args.date_t == "-":

                #We pass through the default value to the Task Object
                item.due_date_input(args.date_t)

            else:
                #If the due date is given, we need to save and convert it to a readable format
                due_date_in = args.date_t

                #Using parser, we can take the input date and convert it to the proper format
                #MM-DD-YY
                due = parser.parse(due_date_in)
                due = due.strftime("%m-%d-%Y")

                #We save the due date to our Task Object
                item.due_date_input(due)
                    

            """--priority Command"""
            if args.prio_t:
                
                #Saves the input - the default priority is 1
                priority_in = args.prio_t

                #We save the priority to our Task Object if its matches the requirements
                if priority_in in [1, 2, 3]:
                    item.priority_input(priority_in)
            
                else:
                    print("Please limit priority to 1, 2, or 3")
            

            #We call the actual Task Class function - add()
            tasks_tracker.add(item)
        

        """--delete Command"""
    elif args.del_t:

        #We do a quick check to see if the ID of the task we want to delete actually exists in the task list
        if args.del_t > len(tasks_tracker.tasks):
            print("Please enter a valid ID")

        else: 

            #We pass the ID number of the task that we want to delete into our Task Class funcction - delete()
            tasks_tracker.delete(args.del_t)


        """--done Command"""
    elif args.done_t:

        #We pass the ID number of the task that we want to complete into our Task Class funcction - done()
        #This saves a completed date variable
        tasks_tracker.done(args.done_t)


        """--list Command"""
    elif args.list_t:

        #We check if there are any items on the actual task list - if no tasks have been added, we return the print statement
        if len(tasks_tracker.tasks) == 0:
            print("No tasks exist - please use --add to add any tasks to your list manager")

        else:
            #We call our Tasks Class function - list()
            tasks_tracker.list()


        """--report Command"""
    elif args.report_t:

        #We check if there are any items on the actual task list - if no tasks have been added, we return the print statement
        if len(tasks_tracker.tasks) == 0:
            print("No tasks exist. Please use --add to add any tasks to your list manager, or -h to learn more about functionality")

        else:
            #We call our Tasks Class function - report()
            tasks_tracker.report()


        """--query Command"""
    elif args.query_t:

        #We push our keywords as a list into the Tasks Class function - query()
        tasks_tracker.query(args.query_t)

    
    #We sort our tasks by the following requirements
    #1) Completion Date - Decreasing
    #2) Due Date - Decreasing
    #3) Priority - from 1 to 3
    tasks_tracker.sort_tasks()    

    #We pickle our tasks list to be loaded in next time the command is called 
    tasks_tracker.pickle_tasks()
    
    #exit the function
    sys.exit(0)


if __name__ == "__main__":
    todo()