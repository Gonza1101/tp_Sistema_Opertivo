from hardware.hardware import HARDWARE

from operating_system.allocation.hole import Hole
class AbstractAllocationAlgorithm:
    
    def __init__(self) -> None:
         self.__avaible_hole =[Hole(0,HARDWARE.memory.size)]
         self.__free_memory = HARDWARE.memory.size
         
    @property
    def avaible_hole(self):
         return self.__avaible_hole  
       
    @property
    def free_memory(self):
        return self.__free_memory
  
    def load(self, data):
        """
        Load the given data into memory.
        """
        #memori_location => devuelve la primera celda donde se cargo el programa
        #Tuple (memory_location, index)
        adecuate_hole = self.first_adecueate_hole(len(data))
        #memoy_Location => tuple (memory_address, number of empty cells)
        hole = adecuate_hole[0]
        #Index of the hole in avaible hole
        index = adecuate_hole[1]
        if hole != None:  #diferente a None
            for i in range(0, len(data)):
                HARDWARE.memory.write(hole.memory_address + i, data[i])
            self.__avaible_hole.pop(index)
            new_hole= Hole( hole.memory_address + len(data), hole.size - len(data) )
            self.__free_memory -= len(data)
            
            if new_hole.size > 0 :
                self.add_hole(index,new_hole)
            #print([str(hole) for hole in self.__avaible_hole])
        return hole.memory_address
    
    def unload(self, pcb):
        """
        Unload the given pcb data from memory.
        """
        for i in range(pcb.memory_base,  pcb.memory_base + pcb.memory_limit ):
                HARDWARE.memory.write(i, '')
        new_hole =Hole(pcb.memory_base, pcb.memory_limit)
        index = self.index_for_hole(new_hole)
        self.add_hole( index , new_hole )
        self.__free_memory += pcb.memory_limit
    
    def has_free_memory(self,data_size):
        """
        Return if exists avaible free memory amount for the given data size
        """
        accumulator = False
        
        for hole in self.__avaible_hole:
            if data_size <= hole.size : accumulator = accumulator or True
            else : accumulator = accumulator or False
            
        return accumulator 
    
    def add_hole(self,index, hole):
        """
        Add the given holes to the avaible holes attrib.
        """
        self.__avaible_hole.insert(index,hole)
    
    def index_for_hole(self, hole):
        """
        Return an index to place the given hole in the available holes attribute.
        """
        for i in range(0, len(self.__avaible_hole)):
            if hole.memory_address < self.__avaible_hole[i].memory_address:
                return i
    
    #TODO I believe miracle
            
    def merge_hole(self, hole_first, hole_Next ):
        """
        Return a hole with the lowest memory address and the sum of the
        size of the two given holes.
        """
        
        address = hole_Next.memory_address
        if(hole_first.memory_address < hole_Next.memory_address):
            address = hole_first.memory_address
        return Hole(address,(hole_first.size + hole_Next.size))
    
    def first_adecueate_hole(self,size):
        raise RuntimeError("Should be implemented by the subclass, but it did not implement it")
    