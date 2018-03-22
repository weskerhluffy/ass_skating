'''
Created on 22/03/2018

@author: 

XXX:
'''

import logging
from queue import Queue

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

class Node():
    def __init__(self, k, x, y):
        self.k = k
        self.x = x
        self.y = y
        self.v = []

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        
        nodos_x = {}
        nodos_y = {}    
        
        nodos = []
        
        n = int(input())
        
        for i in range(n):
            x, y = [int(a) for a in input().split(" ")]
            nn = Node(i, x, y)
            nodos_x.setdefault(x, []).append(nn)
            nodos_y.setdefault(y, []).append(nn)
            nodos.append(nn)
        
        for cn in nodos:
            cn.v.extend(nodos_x[cn.x] + nodos_y[cn.y])
        
        s = set()
        
        c = 0
        for cn in nodos:
            if (cn.k not in s):
                c += 1
                q = Queue()
                q.put(cn)
                s.add(cn.k)
                while(not q.empty()):
                    cn_bfs = q.get()
                    for v in cn_bfs.v:
                        if(v.k not in s):
                            q.put(v)
                            s.add(v.k)
        print("{}".format(c - 1))
                
        

        
