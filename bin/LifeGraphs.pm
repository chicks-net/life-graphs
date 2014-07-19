package LifeGraphs;

use strict;
use warnings;
use Data::Dumper; # just for debugging
#use Time::HiRes qw(gettimeofday tv_interval usleep);

use vars qw($VERSION @EXPORT @EXPORT_OK @ISA);
$VERSION = "0.1";

BEGIN {
    require Exporter;
    @ISA = qw(Exporter);
    @EXPORT = qw(trim);
    @EXPORT_OK = qw(trim);
}

sub new {
	my $class = shift;
	my $self = {
	};

	bless $self, $class;
	return $self;
}

sub trim {
	my ($value) = @_;

	# TODO: handle lists of values

	$value =~ s/^\s+//;
	$value =~ s/\s+$//;

	return $value;
}

1;

__END__

=head1 NAME

Life::Graphs - utilities for life graphs

=head1 SYNOPSIS

   use LifeGraphs;

   my $clean_string = trim($scraggly_string);

=head1 DESCRIPTION

There is not
much to say
at this point.

=head2 METHODS

=head3 new

Create a new object.  There's no point really.

=head3 trim

Get the rid of leading and trailing whitespace.

=head1 TODO

=over 4

=item * move this into the lib directory

=item * centralize json and storable reading and writing

=item * write some tests

=back

=head1 SEE ALSO

Manpages: ganglia(1)

=head1 AUTHOR

Christopher Hicks E<lt>chicks.net@gmail.comE<gt>

=head1 COPYRIGHT AND LICENSE

Copyright 2014 Christopher Hicks

This software is licensed under the Gnu Public License (GPL) version 2.
