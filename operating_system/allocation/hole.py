class Hole():
    def __init__(self,memory_address, hole_size) -> None:
        self.__memory_adress = memory_address
        self.__hole_size = hole_size
    
    @property
    def memory_address(self):
        return self.__memory_adress
    
    @property
    def size (self):
        return self.__hole_size
    
    def __str__(self) -> str:
        
        return f"(addr: {self.__memory_adress}, size: { self.size})"