use strict;
use warnings;

open(my $infile,"<threadomdataset/test-all.list");
my $done = `cat donefile`;
while(my $line=<$infile>){
    my @parts=split(' ',$line);
    my $pdbid=uc(substr($parts[0],0,4));
    next if ($done=~/$pdbid/);
    my $chainid=substr($parts[0],4,1);
    print "$chainid\n";
    print `wget https://files.rcsb.org/download/${pdbid}\.pdb`;
    open(my $pdbfile,"<$pdbid\.pdb");
    open(my $outpdb,">dataset/$parts[0]\.pdb");
    while(my $pdbline=<$pdbfile>){
	if (substr($pdbline,0,4) eq "ATOM" && substr($pdbline,21,1) eq $chainid){
	    print $outpdb $pdbline;
	}
    }
    close($pdbfile);
    close($outpdb);
    print `rm -rf $pdbid\.pdb`;
    print `echo $pdbid >> donefile`;
}
close($infile);
