import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )
    

class Pathfinder :

  DEFAULT_FILE = "day10\\input.txt"
  #DEFAULT_FILE = "day10\\sample.txt"
  #DEFAULT_FILE = "day10\\two.txt"
  DAY = 10
  verbosePrint = True
  BLANK = "."
  PATH = ['0','1','2','3','4','5','6','7','8','9']

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.lines = []
    self.pathCount = 0
    self.currentCount = 0
    self.trailheads = {}
    self.trailEnds = {}
    self.currentHead = (0,0)
    


##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=Pathfinder.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    #self.readInput( args.input )

    with open( args.input, 'r') as foo :
      self.lines = foo.readlines()
      self.lines = [ l.strip() for l in self.lines ]

  ##########
  def trailblaze( self, path ) :
    rating = 0
    for y in range( 0, len( self.lines ) ) :
      for x in range( 0, len( self.lines[y] ) ) :
        if self.lines[y][x] == path[0] :
          self.currentHead = (x, y )
          rating += self.checkNeighbors( x, y, 1 )

    print( "Part 2 Rating: %d" % ( rating ) )

    # print the trailhead score
    sum = 0
    for k in self.trailheads.keys() :
      sum += len( self.trailheads[ k ].keys() )
    print( "Part 1 score: %d" % (sum) )

  ####
  def checkNeighbors( self, x, y, nextOne ) :
    rating = 0
    if self.lines[y][x] == Pathfinder.PATH[-1] and nextOne == len( Pathfinder.PATH ):
      self.markTrailEnd( x, y )
      self.markTrailHead( self.currentHead[0], self.currentHead[1], x, y )
      return 1
    # up
    if self.isInBounds( x, y-1 ) and self.lines[ y-1][x] == Pathfinder.PATH[nextOne] :
      rating += self.checkNeighbors( x, y-1, nextOne+1 )
    # down
    if self.isInBounds( x, y+1 ) and self.lines[ y+1][x] == Pathfinder.PATH[nextOne] :
      rating += self.checkNeighbors( x, y+1, nextOne+1 )

    # left
    if self.isInBounds( x-1, y ) and self.lines[ y][x-1] == Pathfinder.PATH[nextOne] :
      rating += self.checkNeighbors( x-1, y, nextOne+1 )
    # right
    if self.isInBounds( x+1, y ) and self.lines[ y][x+1] == Pathfinder.PATH[nextOne] :
      rating += self.checkNeighbors( x+1, y, nextOne+1 )
    return rating

###########
  def isInBounds( self,x, y ) :
    return ( x in range( 0, len( self.lines[0] ) ) and y in range( 0, len( self.lines ) ) )

########
  def markTrailHead( self, hx, hy, endx, endy ) :
    if ( hx, hy ) not in self.trailheads.keys() :
      self.trailheads[ ( hx, hy ) ] = {}
    self.trailheads[ ( hx, hy ) ][ (endx, endy ) ] = True


########
  def markTrailEnd( self, x, y ) :
    if ( x, y ) in self.trailEnds.keys() :
      self.trailEnds[ ( x, y ) ] += 1
    else:
      self.trailEnds[ ( x, y ) ] = 1

  ##############

  def main(self) :

    self.processArguments()
    self.trailblaze( Pathfinder.PATH )

if __name__ == "__main__":
  p = Pathfinder() 
  p.main()