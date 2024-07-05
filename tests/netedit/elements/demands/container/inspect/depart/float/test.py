#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2009-2024 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2019-07-16

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to demand mode
netedit.supermodeDemand()

# go to container mode
netedit.containerMode()

# create container using three edges
netedit.leftClick(referencePosition, netedit.positions.elements.edge0.x, netedit.positions.elements.edge0.y)
netedit.leftClick(referencePosition, netedit.positions.elements.edge2.x, netedit.positions.elements.edge2.y)

# press enter to create container
netedit.typeEnter()

# go to inspect mode
netedit.inspectMode()

# inspect container
netedit.leftClick(referencePosition, netedit.positions.elements.demands.container.x,
                  netedit.positions.elements.demands.container.y)

# change depart with an invalid value
netedit.modifyAttribute(netedit.attrs.container.inspect.depart, "", False)

# change depart with an invalid value
netedit.modifyAttribute(netedit.attrs.container.inspect.depart, "dummyDepart", False)

# change depart with an invalid value
netedit.modifyAttribute(netedit.attrs.container.inspect.depart, "-3", False)

# change depart with an valid value
netedit.modifyAttribute(netedit.attrs.container.inspect.depart, "10.2", False)

# Check undo
netedit.checkUndoRedo(referencePosition)

# save Netedit config
netedit.saveNeteditConfig(referencePosition)

# save containers
# quit netedit
netedit.quit(neteditProcess)