from operating_system.process_state import PROCESS_STATE
from utilities.printer import Printer

class Process:
    
    def __init__(self, process_id, memory_start, memory_end, ir) :
        self._pid = process_id
        self._state = PROCESS_STATE.CREATE()
        self._memory_start = memory_start
        self._memory_end = memory_end
        self._pc = memory_start
        self._ir = ir
     
       
    
    
    def get_process_state(self):
        return self._state
    
    def set_state(self, new_state):
        self._state = new_state
    
    def get_memory_star(self):
        return self._memory_start
 
    def get_memory_end(self):
        return self._memory_end
    
    def get_pc(self):
        return self._pc
    
    def refresh_pc (self, new_pc):
        self._pc = new_pc
        
    def get_ir(self):
        return self._ir
    
    def refresh_ir (self, new_ir):
        self._pc = new_ir
    
    def get_pid(self):
        return self._pid
    
    def __repr__(self):
        return Printer.tabulated([
            ["PID", self._pid],
            ["Process Status", self._state],
            ["",""], # To show an empty line
            ["Memory Start", self._memory_start],
            ["Memory End", self._memory_end],
            ["", ""], # To show an empty line
            ["PC", self._pc],
            ["IR", self._ir]
        ])
    