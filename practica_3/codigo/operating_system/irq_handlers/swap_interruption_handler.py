from hardware.hardware import HARDWARE
from hardware.irq import IRQ

from operating_system.irq_handlers.abstract_interruption_handler import AbstractInterruptionHandler

class SwapInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        """
        Remove the currently running process and swap it for
        the next process in the ready state.
        """
        # TODO: (5)
        # We are handling preemption here. So we need to swap the
        # currently executing in the CPU, by the one next in the queue.
        # First, lets get the process running
        current_pid = self._kernel.scheduler.currently_running_pid
        # Now, let's move this process to ready state, as it can actually
        # still run, it's the OS who is telling it not to continue.
        self._kernel.scheduler.move_to_ready(current_pid)
        # Once in ready, we have to load the next process in the ready queue.
        # Not that, if there is only one process, it will be the same
        # process that we load.
        next_process = self._kernel.scheduler.next_process()
        self._kernel.scheduler.move_to_running(next_process.pid())