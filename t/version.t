#!perl
# Check consistency between manifest versions
use File::Spec::Functions qw(catfile updir);
use FindBin;
use JSON::PP; # qw(decode_json)
use TOML::Tiny qw(from_toml);
use Test::More tests => 1;

my $js_mf = catfile($FindBin::Bin, updir, 'web', 'package.json');
my $py_mf = catfile($FindBin::Bin, updir, 'api', 'pyproject.toml');

note "package.json is $js_mf";
my $jsver = do {
	open my $js_fh, '<', $js_mf or die "open <$js_mf: $!";
	binmode($js_fh, ':utf8');  # lazy :P
	my $js_dd = decode_json(do { local $/; <$js_fh> }); # croaks on error
	close $js_fh;
	$js_dd->{version}
};

note "pyproject.toml is $py_mf";
my $pyver = do {
	open my $py_fh, '<', $py_mf or die "open <$py_mf: $!";
	binmode($py_fh, ':utf8');
	my $py_dd = from_toml(do { local $/; <$py_fh> });
	close $py_fh;
	$py_dd->{project}->{version}
};

is($jsver => $pyver, "package.json version equals pyproject.toml version");
