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
    self.cache = {}
    self.newCache = {}

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
    for l in self.line :
      self.cacheIt( l, 1 )
    self.cache = self.newCache


######
  def cacheIt( self, stone, num ) :
    if stone in self.newCache.keys() :
      self.newCache[stone] += num
    else:
      self.newCache[stone] = num

  ##########
  def blink( self ) :
    # the short version is, the order doesn't matter
    # also clear cache
    self.newCache = {}
    for stone in self.cache.keys() :

      if stone == "0" :
        self.cacheIt( '1', self.cache[stone] )
      elif len(stone) % 2 == 0 :
        foo = len(stone)//2
        self.cacheIt( stone[0:foo], self.cache[stone] )

        bar = re.sub( "^0+(\\d)", "\\1", stone[foo:] )
        self.cacheIt( bar, self.cache[stone] )
      else:
        num = int(stone) * 2024
        self.cacheIt( str( num ), self.cache[stone] )
    self.cache = self.newCache

  #############
  def countRocks( self ) :
    sum = 0
    for r in self.cache.keys() :
      sum += self.cache[r]
    return sum

  ##############

  def main(self) :

    self.processArguments()
    for i in range( 0, 75 ) :
      self.blink( )

      print( "blink %d - %d stones" % ( i, self.countRocks() ) )

if __name__ == "__main__":
  p = StoneSolver() 
  p.main()