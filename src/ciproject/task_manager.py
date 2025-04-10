from enum import Enum
"""_summary_
    This is where we store the function logic for our simple application


    Add, Update, and Delete tasks
    Mark a task as in progress or done
    List all tasks
    List all tasks that are done
    List all tasks that are not done
    List all tasks that are in progress
"""


class Priority(Enum):
    High = 2
    Moderate = 1
    Low = 0

class Completeness(Enum):
    """_summary_
    """
    Complete = 2
    Incomplete = 1
    InProgress = 0


class Task:
    """_summary_
    Tasks are a mutable objects that hold state relating to an individual task in our task manager. They are able to be stored or read in a json file. 
    All tasks are "complete", "incomplete" or "in_progress". Tasks can be updates, and those updates will be reflected int he stored json.
    """
    def __init__(self,id,desc,priority,):
        pass
    def mark_complete(self):
        """_summary_

        """
        pass
    def update(self, priority: Priority | None, completeness : Completeness | None ):
        pass
    def mark_incomplete(self):
        pass
    def mark_in_progress(self):
        pass


class TaskManager:
    """_summary_
        Our task manager class defines an object which will hold our tasks

    """
    def __init__(self):
        pass
    
    def add_task(self, description: str, id: int | None, priority: Priority | None) -> str:
        """_summary_
            Adds a task to our task manager object's task list.
        Args:
            description (str): A string which describes the task being supplied
            id (str): OPTIONAL, an id for direct lookup of a task, if not supplied, a random value will be generated.
            priority (_type_): OPTIONAL  priority value (High,Moderate,Low) to filter for high, moderate or low priority tasks. If not supplied, the priority defaults to "Low"

        Returns:
            str: returns the id of the newly added task
        """
        pass
    def update_task(self,):
        pass
    def delete_task(self, id: int)-> bool:
        """_summary_
        Removes a task object from the task manager's task list, if the task exists 
        and is successfully deleted returns True, else False
        Args:   
            id (int): id of the task being deleted. 

        Returns:
            bool: returns true if the id was present in the tasklist and successfully removed.
        """
        pass
    def list_tasks(self) -> str:
        """_summary_
        Returns a string describing all of the tasks in the TaskManager's tasklist

        Returns:
            str: A string which is explicitly comprised of the descriptions from all the tasks in 
                the TaskManager's task list, separated by new lines.
        """
        pass
    def list_complete_tasks(self):
        """_summary_
        Returns a string describing all of the COMPLETE tasks in the TaskManager's tasklist

        Returns:
            str: A string which is explicitly comprised of the descriptions from all the COMPLETE tasks in 
                the TaskManager's task list, separated by new lines.
        """
        pass
    def list_incomplete_tasks(self):
        """_summary_
        Returns a string describing all of the INCOMPLETE tasks in the TaskManager's tasklist

        Returns:
            str: A string which is explicitly comprised of the descriptions from all the INCOMPLETE tasks in 
                the TaskManager's task list, separated by new lines.
        """
        pass
    def list_progress_tasks(self):
        """_summary_
        Returns a string describing all of the IN_PROGRESS tasks in the TaskManager's tasklist

        Returns:
            str: A string which is explicitly comprised of the descriptions from all the IN_PROGRESS tasks in 
                the TaskManager's task list, separated by new lines.
        """
        pass
