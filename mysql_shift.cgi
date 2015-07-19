#!/usr/bin/perl --

use URI;
use DBI;
&joint;
&joint2;
&shift;
exit;



sub shift{


$sth = $db->prepare("SELECT * FROM kareshi_hoshi;");
$sth->execute;
while (my @row = $sth->fetchrow_array) {
	my $a = $row[0];
	my $b = $row[1];
	my $c = $row[2];
	my $d = $row[3];
	my $e = $row[4];
	my $f = $row[5];
	my $g = $row[6];
	my $h = $row[7];
	my $i = $row[8];
	my $j = $row[9];
	my $k = $row[10];
	my $l = $row[11];
	my $m = $row[12];
  	$sth2 = $db2->prepare("INSERT INTO kareshi_hoshi2(no,flag,name,screen_name,user_id,tweet,tweet_id,date,follow,follower,ff,description,source) VALUES (\"$a\",\"$b\",\"$c\",\"$d\",\"$e\",\"$f\",\"$g\",\"$h\",\"$i\",\"$j\",\"$k\",\"$l\",\"$m\");");
	$sth2->execute;
}#foreach

$sth->finish;
$db->disconnect;

#print "Content-type: text/html \n\n";
print "ok";


}#sub end




sub joint{
my $user = 'root';
my $passwd = 'mugen19260327';
my $db_name = 'DBI:mysql:twitter_bot:localhost';
$db = DBI->connect($db_name, $user, $passwd,{'mysql_enable_utf8'=>1});
}#sub joint2 end

sub joint2{
my $user = 'root';
my $passwd = 'mugen19260327';
my $db_name = 'DBI:mysql:twitter_bot:localhost';
$db2 = DBI->connect($db_name, $user, $passwd,{'mysql_enable_utf8'=>1});
}#sub joint3 end
