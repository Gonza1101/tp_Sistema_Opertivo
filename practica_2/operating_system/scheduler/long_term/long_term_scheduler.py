from operating_system.process import Process
from utilities.printer import Printer


class Long_term_scheduler :
    def __init__(self, memory_size):
        self._memory_size = memory_size
                
#Crea nuevo proceso y guarda PSB en PST y manda a cargarlo
    def create_process(self, program, memory_end, pid):
        program_size = len(program.instructions)  
        memory_start = memory_end
        memory_end = (memory_start + program_size) - 1  
        try:
            if (self._memory_size - memory_start) >= program_size :
                pcb = Process(pid, memory_start, memory_end, 0)
                return pcb
        except:
            Printer.error("Unable to create a process")

#cambio de State
    def change_state(self, process, state):
        process.set_process_state(state)