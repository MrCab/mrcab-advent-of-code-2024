import re
import argparse
from fractions import Fraction

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )
    

class WifiSolver :

  DEFAULT_FILE = "day8\\input.txt"
  #DEFAULT_FILE = "day8\\sample.txt"
  DAY = 8
  verbosePrint = True
  BLANK = "."

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.lines = []
    self.antiNodes = {}
    self.nodes = {}
    self.xLen = 0
    self.yLen = 0

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=WifiSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

    # with open( args.input, 'r') as foo :
    #   self.lines = foo.readlines()
    # self.lines = [ l.strip() for l in self.lines ]

######
  def readInput( self, fileName ) :
    lines = None
    with open( fileName, 'r') as foo :
      lines = foo.readlines()
      lines = [ l.strip() for l in lines ]
      lines = [ list(l) for l in lines ]

    self.yLen = len( lines )
    self.xLen = len( lines[0] )

    for y in range( 0, self.yLen ) :
      for x in range( 0, self.xLen ):
        if lines[y][x] != WifiSolver.BLANK :
          anttype = lines[y][x]
          if anttype in self.nodes.keys() :
            self.nodes[ anttype ].append( ( x, y ) )
          else :
            self.nodes[ anttype ] = [ ( x, y ) ]

    self.lines = lines

################

  def findAntinodes1( self ) :
    for anttype in self.nodes.keys() :
      locs = self.nodes[ anttype ]
      for i in range( 0, len( locs ) - 1 ):
        cur = locs[i]
        theRest = locs[ i+1: ]
        for j in theRest :
          self.markAntinodes( cur, j )

    print( len( self.antiNodes.keys() ) )

######
  def markAntinodes1( self, loc1, loc2 ) :
    delX = loc1[0] - loc2[0]
    delY = loc1[1] - loc2[1]

    anode1 = ( ( loc1[0] + ( delX)), ( loc1[1] + ( delY) ) )
    anode2 = ( ( loc2[0] - ( delX)), ( loc2[1] - ( delY) ) )

    self.flagAntinode( anode1 )
    self.flagAntinode( anode2 )

######
  def markAntinodes( self, loc1, loc2 ) :
    delX = loc1[0] - loc2[0]
    delY = loc1[1] - loc2[1]

    # NOTE - THIS SHOULD FAIL FOR A HORIZONTAL LINE WHERE delY = 0
    # should say if delY = 0 then slopeX = 1, slopeY = 0, and proceed
    slope = Fraction( delX, delY )
    slopeX = slope.numerator
    slopeY = slope.denominator

    mark = loc1
    while ( 0 <= mark[0] < self.xLen ) and mark[1] in range( 0, self.yLen ) :
      self.flagAntinode( mark )
      mark = ( mark[0] + slopeX, mark[1] + slopeY )
      #anode1 = ( ( loc1[0] + ( delX)), ( loc1[1] + ( delY) ) )

    mark = loc1
    while ( 0 <= mark[0] < self.xLen ) and mark[1] in range( 0, self.yLen ) :
      self.flagAntinode( mark )
      mark = ( mark[0] - slopeX, mark[1] - slopeY )
      #anode2 = ( ( loc2[0] - ( delX)), ( loc2[1] - ( delY) ) )

######
  def flagAntinode( self, loc ) :
    #if loc[0] in range( 0, self.xLen ) and loc[1] in range( 0, self.yLen ) :
    if ( 0 <= loc[0] < self.xLen ) and loc[1] in range( 0, self.yLen ) :
      self.antiNodes[ loc ] = True

  ##############

  def main(self) :

    self.processArguments()
    self.findAntinodes1()

if __name__ == "__main__":
  p = WifiSolver() 
  p.main()