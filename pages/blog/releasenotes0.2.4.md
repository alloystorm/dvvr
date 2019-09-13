## DVVR 0.2.4

Bug fixes, control & camera updates.
* Able to launch in desktop mode only from a shortcut argument. 
  * Use the included "desktop_only.cmd" to launch in desktop mode only
* Resolution dialog hidden by default
  * Hold down Alt key when launching DVVR if you wish to change resolution/window mode
* Improved error handling when loading texture maps. So the app can continue to function without restart when an error occurs.
* Found a better way to get the model ground position, the "Ground" setting introduced in the previous release is no longer required and removed from UI.
* Updated feet correction, more accurate result.
* Added texture settings for PMX models, can be used to change texture modes when the default value is not working well. 
  * Mode 0: Opaque, 1: Cutoff mode, alpha value lower than 0.5 will be invisible. 2/3: Transparent mode, use alpha channel for transparency.
* Updated PMX model physics interpretation, there are still issues in physics and we will continue to work on this in future releases.
* Control updates
  * Use C key on the keyboard to switch between camera tracks
  * Left Shift + WASD navigation now works in VR when hand controllers are connected
  * Updated hand controller detection
  * Attempt to get Index controller to work with UI, looking forward to hearing from Index users to see if this is working.
* Camera tracks now work in VR. To activate it, 
  1. Tick the track from UI or use C key to activate camera track
  2. Camera tracks will stay inactive when UI is on screen, to ensure UI is controllable. Simply toggle off UI with left-hand menu button or Tab key on the keyboard to turn off UI and activate the selected camera track.
  3. To quit the camera control, toggle on UI again then tick off the camera track. 

Above changes available in both public and private release branches
