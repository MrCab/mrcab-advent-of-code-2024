import re
import argparse
from fractions import Fraction

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )
    

class SysProg2Solver :

  DEFAULT_FILE = "day9\\input.txt"
  #DEFAULT_FILE = "day9\\sample.txt"
  DAY = 9
  verbosePrint = True
  BLANK = "."

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.lines = []
    self.theLine = ""
    self.curFile = 0
    self.endFile = 0
    self.endFileSize = 0    


##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=SysProg2Solver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    #self.readInput( args.input )

    with open( args.input, 'r') as foo :
      #self.lines = foo.readlines()
      l = foo.readlines()
      self.theLine = l[0].strip()
    self.endFile = ( len( self.theLine ) // 2 ) + 1

  ##########
  def defrag1( self ) :
    defrag = []
    diskSize = len( self.theLine )
    endFile = ( diskSize -1 ) // 2

    # if we do for i in range, and the top number changes,
    # the range is not re-evaluated
    i = 0
    while i < self.endFile * 2 :
      if i % 2 == 0 :
        self.curFile = i // 2
        foo = int( self.theLine[i] )
        for kb in range( 0, foo ) :
          defrag.append( i // 2 )
      else :
        bar = int( self.theLine[i] )
        for mb in range( 0, bar ) :
          if self.endFileSize == 0  :
            self.setNextEndFile()
          defrag.append( self.endFile )
          self.endFileSize -= 1
      i += 1

    if i == self.endFile * 2:
      while self.endFileSize > 0 :
        defrag.append( self.endFile )
        self.endFileSize -= 1

    self.checksum1( defrag )     
    
  #######

  def setNextEndFile( self ) :
    while( self.endFileSize == 0 ) :
      self.endFile -= 1
      self.endFileSize = int( self.theLine[ self.endFile * 2 ] )
    if self.endFile <= self.curFile :
      self.endFile = 0

  #####
  def checksum1( self, defragged ) :
    sum = 0
    for i in range( 0, len( defragged ) ) :
      sum += ( i * defragged[i] )
    print( sum )

  ##############

  def main(self) :

    self.processArguments()
    self.defrag1()

if __name__ == "__main__":
  p = SysProg2Solver() 
  p.main()