import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class MultiplicationSolver :

  DEFAULT_FILE = "day3\\puzzle1\\input.txt"
  DAY = 3
  verbosePrint = True


  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.linesOfCode = []

    #self.searchRegex = re.compile( f'^.*?(?P<command>mul\((?P<num1>(\d{1,3}),(?P<num2>\d{1,3})\))(?P<theRest>.*)' )
    self.searchRegex = re.compile( '^.*?(?P<command>mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\))(?P<theRest>.*)' )
    self.actuallyDoIt = True    
    

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=MultiplicationSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    #self.readInput( args.input )
    with open( args.input, 'r') as foo :
      self.linesOfCode = foo.readlines()

################

  def processCommands( self ) :
    sum = 0
    for line in self.linesOfCode :
       m = self.searchRegex.match( line )
       while m != None :
         sum += ( int( m.groupdict()["num1"]) * int( m.groupdict()["num2"]) )
         m = self.searchRegex.match( m.groupdict()["theRest"])
    print( sum )


  ##############

  def main(self) :

    self.processArguments()
    self.processCommands()

if __name__ == "__main__":
  p = MultiplicationSolver() 
  p.main()