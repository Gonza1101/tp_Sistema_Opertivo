from operating_system.allocation.abstract_allocation import AbstractAllocationAlgorithm

from hardware.hardware import HARDWARE

from utilities.priority_queue import PriorityQueue
from operating_system.allocation.hole import Hole

class WorstFitAllocationAlgorithm(AbstractAllocationAlgorithm):
    
    def __init__(self) -> None:
        super().__init__()
        self.__avaible_holes = PriorityQueue()
        self.__avaible_holes.enqueue(Hole(0, -HARDWARE.memory.size))
    
    @property
    def avaible_hole(self):
        return self.__avaible_holes
    
    def load(self, data):
        return super().load(data)
    
    def unload(self, pcb):
        for i in range(pcb.memory_base,  pcb.memory_base + pcb.memory_limit ):
                HARDWARE.memory.write(i, '')
        new_hole =Hole(pcb.memory_base, -pcb.memory_limit)
        
        self.add_hole(new_hole)
    
    def __has_free_memory(self, data_size):
        return super().__has_free_memory(data_size)
    
    def __free_memory(self):
        return super().__free_memory()
    
    def add_hole(self, hole):
        self.__avaible_holes.append(hole)