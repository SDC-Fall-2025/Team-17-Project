#!perl
# Check consistency between manifest versions
use Encode;
use File::Spec::Functions qw(catfile updir);
use FindBin;
use JSON::PP; # qw(decode_json)
use TOML::Tiny qw(from_toml);
use Test::More tests => 1;

use lib catfile($FindBin::Bin, 'lib');
use MY::Stuff;
$MY::CatFile::ROOT = catfile($FindBin::Bin, updir);

my $js_mf = 'web/package.json';
my $py_mf = 'api/pyproject.toml';

note "package.json is $js_mf";
my $jsver = decode_json(encode "UTF-8", cat split '/' => $js_mf)->{version};

note "pyproject.toml is $py_mf";
my $pyver = from_toml(encode "UTF-8" => cat split '/' => $py_mf)->{project}->{version};

is($jsver => $pyver, "package.json version equals pyproject.toml version");
