#!/usr/bin/env ruby
#Original file's google_geolocate_bssid Metaspoilt recon tool
msfbase = __FILE__
while File.symlink?(msfbase)
  msfbase = File.expand_path(File.readlink(msfbase), File.dirname(msfbase))
end

$LOAD_PATH.unshift(File.expand_path(File.join(File.dirname(msfbase), '..', '..','lib')))
require 'rex/google/geolocation'
require 'optparse'

g = Rex::Google::Geolocation.new
ARGV.each do |mac|
  g.add_wlan(mac, nil, -83)
end

g.fetch!

puts g, g.google_maps_url
