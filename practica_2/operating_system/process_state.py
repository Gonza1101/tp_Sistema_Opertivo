STATE_CREATED = "CREATED"
STATE_READY = "READY"
STATE_BLOCKED = "BLOCKED"
STATE_FINISHED = "FINISHED"
STATE_EXECUTING = "EXECUTING"


class PROCESS_STATE :
    
    
    @classmethod
    def CREATE(self):
        return STATE_CREATED

    @classmethod
    def READY(self):
        return STATE_READY

    @classmethod
    def BLOCKED(self):
        return STATE_BLOCKED

    @classmethod
    def EXECUTING(self):
        return STATE_EXECUTING

    @classmethod
    def FINISHED(self):
        return STATE_FINISHED