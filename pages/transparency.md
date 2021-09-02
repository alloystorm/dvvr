### Issues With Transparency

Transparent materials are tricky. They can overlap incorrectly and render unexpected color on top of certain parts if not set correctly. 

We try our best to provide a usable default configuration but often you'll need to manually tweak each model to make them look perfect.

XPS models usually don't require any manual tweaking since the model definition tells us what is transparent and what is not. But PMX doesn't have this and the program has to determine by itself what to do with the materials. Currently (version 1.1) the HD variant uses transparent mode as default (since it has the zsorting capability and that provides an acceptable default behavior) and LW uses opaque as default. 

There are a few tools within DanceXR that you can use to tweak transparency behaviours.

First thing you can try is "Transparent Sorting". This setting configures how transparent materials are sorted. The default option is "use mesh order" which means they are sorted with the same order that their mesh are defined in the file. Usually they are orderred from inside out and that's exactly what we needed.  

The toggle (available in HD variant only) turns on Z sorting, it uses z buffer to determine what is visible and what is not. This present a very accurate result however it allows only the top layer to be visible since there can only be one z value for each pixel, any overlaping layers below the top one will be ignored. We use this option as default. Take the following screenshot as example, the sorting is perfect, nothing covers what it shouldn't be but you can see through some part of her hair. That is because the hair layers below are invisible.  

![Z Sorting On](/pages/zsorting_on.png)

You can uncheck the toggle if you wish all transparent materials to be renderred. See the result from the image below. Now hair looks great but you can see that this created another problem for this model, the horns are now covered by hair where they shouldn't be. 

![Z Sorting Off](/pages/zsorting_off.png)

Luckily problems like this can be solved by changing the material type of the items being covered. You can go to the material settings, find the material that renders the horns, and change it to opaque type. This will allow it to be renderred before transparent materials and the z depth test can prevents incorrect ordering from happening.  

![Set Opaque Type](/pages/type_opaque.png)

Now this looks almost perfect but there is still a minor problem: the facepaint on her face doesn't look quite right. This is due to the face paint material is incorrectly set to skin type (due to the fact that we determine material types by checking certain keywords from the material names. Since it contains the word "face", the program set it as "skin" type by default). This made the edge of the image to show up incorrectly. You can fix this by setting its type to transparent.

![Set Transparent Type](/pages/type_transparent.png)
