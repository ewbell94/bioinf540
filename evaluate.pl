use strict;
use warnings;

open(my $testlist,"data.list");
while (my $line=<$testlist>){
    my @parts=split(',',$line);
    print "$parts[0]\n";
    my $result=`python domainDetector.py dataset/$parts[0]\.pdb`;
    print "$parts[1] $result";
    chomp($result);
}

