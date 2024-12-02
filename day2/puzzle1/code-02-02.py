import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class ReactorSolver :

  DEFAULT_FILE = "day2\\puzzle1\\input.txt"
  DAY = 2
  verbosePrint = True


  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.distance = 0
    self.reports = []
    self.safeValue = 3
    self.dampenCapacity = 1

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2024 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=ReactorSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

################

  def readInput( self, fileName ) :
    reports = []
    splitReports = []
    with open( fileName, 'r') as foo :
      reports = foo.readlines()
    
    #splitReports = [ re.split( "\\s+", x.strip() ) for x in reports ]
    for x in reports:
      splitReports.append( [ int(y) for y in re.split( "\\s+", x.strip() ) ] )
    
    self.reports = splitReports

    ###########

  # def isReportSafeUp ( self, report, dampened = 0 ) :
  #   for i in range ( 0, ( len(report) - 1 ) ) :
  #     if report[i+1] - report[i] not in range (1, 1+self.safeValue) :
  #       DebugPrinter.debugPrint ( "Failed Up on i=%d - %d and %d" % ( i, report[i], report[i+1]) )
  #       if dampened < self.dampenCapacity :
  #         reportLessI = report.copy()
  #         reportLessIAnd1 = report.copy()

  #         del reportLessI[i]
  #         del reportLessIAnd1[i+1]
  #         return ( self.isReportSafeUp( reportLessI, dampened+1 ) or self.isReportSafeUp( reportLessIAnd1, dampened+1 ) )
  #       else:
  #         return False
  #   return True
  
  # def isReportSafeDown ( self, report, dampened = 0 ) :
  #   for i in range ( 0, ( len(report) - 1 ) ) :
  #     if report[i+1] - report[i] not in range (0-self.safeValue, 0) :
  #       DebugPrinter.debugPrint ( "Failed Down on i=%d - %d and %d" % ( i, report[i], report[i+1]) )
  #       if dampened < self.dampenCapacity :
  #         reportLessI = report.copy()
  #         reportLessIAnd1 = report.copy()

  #         del reportLessI[i]
  #         del reportLessIAnd1[i+1]
  #         return ( self.isReportSafeDown( reportLessI, dampened+1 ) or self.isReportSafeDown( reportLessIAnd1, dampened+1 ) )
  #       else:
  #         return False
  #       return False
  #   return True
  
  def isReportSafeEitherWay ( self, report, myRange, dampened = 0 ) :
    for i in range ( 0, ( len(report) - 1 ) ) :
      #if report[i+1] - report[i] not in range(myRange[0], myRange[1] ) :
      if report[i+1] - report[i] not in myRange :
        DebugPrinter.debugPrint ( "Failed Down on i=%d - %d and %d" % ( i, report[i], report[i+1]) )
        if dampened < self.dampenCapacity :
          reportLessI = report.copy()
          reportLessIAnd1 = report.copy()

          del reportLessI[i]
          del reportLessIAnd1[i+1]
          return ( self.isReportSafeEitherWay( reportLessI, myRange, dampened+1 ) or self.isReportSafeEitherWay( reportLessIAnd1, myRange, dampened+1 ) )
        else:
          return False
        return False
    return True
  
  ############

  def getSafeReportCount( self ) :
    countSafe = 0
    for report in self.reports :
      DebugPrinter.debugPrint ( "TESTING - " + str(report ) )
      ###if ( self.isReportSafeUp( report ) or self.isReportSafeDown( report ) ) :
      if ( self.isReportSafeEitherWay( report, range(1, 1+self.safeValue) ) or self.isReportSafeEitherWay( report, range(0-self.safeValue, 0 ) ) ) :
        DebugPrinter.debugPrint ( "Success - " + str(report ) )
        countSafe +=1
      else :
        DebugPrinter.debugPrint ( "Fail - " + str(report ) )
    print( countSafe )
    return countSafe

  ##############

  def main(self) :

    self.processArguments()
    self.getSafeReportCount()

if __name__ == "__main__":
  p = ReactorSolver() 
  p.main()