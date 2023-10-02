### PMX Model specific settings
You can locate the model specific physics settings in model settings -> Options -> Physics

![Model Physics](/images/model-physics.png)

Firmness
:  This is an overall multiplier applied to the spring force of all joints. Increasing the value will reduce movements. On top of this you can control spring forces for linear and angular movements individually using the settings below.

Linear Movement
:  Choose how linear movements are restricted for all joints. Auto will set restriction based on the linear limit defined in the model. If the limit is smaller than a small amount, it will be locked otherwise it will be limited. "Bounciness" controls how much velocity is preserved when it hit the edge of its limit and bounce back. "Contact distance" decides when to apply limit spring force when it goes near its limit, 0 means it moves freely until it actually hits the limit, 1 means that the force is always applied when it is with in the limit. 

Angular Movement
:  Similar to the linear movement above, this one controls angular movements of all joints.

Linear Drive
:  This controls how much spring force is used to make the connected object to return to its original positoin. The "Target" setting here controls where the neutural position is. 

Angular Drive
:  This controls the force that make objects to return to their orientation. 

Projection Dist
:  Projection distance. If the distance between the 2 connected objects is greater than the value defined here, the objects will be moved back to avoid runaway situation. 

Projection Angle
:  Similar to above, this one controls rotation. 

Reset on change
:  Once toggled, whenever a change is made here, all the bones are reset to their initial position before the new settings values are applied. This can prevent bones drifting off while changing physics settings. But sometimes this makes it hard to observe the effect of the change, in that case you can turn this option off before you make your changes, and then turn it back on after you found your ideal settings. 

Within movement and drive settings, there are a few common setting values

Spring Force
:  Used to calculate force based on Hooke's law

Damp / drag
:  How much force is applied to stop the movements in ralation to the current velocity. 