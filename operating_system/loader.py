from hardware.hardware import HARDWARE

from operating_system.allocation.bf_allocation import BestfitAllocationAlgorithm
from operating_system.allocation.ff_allocation import FirstFitAllocationAlgorithm
from operating_system.allocation.wf_allocation import WorstFitAllocationAlgorithm

class Loader:
    """
    The loader is in charge of loading programs into memory.
    Later, the loader may use different, more complex
    allocation strategies. For now, we use a super simple strategy.
    The problem with this strategy is that, even if a program is
    unloaded, the freed memory cannot be used back, yikes.
    """

    def __init__(self, kernel, allocation_algorithm):
        self.__kernel = kernel
        self.__available_continuous_allocation_algorithms = {
            'FF' : FirstFitAllocationAlgorithm()
           #'BF' : BestFitAllocationAlgorithm(),
            #'WF' : WorstFitAllocationAlgorithm()
        }
        self.__current_allocation_algorithm_name = allocation_algorithm
        self.__current_allocation_algorithm = self.__available_continuous_allocation_algorithms[allocation_algorithm]
    @property
    def current_allocation_algorithm_name(self):
        return self.__current_allocation_algorithm_name
    
    @property
    def current_allocation_algorithm(self):
        return self.__available_continuous_allocation_algorithms
    
    def load(self, data):
        """
        Load a given program data into memory. Return the location
        where the first instruction was allocated.
        Fails if there is not enough free contiguous memory.
        """
        if not self.has_free_memory(len(data)):
            raise RuntimeError("Not enough free memory.")
        #print(self.has_free_memory(len(data)))
        return self.__current_allocation_algorithm.load(data)
        

    def unload(self, pcb):
        """
        Remove a program that is loaded into memory from the memory.
        The PCB is received and used to know where the program is
        stored in memory.
        """
        self.__current_allocation_algorithm.unload(pcb)
        

    def has_free_memory(self, size):
        """ Answer if there is enough free contiguous memory to store some data. """
        return self.__current_allocation_algorithm.has_free_memory(size)

    def __free_memory(self):
        """ Returns the amount of free contiguous memory. """
        
        return self.__current_allocation_algorithm.free_memory()