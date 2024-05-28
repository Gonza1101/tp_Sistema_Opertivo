from utilities.queue import Queue

from hardware.irq import IRQ

from operating_system.pcb import *
from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class RRSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Round Robin Scheduling Algorithm. """

    # TODO (5) Complete the class
    
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        if quantum > 0 :
            HARDWARE.clock.add_subscriber(self)
        self.__ready_processes_queue = Queue()
        self.__already_executed_processes_queue = Queue()
        
    
    @property
    def next_process_id(self):
        if self.__ready_processes_queue.is_empty :
            self.swap_queues()
        return self.__ready_processes_queue.front
       
    
    def move_to_ready(self, pid, pcb):
        if pcb.state is NEW and pcb.pc == pcb.memory_start:
            self.__ready_processes_queue.enqueue(pid)
        else:
            self.__already_executed_processes_queue.enqueue(pid)

    
    def move_to_running(self, pid, pcb):
        if self.__ready_processes_queue.is_empty :
            self.swap_queues()
            self.__ready_processes_queue.dequeue()
        
     
            
    def move_to_waiting(self, pid, pcb):
        pass
    
    def tick(self,tick_number):
        if self.kernel.scheduler.current_algorithm_name == 'RR' :
            if(tick_number > 0 and tick_number % self.quantum == 0):
                HARDWARE.interrupt_vector.handle(IRQ.SWAP())

    
    def swap_queues(self):
        for i in range (0, len(self.__already_executed_processes_queue)):
            pid = self.__already_executed_processes_queue.dequeue()
            self.__ready_processes_queue.enqueue(pid)
    
    