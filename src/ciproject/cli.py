import argparse
from ciproject import handlers


def add_command(parser: argparse._SubParsersAction )-> argparse.ArgumentParser:
    """_summary_
    Creates the subparser for the "add" command in the cli. Our add command accepts a required descrption, and optionally a number id
    Args:
        parser (argparse._SubParsersAction): the parser object we're attaching our subcommand to 
    Returns:
    argparse.ArgumentParser: a parser for the command "add" which adds tasks new to our taskmanager

    parser_add_task = sub_parsers.add_parser("add", help="add a task")

    """

    parser_add_task = parser.add_parser("add", help="add a task")
    parser_add_task.add_argument("desc",type=str,help="Required, a description of a task")
    parser_add_task.add_argument("--name",type=str,help="optional, a name for the task which maps to an id")
    parser_add_task.set_defaults(func=handlers.add_task_handler)
    return parser_add_task

def delete_command(parser: argparse._SubParsersAction ):
    """_summary_
    Creates the subparser for the "delete" command in the cli
    Args:
        parser (argparse._SubParsersAction): the parser object we're attaching our subcommand to 
    Returns:
    argparse.ArgumentParser: a parser for the command "delete" which removes tasks from our taskmanager
    """

    parser_delete_task = parser.add_parser("delete", help="delete a task")
    parser_delete_task.add_argument("id", type=str, help="Required, the name or id of the task you want to delete")
    parser_delete_task.set_defaults(func=handlers.delete_task_handler)

    return parser_delete_task
    
def update_command(parser: argparse._SubParsersAction )-> argparse.ArgumentParser:
    """_summary_
    Creates the subparser for the "update" command in the cli
    Args:
        parser (argparse._SubParsersAction): the parser object we're attaching our subcommand to 
    Returns:
    argparse.ArgumentParser: a parser for the command "update" which updates tasks in taskmanager with new information

    parser_update_task = sub_parsers.add_parser("update", help="update a task")

    """

    parser_update_task = parser.add_parser("update", help="update a task with a new description")
    parser_update_task.add_argument("id", type=str, help="Required, the name or id of the task you want to update")
    parser_update_task.add_argument("desc", type=str, help="Required, the new description of the task you want updated")
    parser_update_task.set_defaults(func=handlers.update_task_handler)

def list_command(parser: argparse._SubParsersAction )-> argparse.ArgumentParser:
    """_summary_
    Creates the subparser for the "list" command in the cli
    Args:
        parser (argparse._SubParsersAction): the parser object we're attaching our subcommand to 
    Returns:
    argparse.ArgumentParser: a parser for the command "list" which lists tasks in our taskmanager

    parser_list_task = sub_parsers.add_parser("list", help="list tasks")

    """

    pass
def mark_command(parser: argparse._SubParsersAction )-> argparse.ArgumentParser:
    """_summary_
    Creates the subparser for the "mark" command in the cli
    Args:
        parser (argparse._SubParsersAction): the parser object we're attaching our subcommand to 
    Returns:
    argparse.ArgumentParser: a parser for the command "mark" which marks tasks in our taskmanager as either in in_progress, todo, or done

    parser_mark_task = sub_parsers.add_parser("mark", help="mark a task")

    """
    pass

def make_parser():
    parser = argparse.ArgumentParser(description = "simple parser")
    sub_parsers = parser.add_subparsers(title="commands", dest="command")

    #We attach subparser commands to our parser in seperate modularized functions
    add_command(sub_parsers)
    delete_command(sub_parsers)
    update_command(sub_parsers)

    sub_parsers.required = True

    return parser