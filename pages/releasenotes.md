## 0.7.1


## 0.7
https://www.patreon.com/posts/40230045

## 0.6.3
https://www.patreon.com/posts/38558214

## 0.6.2
https://www.patreon.com/posts/37468147

## 0.6.1
https://www.patreon.com/posts/36658089

## 0.6
https://www.patreon.com/posts/35668142

## 0.5.3
https://www.patreon.com/posts/34899808

## 0.5.2
https://www.patreon.com/posts/34158834

## 0.5.1
https://www.patreon.com/posts/33671682

## 0.5
https://www.patreon.com/posts/33251174

## 0.4.4
https://www.patreon.com/posts/32972137

## 0.4.3
https://www.patreon.com/posts/32321052

## 0.4.2
https://www.patreon.com/posts/32321052

## 0.4
https://www.patreon.com/posts/31715495
* Custom stages (public version has 3 built-in stages to choose from while private version allows loading stage files from your content folder)
* Virtual screens. This was available in early versions but later removed for performance reasons. Now it can be turned on in stage settings.  
* Lighting control moved to stage settings, so each stage can have its own lighting setup. 
* Saved scene data now include stage & its settings.
* Various other fixes & improvements.


## 0.3.2
https://www.patreon.com/posts/31300717 
* Media player repeat modes, 
You can now switch between single / repeat one / repeat all / shuffle modes with a single button
* Corrected camera track interpretation 
Camera motion was wrong in all previous versions due to lack of documentation on the VMD file format. We've now worked out the correct interpretation so camera tracks will exactly match MikuMikuDance playback. 
* UI updates & animations
Now there are smooth transitions between UI windows. 
* Load scene feature now available in public builds
For content creators to publish their work with public builds of DVVR. 
* All slider controls now have a simple toggle to turn on automatic updates with music timeline.  
Once toggled on, the value will automatically be updated with the percentage value from music progress.  
* Dissolving effect now available in private builds
A fully customizable shader effect that simulates dissolving/tearing of cloth. 


## 0.3.1
* Upgrade to Unity 2019.3, tons of updates & fixes from Unity for better performance & stability.

* UI updates, as demonstrated in our previous video

Added favorite & recent lists, dropdown selection of motion tracks. 

* Control updates, unified controls for VR & desktop mode. 

Left joystick / WASD: free fly

Right joystick / Arrow keys : move up / down & rotate

Left grip + trigger : center on actor

* Added area light to simulate light bounces from the floor (HDRP only)


## 0.3
* New motion settings
* UI improvements
* Relative path
* Motion selection list now supports folders
* Save & load scenes for private builds

## 0.2.5
Bug fixes, physics stability & UI updates

Both Private & Public branch:
* HDRP build first public release
* Soft shadow!
* Physics improvements
  * Fixed physics issues on certain models
  * Improve stability
* Further improvements of feet adjustment
* Fixed camera motion FOV
* Improved camera motion adjustment, can change height & FOV offsets
* Improved default motion scale

Private branch only:
* Fixed reflection control
* Overall material control
  * Change glossness of all materials
  * Added material modifications
* Various posing controls to blend actor pose 

## 0.2.4
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
  * Tick the track from UI or use C key to activate camera track
  * Camera tracks will stay inactive when UI is on screen, to ensure UI is controllable. Simply toggle off UI with left-hand menu button or Tab key on the keyboard to turn off UI and activate the selected camera track.
  * To quit the camera control, toggle on UI again then tick off the camera track. 
  

## 0.2.3
### Both private and public branches. 
Bug fixes & compatibility improvements.

Model compatibility
* Ground position
* Center Correction
* Missing texture

Bug fixes
* Audio motion lag
* Actor position lock fix
* UI fixes

New
* Refine spotlight control
* Simple looping
* Micro motion
* WASD keyboard control in VR
 

## 0.2.2

### Public branch
* LWRP pipeline
* Fixed material glossiness presentation
* Fixed foot IK for certain dance motions
* Reworked config UI

### Private branch
* HDRP pipeline
Everything in public branch plus
* Volumetric fog
* Floor reflection
* Physics controled light balls

## 0.2
* Support for XPS models
* Async loading
* Reworked IK solution
* Suport for non A-pose models
* Enabled morph control


## 0.1
First public release
* Support for PMX models
* Support for VMD motion
* Automatic correction of bone structure 
* IK support for non-IK models
* Foot correction
