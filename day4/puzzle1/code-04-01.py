import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

class WordSearchSolver :

  DEFAULT_FILE = "day4\\puzzle1\\input.txt"
  DAY = 4
  verbosePrint = True

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.wordPuzzle = []
    self.words = ["XMAS"]
    self.i = 0
    self.j = 0
    

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=WordSearchSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    #self.readInput( args.input )
    with open( args.input, 'r') as foo :
      self.wordPuzzle = foo.readlines()

################

  def wordSearch( self ) :
    sum = 0
    self.i = 0
    self.j = 0
    for self.i in range (0, len( self.wordPuzzle ) ) :
      for self.j in range( 0, len( self.wordPuzzle[ self.i ] ) ) :
        # find out if any words we're looking for 
        words = [ w  for w in self.words if ( w[0] == self.wordPuzzle[ self.i ][ self.j ] ) ]
        if len( words ) > 0 :
          sum += self.spotSearch( -1, -1, words )
          sum += self.spotSearch( -1, 0, words )
          sum += self.spotSearch( -1, 1, words )
          sum += self.spotSearch( 0, -1, words )
          sum += self.spotSearch( 0, 1, words )
          sum += self.spotSearch( 1, -1, words )
          sum += self.spotSearch( 1, 0, words )
          sum += self.spotSearch( 1, 1, words )
    print( sum )

  ##############

  def spotSearch( self, dx, dy, words ) :
    index = 1
    foundWords = []
    allWords = words.copy()
    while len( words ) > 0 :
      if ( self.i + ( dy * index) ) in range( 0, len( self.wordPuzzle ) ) and (self.j + (dx * index ) ) in range( 0, len( self.wordPuzzle[self.i + ( dy * index) ] ) ) :
        words = [ w for w in words if w[index] == ( self.wordPuzzle[self.i + ( dy * index)][self.j + (dx * index )] ) ]
        if len( words ) == 1 and len( words[0] ) == index + 1 :
          return 1
      else :
        break
      index += 1
    return 0

  ##############

  def main(self) :

    self.processArguments()
    self.wordSearch()

if __name__ == "__main__":
  p = WordSearchSolver() 
  p.main()
