from utilities.priority_queue import PriorityQueue

from hardware.hardware import HARDWARE
from hardware.irq import IRQ

from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm
from utilities.queue import Queue

class FPPSSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Fixed Priority Preemtive Scheduling Algorithm. """

    # TODO (4) Complete the class
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        self.__priority_process_queue = PriorityQueue()
        
    @property
    def next_process_id(self):
        currently_process_pid = self.kernel.scheduler.currently_running_pid
        
        if currently_process_pid == None :
            return self.__priority_process_queue.front
    
        if currently_process_pid != None :
            return None
        
        return self.__priority_process_queue.frontt
    
    def move_to_ready(self,pid, pcb):
        
        priority_new = pcb.priority
        self.__priority_process_queue.enqueue(pid,priority_new)
        
        currently_process_pid = self.kernel.scheduler.currently_running_pid
        
        if currently_process_pid != None and pcb.state == 'READY' :
            currently_running_pcb = self.__kernel.process_table.get_pcb_by_pid(pid_new) 
            if priority_new > currently_running_pcb.priority :
                HARDWARE.interrupt_vector.handle(IRQ.SWAP())
    
    def move_to_running(self, pid, pcb):
        self.__priority_process_queue.dequeue()
    
    def move_to_waiting(self, pid, pcb):
        pass