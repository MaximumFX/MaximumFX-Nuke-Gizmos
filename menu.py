import nuke

mfx = nuke.toolbar('Nodes').addMenu('MaximumFX', 'MaximumFX.png')
mfx.addCommand('RotoKit', 'nuke.createNode("RotoKit")', icon='RotoKit.png')
