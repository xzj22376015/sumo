#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2010-2021 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    addParkingAreaStops2Routes.py
# @author  Evamarie Wiessner
# @date    2017-01-09

"""
add stops at parkingAreas to vehicle routes
"""

from __future__ import print_function
from __future__ import absolute_import
import os
import sys
import optparse
try:
    import xml.etree.cElementTree as ET
except ImportError as e:
    print("recovering from ImportError '%s'" % e)
    import xml.etree.ElementTree as ET


if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

import sumolib  # noqa


def get_options(args=None):
    optParser = optparse.OptionParser()
    optParser.add_option("-f", "--file", dest="file", help="define the XML input file")
    optParser.add_option("-o", "--output", dest="output", help="define the XML output file")
    optParser.add_option("--operation", dest="operation", help="operation (add(update) or remove)")
    optParser.add_option("-t", "--tag", dest="tag", help="tag to edit")
    optParser.add_option("-a", "--attribute", dest="attribute", help="attribute to edit")
    optParser.add_option("-v", "--value", dest="value", help="value to update")
    (options, args) = optParser.parse_args(args=args)
    if not options.file:
        optParser.print_help()
        sys.exit()
    return options


def main(options):
    # open output file
    with open(options.output, 'w') as outf:
        # parse tree
        tree = ET.parse(options.file)
        # obtain root
        root = tree.getroot()
        # iterate over all XML elements
        for it in root.iter():
            # check tag
            if (it.tag == options.tag):
                # continue depending of operation
                if (options.operation == "add"):
                    # set new attribute (or modify existent)
                    it.set(options.attribute, options.value)
                else:
                    # delete attribute
                    del it.attrib[options.attribute]
        # write modified tree
        tree.write(options.output)

if __name__ == "__main__":
    options = get_options(sys.argv)
    main(options)
