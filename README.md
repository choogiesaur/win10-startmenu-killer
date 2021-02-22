# win10-startmenu-killer

This is a quick python app to kill three processes associated with the Windows 10 start menu and its search bar:
- SearchApp.exe
- SearchIndexer.exe
- StartMenuExperienceHost.exe

It's useful for people who sometimes experience an issue where they can click both the Windows icon and the search bar, but neither menu loads up. After running this, when clicking the menu or search bar Windows will automatically reload their processes and they should function properly.

Protip: After running, pin this utility to your task bar!

Zipped executable: [kill-startmenu-gui.zip](https://github.com/choogiesaur/win10-startmenu-killer/files/6024238/kill-startmenu-gui.zip "Windows 10 Start Menu Killer 1.0 zip")

Build a new .exe using pyinstaller with this command:

```pyinstaller --onefile --windowed --icon=SpecialAttackPSO.ico .\kill-startmenu-gui.py```
