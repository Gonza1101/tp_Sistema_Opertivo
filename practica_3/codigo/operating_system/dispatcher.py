from hardware.hardware import HARDWARE

from operating_system.pcb import RUNNING, READY, WAITING

class Dispatcher:
    """
    The dispatcher is in charge of loading and saving the state
    of the CPU into a particular PCB.
    """
    def __init__(self, kernel):
        self.__kernel = kernel

    def load(self, pcb):
        """
        Load the state of a PCB into the CPU.
        Next tick will start executing the program of the loaded process.
        """
        # TODO: (2)
        # We need to load the state of the given PCB to the CPU.
        # This implies copying the information stored in the PCB
        # to the corresponding registries in the CPU, so next tick will
        # run the process the PCB represents.
        pcb_pc = pcb.pc
        
        HARDWARE.cpu.pc = pcb_pc
        
    

    def save(self, pcb):
        """
        Save the current state of the CPU to the given PCB.
        The CPU remains IDLE into the next load.
        """
        # TODO: (2)
        # We need to save the current state of the CPU to the given PCB.

        # This occurrs on a context switch, so after this step, the CPU
        # should be put as IDLE, not running anything.
        
        pcb.pc = HARDWARE.cpu.pc
        
           

