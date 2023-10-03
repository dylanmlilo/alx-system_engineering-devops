#!/usr/bin/env ruby
# This script accepts one argument and pass it
# to a regular expression matching method

arg = ARGV[0]
regex = /[S]chool/

match = arg.scan(regex)
puts match.join("")
