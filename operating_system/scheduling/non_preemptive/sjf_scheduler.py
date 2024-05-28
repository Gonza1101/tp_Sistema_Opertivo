from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.non_preemptive.non_preemptive_scheduler import NonPreemptiveSchedulerAlgorithm

class SJFSchedulingAlgorithm(NonPreemptiveSchedulerAlgorithm):
    """ Implementation of Shortest Job First Scheduling Algorithm. """

    # TODO (2) Complete the class
    
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        self.__ready_process_queue = PriorityQueue()
        
    @property
    def next_process_id(self):
        return self.__ready_process_queue.front
    
    def move_to_ready(self, pid, pcb):
        priority = pcb.burst_time * -1
        self.__ready_process_queue.enqueue(pid,priority)
    
    def move_to_running(self, pid, pcb):
        self.__ready_process_queue.dequeue()
    
    def move_to_waiting(self, pid, pcb):
        pass