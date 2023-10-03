#!/usr/bin/env ruby
# This script accepts one argument and pass it
# to a regular expression matching method
# The regex should not contain square brackets

puts ARGV[0].scan(/hbt*n/).join
