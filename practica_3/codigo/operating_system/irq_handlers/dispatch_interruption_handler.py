from hardware.hardware import HARDWARE
from hardware.irq import IRQ
from operating_system.irq_handlers.abstract_interruption_handler import AbstractInterruptionHandler

class DispatchInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        """
        Dispatch the next process to the running state.
        """
        preemptive = irq.arguments[0]
        pid = self.kernel.scheduler.currently_running_pid
        # TODO: (6)
        # As we have The next process in the ready state should be moved
        # to the running state.
        
        next_process = self._kernel.scheduler.next_process
        
        if next_process is None :
            HARDWARE.cpu.pc=-1
        elif preemptive is False and pid is None:
           self._kernel.scheduler.move_to_running(next_process)
        else :
            HARDWARE.interrupt_vector.handle(IRQ.SWAP())