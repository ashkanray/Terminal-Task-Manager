#!/usr/bin/env python

import argparse

def parser_func():

    #Initializes our parser
    parsed_arg = argparse.ArgumentParser(description='Process command line arguments')

    #Saves the parser arguments that are allowed
    #--add, --query, --priority, --due, --delete, --list, --report, --done

    parsed_arg.add_argument('--add', dest = "add_t", type=str, help="Add tasks to list manager - Use proper task names when inputting tasks")
    parsed_arg.add_argument('--query', dest = "query_t", type=str, nargs="+", help="Searchs for tasks based on one or more keywords")
    parsed_arg.add_argument('--priority', dest = "prio_t", type=int, help="Sets priority of added tasks from 1 (Highest) to 3 (Lowest) - The default priority is 3", default = 3)
    parsed_arg.add_argument('--due', type=str, dest = "date_t", help="Sets task due date. Dates can include both names of days or complete dates", default = "-")
    parsed_arg.add_argument('--delete', dest = "del_t", type=int, help="Deletes task on task list by ID number")
    parsed_arg.add_argument('--list', dest = "list_t", action='store_true', help="Lists task sorted in order of age")
    parsed_arg.add_argument('--report', dest = "report_t", action='store_true', help="Outputs a full report of inputted tasks sorted by date, age, and priority")
    parsed_arg.add_argument('--done', dest = "done_t", type=int, required=False, help="Completes a task (i.e. sets task to 'Done' and tracks completion date")

    #we return the parsed arguments list to be called in our main function
    return parsed_arg.parse_args()
