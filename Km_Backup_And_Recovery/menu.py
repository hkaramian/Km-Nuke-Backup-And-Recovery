
import nuke

## Define Rimiya Menu
menubar = nuke.menu('Nodes') ## for top menu : nuke.menu('Nuke')
km_bakup_menu = menubar.addMenu('Km Backup And Recovery Toolkit', icon=os.path.dirname(__file__)+'/icons/backup_on.png')



import km_bakup


#import test
## for test
##############
km_bakup_menu.addCommand('Km Backup And Recovery Toolkit', "km_bakup.show_panel()", icon=os.path.dirname(__file__)+'/icons/icon_holder.png')


#def onsave_alert() :
#    nuke.message("save shod")


##nuke.addOnScriptSave(onsave_alert)