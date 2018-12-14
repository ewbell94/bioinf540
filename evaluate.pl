use strict;
use warnings;

open(my $testlist,"all.list");
my @matrix=([0,0],[0,0]);
while (my $line=<$testlist>){
    my @parts=split(' ',$line);
    print "$parts[0]\n";
    my $result=`python domainDetector.py dataset/$parts[0]\.pdb`;
    print "$result";
    chomp($result);
    my @resparts=split(',',$result);
    my $i=0;
    $i=1 if ($parts[2] != 1);
    my $j=0;
    $j=1 if (scalar(@resparts) > 0);
    $matrix[$i][$j]++;
    print "$matrix[0][0] $matrix[0][1]\n";
    print "$matrix[1][0] $matrix[1][1]\n";
}

