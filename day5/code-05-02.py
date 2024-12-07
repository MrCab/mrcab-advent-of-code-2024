import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class PageOrderSolver :

  # not 5260
  DEFAULT_FILE = "day5\\input.txt"
  #DEFAULT_FILE = "day5\\sample.txt"
  DAY = 5
  verbosePrint = True


  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.linesOfCode = []

    self.pageRules = {}
    self.pageRulesAfter = {}
    self.pageLists = []
    

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=PageOrderSolver.verbosePrint )
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
    
    rules = [ w for w in lines if ( w.find("|") > -1 ) ]
    pages = [ w for w in lines if ( w.find(",") > -1 ) ]

    rules.sort()

    # build up a|b|c|d regex
    for rule in rules :
      r = rule.split("|")
      if r[0] in self.pageRules :
        self.pageRules[ r[0] ] += ( "|" + r[1] )
      else :
        self.pageRules[ r[0] ] = r[1]

      if r[1] in self.pageRulesAfter :
        self.pageRulesAfter[ r[1] ] += ( "|" + r[0] )
      else :
        self.pageRulesAfter[ r[1] ] = r[0]

    self.pageLists = pages

################

  def isInOrder( self, pages) :
    for k in self.pageRules.keys() :
      if re.match( ".*(%s),(.*,)?%s.*" % ( self.pageRules[k] , k), pages ) :
        DebugPrinter.debugPrint( "Failure4" )
        return False      
    for j in self.pageRulesAfter.keys() :
      if re.match( ".*%s,(.*,)?(%s).*" % ( j, self.pageRulesAfter[j] ), pages ) :
        DebugPrinter.debugPrint( "Failure6" )
        return False  

    return True
  
####################

  def findOrder( self, p, num  ) :
    for i in range( 0, len(p) ) :
      q = p.copy()
      q.insert( i, num )
      newOrder = ",".join( q )
      if self.isInOrder( newOrder ) :
        return q
    p.insert( len(p), num )
    return p

##########
  def outOfOrderFixer( self, pages ) :
    p = []
    splitPages = pages.split(',')
    for num in splitPages :
      p = self.findOrder( p, num )

    return int( p[ int( len(p) / 2 ) ] )


#############
  def rulesLawyer( self ) :
    sum = 0
    badSum = 0

    for pages in self.pageLists:
      if self.isInOrder( pages ) :
        p = pages.split(",")
        sum += int( p[ int( len(p) / 2 ) ] )
      else :
        badSum += self.outOfOrderFixer( pages )
    # for page list
    print( "Good: %d" % ( sum ) )
    print( "Bad: %d" % ( badSum ) )

  ##############

  def main(self) :

    self.processArguments()
    self.rulesLawyer()

if __name__ == "__main__":
  p = PageOrderSolver() 
  p.main()