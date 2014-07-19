# NAME

Life::Graphs - utilities for life graphs

# SYNOPSIS

    use LifeGraphs;

    my $clean_string = trim($scraggly_string);

    my $ref = get_storable($filename);

    my $tree = url_tree($url);

    write_json($filename,$ref);
    write_storable($filename,$ref);

# DESCRIPTION

These functions seem to be needed by almost every web scraping bot so don't reinvent the wheel.

## METHODS

### new

Create a new object.  There's no point really.

### get\_storable

Load a storable and return a reference.  Return an empty hash if the storable file does not exist;

### trim

Get the rid of leading and trailing whitespace.

### url\_tree

GET a URL and return an HTML::TreeBuilder tree.

### write\_json

Write a canonical JSON file.  The first argument is a filename and the second is a reference to the data structure to write.
It will return the number of bytes written after printing a success message.

### write\_storable

Write a Storable file.  The first argument is a filename and the second is a reference to the data structure to write.
It will return the number of bytes written after printing a success message.

# TODO

- move this into the lib directory
- write some tests

# SEE ALSO

Manpages: ganglia(1), Storable(3pm)

# AUTHOR

Christopher Hicks <chicks.net@gmail.com>

# COPYRIGHT AND LICENSE

Copyright 2014 Christopher Hicks

This software is licensed under the Gnu Public License (GPL) version 2.
