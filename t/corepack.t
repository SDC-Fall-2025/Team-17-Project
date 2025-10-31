#!perl
# Check consistency between corepack package managers
use File::Spec::Functions qw(catfile updir);
use FindBin;
use JSON::PP; # qw(decode_json)
use Test::More tests => 1;

my $top_mf = catfile($FindBin::Bin, updir, 'package.json');
my $web_mf = catfile($FindBin::Bin, updir, 'web', 'package.json');

note "top-level package.json is $top_mf";
my $top_cp = do {
	open my $top_fh, '<', $top_mf or die "open <$top_mf: $!";
	binmode($top_fh, ':utf8');
	my $top_dd = decode_json(do { local $/; <$top_fh> }); # croaks on error
	close $top_fh;
	$top_dd->{packageManager}
};

note "Svelte package.json is $web_mf";
my $web_cp = do {
	open my $web_fh, '<', $web_mf or die "open <$web_mf: $!";
	binmode($web_fh, ':utf8');
	my $web_dd = decode_json(do { local $/; <$web_fh> }); # croaks on error
	close $web_fh;
	$web_dd->{packageManager}
};

is($top_cp => $web_cp, "packageManager in-sync");
