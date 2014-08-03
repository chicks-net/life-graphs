package LifeGraphs;

use strict;
use warnings;
use English;
use Carp;
use Data::Dumper;    # just for debugging
use DateTime;
use LWP::Simple qw(get);
use HTML::TreeBuilder;
use JSON;
use Storable qw(nstore retrieve);

#use Time::HiRes qw(gettimeofday tv_interval usleep);
#use Readonly;

use vars qw($VERSION @EXPORT @EXPORT_OK @ISA);
$VERSION = "0.1";

BEGIN {
	require Exporter;
	@ISA       = qw(Exporter);
	@EXPORT    = qw(get_now_text get_storable parse_statsday trim url_tree verify_datadir write_json write_storable);
	@EXPORT_OK = qw();
}

sub new {
	my $class = shift;
	my $self  = {};

	croak "this is useless, didn't you read the docs?";

	#bless $self, $class;
	#return $self;
}

sub get_now_text {
	my $stats_time = DateTime->now->format_cldr("yyyy-MM-dd HH:mm");
	return $stats_time;
}

sub get_storable {
	my ( $filename, $quiet ) = @_;
	$quiet = 0 unless defined $quiet;

	my $data;

	if ( -f $filename ) {
		print "starting with $filename\n" unless $quiet;
		$data = retrieve $filename;
	} else {
		warn "starting empty since there is no $filename\n";
		$data = {};
	}

	return $data;
}

sub parse_statsday {
	my ($statsday) = @_;

	if ( $statsday =~ /^(\d+)-(\d+)-(\d+) (\d+):(\d+)$/ ) {
		my $year = $1;
		my $month = $2;
		my $day = $3;
		my $hour = $4;
		my $minute = $5;

		my $stats_date_object = DateTime->new(
                        year      => $year,
                        month     => $month,
                        day       => $day,
                        hour      => $hour,
                        minute    => $minute,
                        second    => 0,
                        time_zone => 'UTC',
                );

		return $stats_date_object;
	} else {
		die "'$statsday' does not fit pattern";
	}
}

sub trim {
	my ($value) = @_;

	# TODO: handle lists of values

	$value =~ s/^\s+//;
	$value =~ s/\s+$//;

	return $value;
}

sub url_tree {
	my ($url) = @_;

	my $retries = 5;
	my $raw_html;
	while ($retries) {
		$raw_html = get($url);
		last if defined $raw_html;
		my $sleep_secs = int(rand(20)*(6-$retries));
		print "\tsleeping for $sleep_secs seconds on failed GET $url\n";
		sleep($sleep_secs);
		$retries--;
	}
	croak "failed on GET $url" unless defined $raw_html;
	my $raw_length = length $raw_html;
	print "got $raw_length bytes from $url\n";

	# parse
	my $tree = HTML::TreeBuilder->new;    # empty tree
	$tree->parse_content($raw_html);

	return $tree;
}

# verify data directory
sub verify_datadir {
	my $data_dir = $ENV{STATS_DIR};
	croak "no STATS_DIR defined" unless defined $data_dir;
	croak "$data_dir is not a directory" unless -d $data_dir;
	chdir($data_dir) or croak "somehow failed to chdir($data_dir): $ERRNO";
	return $data_dir;
}

sub write_json {
	my ( $filename, $data ) = @_;
	my $json     = JSON->new->allow_nonref;
	my $json_out = $json->pretty->canonical->encode($data);
	my $json_fh;
	open( $json_fh, ">", $filename ) or croak "could not open $filename for write: $ERRNO";
	print $json_fh $json_out;
	close($json_fh);
	my $size = -s $filename;
	print "wrote $filename ($size bytes)\n";
	return $size;
}

sub write_storable {
	my ( $filename, $data ) = @_;
	nstore $data, $filename or croak "writing $filename failed: $ERRNO";
	my $size = -s $filename;
	print "wrote $filename ($size bytes)\n";
	return $size;
}

1;

__END__

=head1 NAME

Life::Graphs - utilities for life graphs

=head1 SYNOPSIS

   use LifeGraphs;

   my $clean_string = trim($scraggly_string);

   my $ref = get_storable($filename);

   my $tree = url_tree($url);

   write_json($filename,$ref);
   write_storable($filename,$ref);

=head1 DESCRIPTION

These functions seem to be needed by almost every web scraping bot so don't reinvent the wheel.

=head2 METHODS

=head3 new

Create a new object.  There's no point really.

=head3 get_storable

Load a storable and return a reference.  Return an empty hash if the storable file does not exist;

=head3 parse_statsday

Take a <code>YYYY-MM-DD HH:MM</code> timestamp like <code>'2014-07-27 02:13'</code> and return a <code>DateTime</code> object.

=head3 trim

Get the rid of leading and trailing whitespace.

=head3 url_tree

GET a URL and return an HTML::TreeBuilder tree.

=head3 verify_datadir

Pulls STATS_DIR from the environment, verifies that it is a directory, and chdir's to it.  Returns the directory.
verify_datadir() takes no arguments.

=head3 write_json

Write a canonical JSON file.  The first argument is a filename and the second is a reference to the data structure to write.
It will return the number of bytes written after printing a success message.

=head3 write_storable

Write a Storable file.  The first argument is a filename and the second is a reference to the data structure to write.
It will return the number of bytes written after printing a success message.

=head1 TODO

=over 4

=item * move this into the lib directory

=item * write some tests

=back

=head1 SEE ALSO

Manpages: ganglia(1), Storable(3pm)

=head1 AUTHOR

Christopher Hicks E<lt>chicks.net@gmail.comE<gt>

=head1 COPYRIGHT AND LICENSE

Copyright 2014 Christopher Hicks

This software is licensed under the Gnu Public License (GPL) version 2.

