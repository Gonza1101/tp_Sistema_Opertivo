from hardware.hardware import HARDWARE
from utilities.printer import Printer

from operating_system.process import Process
from operating_system.scheduler.long_term.long_term_scheduler import Long_term_scheduler

class Kernel:
    #Constructor
    def __init__(self) :
        self._pct = PCT()
        self._long_term_scheduler = Long_term_scheduler(HARDWARE.memory.size)
        self._jobs_queue =[]
        self._pid = 1

        self._memory_start = 0
        self._memory_end = 0
        
        self._pc = HARDWARE.cpu.pc
    
    def add_to_pct(self, pcb) :
        self._pct.add_pcb(pcb)
        
    def pid_increase(self):
        self._pid += 1


    #Crea nuevo proceso y guarda PSB en PST y manda a cargarlo
    def create_process(self, program) :
        pcb = self._long_term_scheduler.create_process(program, self._memory_end, self._pid)
        
        self.add_to_pct(pcb)
        self.pid_increase()
        self.load_program(program) 
        
    #eliminar proceso de memoria y PCT
    def kill_process(self, pid):
        process_to_kill = self._pct.get_pcb(int(pid))
        self._pct.remove_pcb(pid)
        
        for i in range(process_to_kill.get_memory_star(), process_to_kill.get_memory_end() + 1):
            HARDWARE.memory.write(i, "")
        
 
    def load_program(self, program):
        program_size = len(program.instructions)
        
        self._memory_start = self._memory_end
        
        j = 0
        for i in range(self._memory_start, (self._memory_start + program_size)):
            HARDWARE.memory.write(i, program.instructions[j])
            j += 1 

        self._memory_end = (self._memory_start + program_size)

    
    
    @property
    def pid(self):
        return self._pid
    
    @property
    def pct(self):
        return self._pct

#agregar propety jobs_table

    
     ################### Class PCT ##############
     
class PCT:
    def __init__(self):
        self._pcb_table = {}
            
    def add_pcb(self, pcb):
        self._pcb_table[pcb.get_pid()] = pcb
    
    def get_pcb(self, process_id):
        return self._pcb_table.get(process_id)
    
    def remove_pcb(self, process_id):
        del self._pcb_table[process_id]

    @property   
    def pcb_table(self):
        return self._pcb_table
        
    def __repr__(self):
        values = list(self._pcb_table.values())
        return Printer.tabulated([
            ["PCB",values]
        ])

"""
EL Kernel o "OS" tiene
Tabla de Procesos { int : PCB }

System calls : 
createProcess(Program)
            ||
scheduler / Planificador
    *Largo Plazo (Crea Prossesos) / Planificador de Entrada
    *Corto Plazo(Asigna a la CPU)
    *Mediano Plazo ...
    
Cola de Processos (Process Listos)
"""