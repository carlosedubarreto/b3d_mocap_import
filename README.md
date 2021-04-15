# b3d_mocap_import
addon for blender to import mocap data from tools like easymocap, frankmocap and Vibe


==================VIBE==================

To use VIBE you have to install it using


https://github.com/mkocabas/VIBE

if you are on windows, you can follow this repo

https://github.com/carlosedubarreto/vibe_win_install

explained in this tutorial


========================================

===============FRANKMOCAP===============

To use frankmocap you have to install it using

https://github.com/facebookresearch/frankmocap

if you are on windows, you can follow this repo

https://github.com/carlosedubarreto/frankmocap_win_install

explained in this tutorial


========================================

--------------------------------------------------------------

Version Beta 0.6
Tools for making the mocap data be centered and in the right orientation

Version Beta 0.51
Fix a problem using on other than Windows environment, thanks to k30n1 on GitHub

Version Beta 0.5
- Better skeleton. Now you can do retargetting for:

    -- Vibe

    -- Frankmocap

    -- MediaPipe

- Multiplier to fine tune the bones proportions



PS.: On my tests, the better mutliplier is between 0.7 and 1.2



Version Beta 0.4
Now we have MediaPipe inside of blender, you can make a pose estimation choosing a video file.
PS.: You must first click on the install MediaPipe Button



Version Beta 0.3
Fix for non englsh languages.

Easymocap has some issues, but work most of the time,

Version Beta 0.2
Import of Frankmocap and VIBE

PS.: To use VIBE you must install a python package inside Blender.

To do that, you have to get your blender path and replace in the following command line (and execute in Windows CMD) if you have further problems, contact me on twitter(https://twitter.com/carlosedubarret)



The Commandline: 

D:\Blender\blender-2.92.0-windows64\2.92\python\bin\python.exe D:\Blender\blender-2.92.0-windows64\2.92\python\lib\site-packages\pip install joblib



Version Beta 0.1
This version imports data from Easymocap only. (https://github.com/zju3dv/EasyMocap)



For contact you can reach me at:

https://twitter.com/carlosedubarret



If you find bugs, please report them here:

https://github.com/carlosedubarreto/b3d_mocap_import/issues
