### Issues With Transparency

Transparent materials are tricky. They can overlap incorrectly and render unexpected color on top of certain parts if not set correctly. 

We try our best to provide a usable default configuration but often you'll need to manually tweak each model to make them look perfect.

There are a few tools within DanceXR that you can use to achieve this.

First thing you can try is "Transparency Sorting". This setting configures how transparent materials are sorted in order to address sorting issues. 

The toggle (available in HD variant only) turns on Z sorting, it is the most accurate sorting method however it allows only the top layer to be visible, any overlaping layers below the top one will be ignored. We use this option as default. Take the following screenshot as example, notice that you can see through some part of her hair. This is because the hair layers below are invisible.  

![Z Sorting On](/pages/zsorting_on.png)

You can uncheck the toggle if you wish all transparent materials to be renderred. See the result from the image below. Now hair looks great but you can see that this created another problem for this model, the horns are now covered by hair where they shouldn't be. 

![Z Sorting Off](/pages/zsorting_off.png)

Luckily problems like this can be solved by changing the material type of the horns. You can go to the material settings, find the material that renders the horns, and change it to opaque type. 

![Set Opaque Type](/pages/type_opaque.png)

Now this looks almost perfect but there is still a minor problem: the facepaint on her face doesn't look quite right. This is due to the face paint material is incorrectly set to skin type (due to the fact that we determine material types by checking certain keywords from the material names. Since it contains the word "face", the program set it as "skin" type by default). This made the edge of the image to show up incorrectly. You can fix this by setting its type to transparent.

![Set Transparent Type](/pages/type_transparent.png)
