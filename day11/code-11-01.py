import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )
    

class StoneSolver :

  DEFAULT_FILE = "day11\\input.txt"
  #DEFAULT_FILE = "day11\\sample.txt"
  DAY = 11
  verbosePrint = True

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.line = []


##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=StoneSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    #self.readInput( args.input )

    with open( args.input, 'r') as foo :
      self.line = foo.readlines()
      self.line= [ l.strip() for l in self.line ]
      self.line = self.line[0].split(" ")

  ##########
  def blink( self ) :
    newLine = []
    for stone in self.line :
      if stone == "0" :
        newLine.append( "1" )
      elif len(stone) % 2 == 0 :
        foo = len(stone)//2
        newLine.append( stone[0:foo] )

        bar = re.sub( "^0+(\\d)", "\\1", stone[foo:] )
        newLine.append( bar )
      else:
        num = int(stone) * 2024
        newLine.append( str( num ) )
    self.line = newLine

  ##############

  def main(self) :

    self.processArguments()
    for i in range( 0, 75 ) :
      self.blink( )
      print( "blink %d - %d stones" % ( i, len( self.line) ) )

if __name__ == "__main__":
  p = StoneSolver() 
  p.main()