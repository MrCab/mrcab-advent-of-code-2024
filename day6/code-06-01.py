import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class HyruleCastleSolver :

  DEFAULT_FILE = "day6\\input.txt"
  #DEFAULT_FILE = "day6\\sample.txt"
  DAY = 6
  verbosePrint = True

  BLOCKER = "#"
  TRAVERSED = "X"
  BLANK = "."
  START = "^"
  # for coordinates
  X = 1
  Y = 0
  DIRECTIONS = [ [ -1, 0 ], [ 0, 1 ], [1, 0 ], [ 0, -1 ] ]

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0

    self.room = []
    self.x = 0
    self.y = 0
    self.dir = 0
    

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=HyruleCastleSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

    #   ##########
  def readInput( self, fileName ) :
    lines = []
    with open( fileName, 'r') as foo :
      lines = foo.readlines()
      lines = [ l.strip() for l in lines ]
    self.room = [ list(l) for l in lines ]

################

  def findStart( self ) :
    for y in range( 0, len( self.room ) ) :
      if HyruleCastleSolver.START in self.room[y] :
        return ( self.room[y].index( HyruleCastleSolver.START ), y )

  ##############

  def traverse( self ) :
    xLoc = self.x
    yLoc = self.y
    facing = self.dir

    keepGoing = True

    while keepGoing :
      
      self.room[ yLoc ][ xLoc ] = HyruleCastleSolver.TRAVERSED

      if xLoc + HyruleCastleSolver.DIRECTIONS[ facing ][HyruleCastleSolver.X ] not in range( 0, len( self.room[0] ) ) or \
         yLoc + HyruleCastleSolver.DIRECTIONS[ facing ][HyruleCastleSolver.Y ] not in range( 0, len( self.room ) ) :
        keepGoing = False

      else :
        nextSpot = self.room[ yLoc + HyruleCastleSolver.DIRECTIONS[ facing ][HyruleCastleSolver.Y ] ][ xLoc + HyruleCastleSolver.DIRECTIONS[ facing ][HyruleCastleSolver.X ] ]

        if nextSpot == HyruleCastleSolver.BLOCKER :
          facing = ( facing + 1 ) % len( HyruleCastleSolver.DIRECTIONS )
        else :
          xLoc += HyruleCastleSolver.DIRECTIONS[ facing ][HyruleCastleSolver.X ]
          yLoc += HyruleCastleSolver.DIRECTIONS[ facing ][HyruleCastleSolver.Y ]

        
  ##################

  def countSquares( self ) :
    sum = 0
    for line in self.room :
      sum += line.count( HyruleCastleSolver.TRAVERSED )
    print( sum )

  ##############

  def main(self) :

    self.processArguments()
    ( self.x, self.y ) = self.findStart()
    self.traverse()
    self.countSquares()


if __name__ == "__main__":
  p = HyruleCastleSolver() 
  p.main()