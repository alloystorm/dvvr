### Issues With Transparency

Transparent materials are tricky. They can overlap incorrectly and render unexpected color on top of certain parts if not set correctly. 

We try our best to provide a usable default configuration but there are still models that require manually tweaking before they are renderred correctly. 

To deal with these issues DanceXR has included a few settings for you to tweak your models.

First thing you can try is "Transparency Sorting". This setting configures how transparent materials are sorted in order to address sorting issues. 

The toggle (available in HD variant only) turns on Z sorting, it is the most accurate sorting method however it allows only the top layer to be visible, any overlaping layers below the top one will be ignored. We use this option as default. Take the following screenshot as example, notice that you can see through some part of her hair. This is because the hair layers below are invisible.  
![Z Sorting On](/pages/zsorting_on.png)

You can uncheck the toggle if you wish all transparent materials to be renderred. But this often leads to other problems like the image below, the horns are being coverred by hair behind it. 
![Z Sorting Off](/pages/zsorting_off.png)

To address this, you can go to the material settings, find the material that renders the horns, and change it to opaque type. 
![Set Opaque Type](/pages/type_opaque.png)

Furthermore, you notice that the facepaint on her face doesn't look quite right, this is due to the material is incorrectly set to opaque, letting the edge of the image to show up in rendering. You can fix this by setting its type to transparent.
![Set Transparent Type](/pages/type_transparent.png)
