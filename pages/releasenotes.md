## 0.2.4
* Able to launch in desktop mode only from a shortcut argument. 
* Error handling when loading texture maps. Ignores texture error so the app can continue to function.
* Found a better way to find model ground position, the "Ground" settings is no longer necessary and removed from UI.
* Feet correction improvements 
* Added texture settings for PMX models, can be used to change texture modes when the default value is not working well. 
* Updated PMX model physics interpretation, there are still issues in this area and will continue to work on this in the future versions.
* Control updates
  * Keyboard C to toggle camera tracks
  * WASD now works in VR when hand controllers available
  * Updated hand controller detection
  * Attempt to get Index controller to work with UI
* Camera tracks work in VR. 
  1. Tick the track from UI or use C to activate camera track
  2. Toggle off UI with controller menu button or Tab key on keyboard. The camera track controls main camera when UI is not present.
  3. To quit the camera control, toggle on UI again then tick off the camera track. 
*Changes available in both public and private release branches*

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
