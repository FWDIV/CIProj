from ciproject import task_manager
import random
"""_summary_
handlers interact with our task manager and utility modules to officiate tasks for the cli
"""
def add_task_handler(id : str | None, desc : str, priority = int | None) -> int:
    """_summary_

    Args:
        id (str | int | None): Can pass an integer id or a string name to map to a generated id
        desc (str): _description_

    Returns:
        int: _description_
    """
    id = random.randint(1,100000) if id is None else id #note we want to change this when we write our json

    tm = task_manager.TaskManager()
    try:
        int_id = int(id)
        tm.add_task(desc,int_id,priority)
    except ValueError:
        int_id = hash(id)
        tm.add_task(int_id,desc,priority)
    
    return int(int_id)

    
        
def delete_task_handler(id : str) -> int:
    pass
def update_task_handler(id : str | None, desc : str) -> int:
    pass
def list_task_handler()-> None:
    pass