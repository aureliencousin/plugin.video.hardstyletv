# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.hardstyletv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_PLAYLIST_ID = "PLUKXSlbHWi2huhANVImh3RxMQ19ASXw6p"

# Entry point
def run():
    plugintools.log("hardstyletv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("hardstyletv.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Hardstyle Livesets",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID+"/",
        thumbnail=icon,
        folder=True )

run()