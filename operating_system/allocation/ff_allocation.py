from operating_system.allocation.abstract_allocation import AbstractAllocationAlgorithm

class FirstFitAllocationAlgorithm(AbstractAllocationAlgorithm):
    
    def __init__(self) -> None:
         super().__init__()


    def load(self, data):
        return super().load(data)
    
    def unload(self, pcb):
        super().unload(pcb)
        
    def has_free_memory(self,data_size):
       return super().has_free_memory(data_size)
        
    def add_hole(self,index, hole):
        super().add_hole(index,hole)
    
    def index_for_hole(self, hole):
        return super().index_for_hole(hole)
    
    def first_adecueate_hole(self, size):
        """
        Return the first adecuate hole if exists compared with a given size.
        Return none if an adecuate hole doesn't exist.
        """
        for i in range(0,len(super().avaible_hole)):
            if size <= super().avaible_hole[i].size:
                return (super().avaible_hole[i],i)
            
    def merge_hole(self, hole_first, hole_Next ):
        super().merge_hole(hole_first, hole_Next)