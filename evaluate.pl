use strict;
use warnings;

open(my $testlist,"<data.list");
open(my $resultfile,">results.list");
while (my $line=<$testlist>){
    my @parts=split(',',$line);
    chomp($parts[1]);
    my $result=`python domainDetector.py dataset/$parts[0]\.pdb`;
    $result=~s/\(//g;
    $result=~s/\)//g;
    my @resparts=split(',',$result);
    $resparts[0]*=1.0;
    $resparts[1]*=1.0;
    $resparts[2]*=1.0;
    print "$parts[0],$resparts[0],$resparts[1],$parts[1],$resparts[2]\n";
    print $resultfile "$parts[0],$resparts[0],$resparts[1],$parts[1],$resparts[2]\n";
}

