#!/usr/bin/env python

import datetime
import pytz


class Task:
    """Representation of a task
  
    Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    """

    #Initializes our Task Object using the str via the --add command
    def __init__(self, name):
        self.name = name

        #Created date uses datetime.today() to save our current date
        self.created_date = datetime.date.today()

        #Completed date is saved as Null until we complete it later
        self.completed_date = "-"

        #We save a separate created date with proper formatting for our Report
        #We use pytz to save CST timezone
        chicagoTz = pytz.timezone("America/Chicago") 
        now = datetime.datetime.now(chicagoTz)

        self.created_detail = now.strftime("%a %b %d %H:%M:%S %Z %Y")
        

    #If we get a priority input, we save it here
    def priority_input(self, pri):
        self.priority = pri

    #If we get a due date input, we save it here
    def due_date_input(self, due):
        self.due_date = due

    #We use this to assign our ID based on the sorting of the list
    #This function is called whenever we need to add / remove / complete / or re-sort the task objects list
    def unique_id(self, id):
        self.id = id

    #When we call our list / report / query, we need to calculate the age of our tasks
    #This is done by subtracting our current time with our created date
    #We round the age to the nearest day
    def task_age(self):
        self.age = int((datetime.date.today() - self.created_date).days)
