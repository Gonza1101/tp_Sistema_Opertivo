from operating_system.allocation.abstract_allocation import AbstractAllocationAlgorithm

from hardware.hardware import HARDWARE

from operating_system.allocation.hole import Hole
from utilities.priority_queue import PriorityQueue
from utilities.queue import Queue

class BestfitAllocationAlgorithm(AbstractAllocationAlgorithm):
    
    def __init__(self) -> None:
        super().__init__()
        self.__avaible_holes = PriorityQueue()
        self.__avaible_holes.enqueue(Hole(0, HARDWARE.memory.size),-HARDWARE.memory.size)
    
    @property
    def avaible_hole(self):
        return self.__avaible_holes
    
    def load(self, data):
        hole = self.first_adecueate_hole(len(data))
        
        if hole != None:
            for i in range(0, len(data)):
                    HARDWARE.memory.write(hole.memory_address + i, data[i])
            new_hole = Hole(hole.memory_address + len(data),  hole.size + len(data))
            if new_hole.size < 0 :
                self.add_hole(new_hole)
        
    
    def unload(self, pcb):
        for i in range(pcb.memory_base,  pcb.memory_base + pcb.memory_limit ):
                HARDWARE.memory.write(i, '')
        new_hole =Hole(pcb.memory_base, -pcb.memory_limit)
        
        self.add_hole(new_hole)
    
    def __has_free_memory(self, data_size):
        aux_queue = Queue()
        for i in range(0, len(self.__avaible_holes)):
            if self.__avaible_holes.front().size >= data_size:
                return True
            aux_queue.enqueue(self.__avaible_holes.front())
            self.__avaible_holes.dequeue()
        
        if not aux_queue.is_empty:
            self.swap_queue(aux_queue, self.__avaible_holes)    
        return False
    
    def __free_memory(self):
        """
        TODO : Queda FREE_MEMORY
        """
        return super().__free_memory()
    
        
    def first_adecueate_hole(self, size):
        """
        Return the first adecuate hole if exists compared with a given size.
        Return none if an adecuate hole doesn't exist.
        """
        aux_queue = Queue()
        for i in range(0, len(self.__avaible_holes)):
            if size <= self.__avaible_holes.front().size:
                return self.__avaible_holes.dequeue()
            aux_queue.enqueue(self.__avaible_holes.dequeue())
        
        if not aux_queue.is_empty:
            self.swap_queue(aux_queue, self.__avaible_holes)
    
    
    def add_hole(self, hole):
        self.__avaible_holes.enqueue(hole, -hole.size)
        
    def swap_queue(self, aux_queue, priorityQueue):
        for i in range(0, len(aux_queue)):
            priorityQueue.enqueue(aux_queue.front(), -aux_queue.front().size)
            aux_queue.dequeue()
        