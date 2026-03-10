from enum import Enum
from typing import Dict
import time
class Phase(Enum): SPROUT="sprout"; GREEN="green_leaf"; YELLOW="yellow_leaf"; RED="red_leaf"; SOIL="soil"
class CapsuleLifecycle:
    def __init__(self): self.c: Dict={}
    def add(self,i,c,p="P2"): self.c[i]={'c':c,'p':p,'conf':0.7,'phase':Phase.SPROUT,'t':time.time()}
    def access(self,i):
        if i not in self.c: return False
        self.c[i]['conf']=min(1.0,self.c[i]['conf']+0.03)
        self.c[i]['phase']=Phase.GREEN if self.c[i]['conf']>=0.8 else Phase.SPROUT
        return True
