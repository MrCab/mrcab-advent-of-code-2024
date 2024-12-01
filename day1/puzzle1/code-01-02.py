import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class LocationSolver :

  DEFAULT_FILE = "day1\\puzzle1\\input.txt"
  DAY = 1
  verbosePrint = True

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.list1 = []
    self.list2 = []
    self.list2Count = {}


  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=LocationSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  def readInput( self, fileName ) :
    lists = []
    numLists = 2
    i = 0
    while i < numLists :
      lists.append( [] )
      i += 1

    foo = open( fileName, 'r').readlines()
    for line in foo :
      x = re.split( "\s+", line )
      DebugPrinter.debugPrint( "Adding " + x[0] + " to list 0" )
      lists[ 0 ].append( int(x[ 0 ]) )
      DebugPrinter.debugPrint( "Adding " + x[1] + " to list 1" )
      lists[ 1 ].append( int(x[ 1 ]) )

      # put this in because I goofed on the first pass and forgot i += 1
      # But why is this broken...
      y = int(x[1]) # this was wrong the first time
      if y in self.list2Count :
        self.list2Count[y] += 1
      else :
        self.list2Count[y] = 1
      

    self.list1 = lists[0]
    self.list2 = lists[1]

#####################

  def LocationMath1( self ) :
    sum = 0
    self.list1.sort()
    self.list2.sort()

    i = 0
    while i < len(self.list1) :
      sum += abs( self.list1[i] - self.list2[i] )
      i += 1

    print ( str( sum ) )

#####################

  def LocationMath2( self ) :
    sum = 0

    i = 0
    while i < len(self.list1) :
      x = self.list1[i]
      # if this used the self.list2count it needs to check if the key exists first
      # but now we remembered i += 1 so the loop actually finished
      sum += x * self.list2.count(x)
      i += 1 # yeah forgot this the first time
    print ( str( sum ) )

##################
  
  def main(self) :

    self.processArguments()
    self.LocationMath2()

if __name__ == "__main__":
  p = LocationSolver() 
  p.main()