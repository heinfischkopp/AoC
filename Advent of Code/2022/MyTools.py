import time
import os

class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name,)
        print('Zeit: %s' % (time.time() - self.tstart))

class AoC:
    def __init__(self, day=0,TestDaten = False):
        self.day = day
        if TestDaten:
            self.puzzlefile = os.path.dirname(__file__) + '\\day' + str(self.day) + '.txt'
        else:
            self.puzzlefile = os.path.dirname(__file__) + '\\day' + str(self.day) + 'testdata.txt'
        self.tstart = time.time()
        self.puzzle = 'A'

    def solution(self,Solution="NA"):
        print('\n\tLösung ' + self.puzzle + ': ' + str(Solution))
        print('\tZeit: %s ' % (time.time() - self.tstart)) 
        self.nextPuzzle()

    def nextPuzzle(self):
        self.puzzle = chr(ord(self.puzzle)+1)

    def toc(self,comment=''):
        print('TOC: %s %s' % (time.time() - self.tstart,comment)) 

    def readLines(self):
        with open(self.puzzlefile, 'r') as f:
            return f.read().splitlines()