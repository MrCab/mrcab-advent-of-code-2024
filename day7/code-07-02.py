import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class TreeNode :

  def __init__( self, num=0 ) :
    self.num = num
    self.total = num
    self.plusNode = None
    self.multNode = None
    self.concatNode = None

  def addNode( self, num ) :

    if self.plusNode != None:
      self.plusNode.addNode( num )
    else: 
      self.plusNode = TreeNode()
      self.plusNode.num = num
      self.plusNode.total = self.total + num

    if self.multNode != None:
      self.multNode.addNode( num )
    else:
      self.multNode = TreeNode()
      self.multNode.num = num
      self.multNode.total = self.total * num

    if self.concatNode != None :
      self.concatNode.addNode( num )
    else:
      self.concatNode = TreeNode()
      self.concatNode.num = num
      self.concatNode.total = int( str(self.total) + str(num) )

    
  def treeContains( self, total ) :
    answer = False
    if self.plusNode != None :
      if self.concatNode == None:
        print( "break")
      answer = self.plusNode.treeContains( total ) or self.multNode.treeContains( total ) or self.concatNode.treeContains( total )
    else :
      answer = total == self.total
    return answer
    

class WowieZowieSolver :

  DEFAULT_FILE = "day7\\input.txt"
  #DEFAULT_FILE = "day7\\sample.txt"
  DAY = 7
  verbosePrint = True


  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.lines = []

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=WowieZowieSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    #self.readInput( args.input )

    with open( args.input, 'r') as foo :
      self.lines = foo.readlines()
    self.lines = [ l.strip() for l in self.lines ]


################

  def butterBridge2( self ) :
    sum = 0

    for line in self.lines :
      a = re.split( ':\s*', line )
      total = int(a[0])
      nums = a[1].split( " " )

      tree = TreeNode( int(nums[0] ) )
      for num in nums[1:]:
        tree.addNode( int(num) )
      if tree.treeContains( total ) :
        sum += total
    print( sum )


  ##############

  def main(self) :

    self.processArguments()
    self.butterBridge2()

if __name__ == "__main__":
  p = WowieZowieSolver() 
  p.main()